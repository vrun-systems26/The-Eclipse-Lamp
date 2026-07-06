cd ~/eclipse_lamp
python3 -m venv venv --system-site-packages
source venv/bin/activate
pip install numpy==1.26.4
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
pip install ultralytics flask onnxruntime
python3 -c "from ultralytics import YOLO; model = YOLO('yolov8n.pt'); model.export(format='onnx', imgsz=640)"