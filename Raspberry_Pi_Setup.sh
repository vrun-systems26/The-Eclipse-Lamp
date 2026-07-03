#!/bin/bash

# Update Raspberry Pi
sudo apt update
sudo apt upgrade -y

# Enable Camera
sudo raspi-config
# Interface Options -> Camera -> Enable
# Reboot afterwards

sudo reboot

# Install camera software
sudo apt install -y python3-picamera2 python3-opencv python3-flask git

# Make project folder
mkdir ~/eclipse_lamp
cd ~/eclipse_lamp

# Create Python virtual environment
python3 -m venv venv
source venv/bin/activate
