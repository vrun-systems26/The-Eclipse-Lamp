cd ~/eclipse_lamp
source venv/bin/activate

python3 detect_test.py

#__________________________
#Other Helpful Commands:

#If camera busy
ps aux | grep python
kill -9 PID
#PID is the number that shows up in the first row

#Activate virtual environment
cd ~/eclipse_lamp
source venv/bin/activate

#Leave virtual environment
deactivate

#Check Raspberry Pi IP
hostname -I

#Test Camera without AI or Live View(Very Important)
rpicam-hello

#Test YOLO works after installation
python3 -c "from ultralytics import YOLO; print('YOLO Ok')"

#Chech Camera Processes
ps aux | grep detect

#Edit Python Files
nano detect_test.py
#or
nano server.py
