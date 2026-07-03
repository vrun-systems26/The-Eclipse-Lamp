#!/bin/bash

cd ~/eclipse_lamp
source venv/bin/activate

# Install compatible NumPy first
pip install numpy==1.26.4

# Install Ultralytics (YOLO)
pip install ultralytics

# Install browser streaming packages
pip install flask opencv-python

# Test YOLO installation
python3 -c "from ultralytics import YOLO; print('YOLO Installed!')"
