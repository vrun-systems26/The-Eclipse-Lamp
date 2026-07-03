#In terminal type nano server.py and paste this entire code, then ctr X, Y, Enter

from flask import Flask, Response
from picamera2 import Picamera2
import cv2

app = Flask(__name__)

# Initialize camera
picam2 = Picamera2()

config = picam2.create_preview_configuration(
    main={"size": (640, 480)}
)

picam2.configure(config)
picam2.start()


def generate_frames():
    while True:
        frame = picam2.capture_array()

        # Convert RGB to BGR for OpenCV
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        ret, buffer = cv2.imencode('.jpg', frame)

        if not ret:
            continue

        frame = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' +
            frame +
            b'\r\n'
        )


@app.route('/')
def index():
    return """
    <html>
        <head>
            <title>Eclipse Lamp Camera</title>
        </head>
        <body style="text-align:center; background:#111; color:white;">
            <h1>Eclipse Lamp Live Camera Feed</h1>
            <img src="/video_feed" width="800">
        </body>
    </html>
    """


@app.route('/video_feed')
def video_feed():
    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
