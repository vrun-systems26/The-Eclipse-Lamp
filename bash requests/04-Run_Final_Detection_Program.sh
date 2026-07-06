cd ~/eclipse_lamp
source venv/bin/activate
python3 detect.py

# This will run detect.py — the main detection, streaming, and notification script
# Open the live camera feed in your browser at http://YOUR_PI_IP:5000
# Find your Pi IP with: hostname -I

#__________________________
# Other Helpful Commands:

# If camera busy
ps aux | grep python
kill -9 PID
# PID is the number that shows up in the first row

# Activate virtual environment
cd ~/eclipse_lamp
source venv/bin/activate

# Leave virtual environment
deactivate

# Check Raspberry Pi IP
hostname -I

# Test camera without AI or live view (very important)
rpicam-hello

# Test YOLO works after installation
python3 -c "from ultralytics import YOLO; print('YOLO Ok')"

# Check camera processes
ps aux | grep detect

# Run iris servo test
python3 iris_test.py

# Test Telegram notifications independently
python3 notify_test.py

# Export YOLO model to ONNX format (only needed once)
python3 -c "from ultralytics import YOLO; model = YOLO('yolov8n.pt'); model.export(format='onnx', imgsz=640)"

# Check swap space
cat /proc/meminfo | grep Swap