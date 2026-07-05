# The Eclipse Lamp

A fully normal-looking modern lamp that secretly conceals a covert camera system, complete with a mechanical iris that rotates to reveal it, activating AI person detection for your security, while sending real-time alerts to your phone.

![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi-C51A4A?logo=raspberrypi&logoColor=white)
![status](https://img.shields.io/badge/status-in%20progress-orange)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Notifications](https://img.shields.io/badge/Alerts-Pushover%20%7C%20ntfy%20%7C%20Telegram-green)
![Hackathon](https://img.shields.io/badge/Hack%20Club-Starhacks-blue)
![Servo](https://img.shields.io/badge/Actuator-SG90%20Servo-blue)
![AI Model](https://img.shields.io/badge/AI-YOLOv8n-purple)
![Camera](https://img.shields.io/badge/Camera-Pi%20Camera%20Module-lightgrey)
__________________________________________________________________________________________________________________________________________

## Principle of Operation (How it works):

+ Idle state: The iris stays closed. The pan servo slowly sweeps the camera left and right at a slow, subtle pace — just enough to suggest the room is being scanned without looking erratic.
+ Iris cycle: Every 5–10 seconds, the iris servo opens the shutter, exposing the camera lens for about 5 seconds, then closes it again. This loop repeats continuously.
+ Detection: While the iris is open, the camera feed runs through a lightweight on-device AI model to check for a person in frame.
+ Alert: If a person is detected, the Pi sends a push notification to the owner's phone or computer.
+ Lock-on: Instead of continuously tracking the person, the pan servo snaps to their last known horizontal position and holds there — giving the impression of "locking on" without needing full live tracking.

__________________________________________________________________________________________________________________________________________

### Main features:

* Disguise — built to look and function like an ordinary lamp

* Mechanical iris — servo-driven cover that opens/closes on a timed loop, mimicking a real camera aperture

* Idle pan sweep — slow side-to-side motion during downtime, no live feedback loop required

* On-device AI person detection — lightweight model (e.g. YOLOv8n) running locally on the Pi

* Push notifications — alerts sent to phone/computer on detection (e.g. via Pushover, ntfy, or a Telegram bot)

* Lock-on behavior — servo holds position at the last detected location instead of continuously tracking

* Pi-managed lamp power — the lamp's light circuit is wired through the Pi so it can be controlled as part of the system



| Component | Info |
| ------------------ | ------------------- |
| Raspberry Pi(Computer)    |4B, 2GB |
| 2x SG90     | 9g Micro Servo Motor |
|Lamp Module  | Bambu Lab Lamp Module Kit 001 |
|Raspberyr Pi Cammera Module| Rpicam V2 noIR |
|Power supply | 5V 3A Designated Rasp Pi Supply
|Frame | PLA 3D-printed models ~ 220g
Firmware | YOLO (Ultralytics), Python Libraries, Bash requests
|Other 3D printed parts| PLA 3D-printed models ~ 50g
|Alert Software | Pushover/ntfy/Telegram


### Repository Structure

```
The-Eclipse-Lamp/
├── bash requests/                           # Setup and utility scripts
│   ├── 01-Raspberry_Pi_Setup.sh             # Initial Pi OS/environment setup
│   ├── 02-Install_AI_and_Python_Packages.sh # Bashes to install packages
│   ├── 03-Camera_Testing_in_Browser.sh      # Launches browser-based camera test
│   └── 04-Run_Final_Detection_Program.sh    # Runs final person-detection prog
├── hardware/                                # Build docs for physical components
│   ├── 01-Mechanical Iris Construction.md   # Building the iris mechanism
│   ├── 02-Bottom Lamp Construction.md       # Bottom stand build 
│   ├── 03-Top Lamp Construction.md          # Top shell build
│   ├── 04-Camera - Iris Frame.md            # Frame mounting camer and iris
│   ├── 05-Iris Face Extension.md            # Extension piece iris to wall
│   ├── Custom Created CAD Models.md         # Custom-designed CAD parts
│   └── KiCad Wiring Schematic.md            # Electrical wiring schematic(KiCad)
├── detect_test.py                   # Script for testing the AI detection model
├── server.py                        # Server handling camera feed / notifications
├── LICENSE                          # Project license
├── README.md                        # Project overview and documentation
└── SECURITY.md                      # Security policy / reporting info
```

### Quick Start 

1. Hardware Assembly

See the hardware folder for all docs and building processes in order 
See the B.O.M.csv for all hardware parts and components

2. Bash Requests

SSH into your Pi and see the bash requests folder for all bashes to run into terminal
Run code in order

3. Power

Attach power supply to the raspberry pi from wall outlet to the bottom shell
Find the Lamp button in the back and turn it on

4. Push Notifications

Set your phone or computer up to receive push notifications of person detection in your room

5. Your Finished! 

Have Fun with your new Security System at home!

