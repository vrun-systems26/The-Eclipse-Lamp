#In terminal type nano detect_test.py and paste this entire code, then ctr X, Y, Enter

from flask import Flask, Response
from picamera2 import Picamera2
from ultralytics import YOLO
import cv2

app = Flask(__name__)

model = YOLO("yolov8n.pt")

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(
    main={"format": "RGB888", "size": (640, 480)}
))
picam2.start()


def generate_frames():
    frame_count = 0

    while True:
        frame = picam2.capture_array()

        results = model(frame)
        annotated_frame = results[0].plot()

        _, buffer = cv2.imencode('.jpg', annotated_frame)
        frame_bytes = buffer.tobytes()

        frame_count += 1
        print(f"Frame {frame_count} processed")

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


@app.route('/')
def index():
    return """
    <h1>YOLO Live Stream</h1>
    <img src="/video_feed" width="640">
    """


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    print("Server running at http://0.0.0.0:5000")
    app.run(host="0.0.0.0", port=5000, debug=False)
