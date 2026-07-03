#!/bin/bash

cd ~/eclipse_lamp
source venv/bin/activate

# Test that Raspberry Pi detects the camera
rpicam-hello

# Run browser stream
python3 server.py

#To open in browser type http://YOUR RASPBERRY PI IP:5000

#Find Raspberry pi IP
hostname -I

#If camera is busy
ps aux | grep python

kill -9 PID_NUMBER 
#PID_NUMBER is the number that shows up first in the table
