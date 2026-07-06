# The Eclipse Lamp

A fully normal-looking modern lamp that secretly conceals a covert camera system, complete with a mechanical iris that rotates to reveal it, activating AI person detection for your security, while sending real-time alerts to your phone.

![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi-C51A4A?logo=raspberrypi&logoColor=white)
![status](https://img.shields.io/badge/status-in%20progress-orange)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Notifications](https://img.shields.io/badge/Alerts-Telegram-green)
![Servo](https://img.shields.io/badge/Actuator-SG90%20Servo-blue)
![AI Model](https://img.shields.io/badge/AI-YOLOv8n-purple)
![Hackathon](https://img.shields.io/badge/Hack%20Club-Starhacks-pink)
![Camera](https://img.shields.io/badge/Camera-Pi%20Camera%20Module-lightgrey)

__________________________________________________________________________________________________________________________________________

## Principle of Operation (How it works):

+ Idle state: The iris stays closed. The pan servo slowly sweeps the camera left and right at a slow, subtle pace — just enough to suggest the room is being scanned without looking erratic.
+ Iris cycle: Every 5–10 seconds, the iris servo opens the shutter, exposing the camera lens for about 5 seconds, then closes it again. This loop repeats continuously.
+ Detection: While the iris is open, the camera feed runs through a lightweight on-device AI model to check for a person in frame.
+ Alert: If a person is detected, the Pi sends a push notification to the owner's phone or computer through Telegram.
+ Lock-on: Instead of continuously tracking the person, the pan servo snaps to their last known horizontal position and holds there — giving the impression of "locking on" without needing full live tracking.
__________________________________________________________________________________________________________________________________________

## Main features:

* Disguise — built to look and function like an ordinary lamp

* Mechanical iris — servo-driven cover that opens/closes on a timed loop, mimicking a real camera aperture

* Idle pan sweep — slow side-to-side motion during downtime, no live feedback loop required

* On-device AI person detection — lightweight model (e.g. YOLOv8n) running locally on the Pi

* Push notifications — alerts sent to phone/computer on detection (Telegram bot)

* Lock-on behavior — servo holds position at the last detected location instead of continuously tracking

* Pi-managed lamp power — the lamp's light circuit is wired through the Pi so it can be controlled as part of the system

__________________________________________________________________________________________________________________________________________


## Core components:

| Component | Info |
| ------------------ | ------------------- |
| Raspberry Pi(Computer)    |4B, 2GB |
| 2x SG90     | 9g Micro Servo Motor |
|Lamp Module  | Bambu Lab Lamp Module Kit 001 |
|Raspberry Pi Camera Module| RPiCam V2 NoIR |
|Power supply | 5V 3A Designated Rasp Pi Supply
|Frame | PLA 3D-printed models ~ 220g
|Firmware | YOLO (Ultralytics), Python Libraries, Bash requests
|Other 3D printed parts| PLA 3D-printed models ~ 50g
|Alert Software | Telegram

__________________________________________________________________________________________________________________________________________

## Repository Structure

```
The-Eclipse-Lamp/
├── bash requests/                              # Setup and utility scripts
│   ├── 01-Raspberry_Pi_Setup.sh                # Initial Pi OS/environment setup
│   ├── 02-Install_AI_and_Python_Packages.sh    # Bashes to install packages
│   ├── 03-Camera_Testing_in_Browser.sh         # Launches browser-based camera test
│   ├── 04-Run_Final_Detection_Program.sh       # Runs final person-detection program
|   ├── detect.py                               # Final program for Telgram/AI detection
|   ├── iris_test.py                            # Mechanical Iris physical limit test
|   └── notify_test.py                         # Telegram test from Pi to user through chatbot 
├── hardware/                                   # Build docs for physical components
│   ├── 01-Mechanical Iris Construction.md      # Building the iris mechanism
│   ├── 02-Bottom Lamp Construction.md          # Bottom stand build 
│   ├── 03-Top Lamp Construction.md             # Top shell build
│   ├── 04-Camera - Iris Frame.md               # Frame mounting camera and iris
│   ├── 05-Iris Face Extension.md               # Extension piece iris to wall
│   ├── Custom Created CAD Models.md            # Custom-designed CAD parts
│   └── KiCad Wiring Schematic.md               # Electrical wiring schematic(KiCad)
├── LICENSE                                     # Project license
├── README.md                                   # Project overview and documentation
├── .gitignore                                  # Excludes model files, venv, and cache from version control
└── SECURITY.md                                 # Security policy / reporting info
```
__________________________________________________________________________________________________________________________________________

## Power Distribution — how power reaches everything

```
[Wall Outlet / Power Supply]
         |
   [Raspberry Pi 5V/3A]
         |
   ┌─────┼──────────────┬───────────────────────┐
   |     |              |                       |
[Pan   [Iris       [Lamp Module]         [Pi Camera Module]
Servo] Servo]   (Pi-controlled)

```

## Signal / Data Flow — how the Pi talks to each component

```
[Raspberry Pi]
   ├── GPIO --> Pan Servo (idle sweep / lock-on position)
   ├── GPIO --> Iris Servo (open/close timing loop)
   ├── CSI Ribbon --> Pi Camera (video feed)
   └── GPIO --> Lamp Circuit (on/off control)
```
## Detection / Alert Pipeline

```
[Camera Feed] --> [On-device AI Model (YOLOv8n.onnx)]
                        |
                  Person detected?
                    /         \
                  No           Yes
                   |             |
            (loop continues)  [Push Notification --> Phone/PC by Telegram]
                                  |
                          [Pan Servo Locks to Position]
```
__________________________________________________________________________________________________________________________________________

## Resources/Credits

**Hardware:**

+ Raspberry Pi (Model B)
+ Raspberry Pi Camera Module V2 NoIR
+ Servo motors (for the pan/iris systems)
+ LED lamp/light source
+ Raspberry Pi power supply
+ USB cable
+ 3D printer
+ PLA filament

**Software:**
- Raspberry Pi OS
- Python 3
- Visual Studio Code (or Nano for editing on the Pi)
- Terminal/Bash
- Git
- Python Libraries
  - Flask
  - OpenCV (cv2)
  - Ultralytics YOLO
  - NumPy
  - ONNX Runtime
  - pigpio
  - requests

**CAD & Design:**
- Onshape
- Tinkercad

**Electronics Design**
- KiCad

**Raspberry Pi Utilities**
- rpicam-hello
- libcamera
- raspi-config

**Online Resources:**
- Raspberry Pi Documentation
- Picamera2 Documentation
- Ultralytics YOLO Documentation
- Flask Documentation
- OpenCV Documentation
- GitHub
- Printables (Tremors)
- Thingiverse (Lore09, thirdhorizon)
- YOLOv8 Nano (yolov8n.pt)
- VNC Viewer (for remote Raspberry Pi desktop access)
- 3D printer slicer (Cura)

**People/Help**
- My friend Rishith (rishithc) helped me getting better acquainted with GitHub
- ChatGPT and Claude (for debugging, troubleshooting, explaining concepts, and helping develop the software pipeline)
