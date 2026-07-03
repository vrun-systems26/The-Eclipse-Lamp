# The Eclipse Lamp

A fully normal-looking modern lamp that secretly conceals a covert camera system, complete with a mechanical iris that rotates to reveal it, activating AI person detection for your security, while sending real-time alerts to your phone.

[![License: MIT](https://shields.io)](https://opensource.org)
[![build](https://shields.io)](https://github.com)
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

  ###### STATUS: In progress for Hackclub Starhacks
