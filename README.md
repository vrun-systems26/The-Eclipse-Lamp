# The Eclipse Lamp

Spy Lamp

A fully normal-looking modern lamp that secretly conceals a covert camera system — complete with a mechanical iris that rotates to reveal a camera that peeks at the room, activates AI person detection for your security, sends real-time alerts to your phone.


Core Concept

From the outside, it's just a lamp on your desk or shelf. It lights up like one, sits like one, and does nothing to suggest otherwise. Hidden inside is a Raspberry Pi-powered camera system, covered by a mechanical iris that only opens periodically to scan the room. When the onboard AI detects a person, it sends you a notification and the camera "locks on" to their last known position.

Components

  Some of the main components consist of, a Raspberry Pi 4 B Main controller running detection, servo logic, and notifications, a Pi Camera Module acting as an eye capturing the room for AI processing, the SG90 Servo Motor #1 (Iris) Opening/closing a mechanical iris/shutter covering the lens, the Servo #2 (Pan) Slowly sweeping the camera left/right during idle scanning, a 3d printed Lamp housing or a modified modern lamp shell, able to hide the Pi, camera, servos, and wiring, and finally the USB-powered lamp light that will be the main light source connected to the Pi.

  Note: This project will require the use of a wall outlet or external power supply

Idle state: The iris stays closed. The pan servo slowly sweeps the camera left and right at a slow, subtle pace — just enough to suggest the room is being scanned without looking erratic.
Iris cycle: Every 5–10 seconds, the iris servo opens the shutter, exposing the camera lens for about 5 seconds, then closes it again. This loop repeats continuously.
Detection: While the iris is open, the camera feed runs through a lightweight on-device AI model to check for a person in frame.
Alert: If a person is detected, the Pi sends a push notification to the owner's phone or computer.
Lock-on: Instead of continuously tracking the person, the pan servo snaps to their last known horizontal position and holds there — giving the impression of "locking on" without needing full live tracking.

Main features:

Disguise-first design — built to look and function like an ordinary lamp
Mechanical iris — servo-driven cover that opens/closes on a timed loop, mimicking a real camera aperture
Idle pan sweep — slow side-to-side motion during downtime, no live feedback loop required
On-device AI person detection — lightweight model (e.g. YOLOv8n, MobileNet-SSD, or Pi AI Camera) running locally on the Pi
Push notifications — alerts sent to phone/computer on detection (e.g. via Pushover, ntfy, or a Telegram bot)
Lock-on behavior — servo holds position at the last detected location instead of continuously tracking
Pi-managed lamp power — the lamp's light circuit is wired through the Pi so it can be controlled as part of the system

Status: In progress for Hackclub Starhacks

⚠️ Disclaimer

This project is intended for personal use in spaces you own or have full rights to monitor (e.g. your own home/office). Always check local laws regarding recording and surveillance before deploying anything like this in spaces shared with others.
