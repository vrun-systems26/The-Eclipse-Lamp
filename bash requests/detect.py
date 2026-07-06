# detect.py
# Run with: python3 detect.py
# Open stream at: http://YOUR_PI_IP:5000

from flask import Flask, Response
from picamera2 import Picamera2
from ultralytics import YOLO
import cv2
import threading
import time
import requests

# ─── Telegram Config ─────────────────────────────────────────────
TOKEN = "8650998287:AAErARyPcKYPFD7-v5lycO44k_IRaZ5Li7o"
CHAT_ID = "8951826527"

def send_alert():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": "🚨 Eclipse Lamp: Person detected in the room!"
    })

# ─── Settings ────────────────────────────────────────────────────
ALERT_COOLDOWN     = 60   # seconds between notifications
DETECTION_INTERVAL = 2.0  # seconds between YOLO runs
RESOLUTION         = (640, 480)

# ─── State ───────────────────────────────────────────────────────
latest_raw_frame  = None
overlay_frame     = None
frame_lock        = threading.Lock()
overlay_lock      = threading.Lock()
last_alert_time   = 0

# ─── Load model ──────────────────────────────────────────────────
print("Loading YOLO model...")
model = YOLO("yolov8n.onnx", task="detect")
model.overrides["workers"] = 4
print("YOLO ready")

# ─── Camera ──────────────────────────────────────────────────────
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(
    main={"format": "RGB888", "size": RESOLUTION}
))
picam2.start()
time.sleep(2)

# ─── Camera capture thread ───────────────────────────────────────
def capture_loop():
    global latest_raw_frame
    while True:
        frame = picam2.capture_array()
        with frame_lock:
            latest_raw_frame = frame

# ─── YOLO detection thread ───────────────────────────────────────
def detection_loop():
    global overlay_frame, last_alert_time
    while True:
        time.sleep(DETECTION_INTERVAL)

        with frame_lock:
            frame = latest_raw_frame
        if frame is None:
            continue

        results = model(frame, classes=[0], verbose=False, imgsz=640)

        if len(results[0].boxes) > 0:
            now = time.time()
            if now - last_alert_time > ALERT_COOLDOWN:
                last_alert_time = now
                print("Person detected — sending alert")
                threading.Thread(target=send_alert, daemon=True).start()

        annotated = results[0].plot()
        with overlay_lock:
            overlay_frame = annotated

# ─── Flask stream ────────────────────────────────────────────────
app = Flask(__name__)

def generate_frames():
    while True:
        with overlay_lock:
            frame = overlay_frame
        if frame is None:
            with frame_lock:
                frame = latest_raw_frame
        if frame is None:
            time.sleep(0.05)
            continue
        _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 70])
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' +
               buffer.tobytes() + b'\r\n')

@app.route('/')
def index():
    return """
    <html>
        <head><title>Eclipse Lamp</title></head>
        <body style="background:#111; color:white; text-align:center;">
            <h1>Eclipse Lamp — Live Feed</h1>
            <img src="/video_feed" width="640">
        </body>
    </html>
    """

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# ─── Start ───────────────────────────────────────────────────────
if __name__ == "__main__":
    threading.Thread(target=capture_loop, daemon=True).start()
    threading.Thread(target=detection_loop, daemon=True).start()
    print("Stream running at http://0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000, debug=False, threaded=True)