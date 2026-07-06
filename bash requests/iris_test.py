#This tests the physical limits of my iris servo to find the angle range of the mechanism opening/closing
# To run bash: python3 iris_test.py

from gpiozero import AngularServo, Device
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import threading

Device.pin_factory = PiGPIOFactory()

SERVO_PIN = 27 # (GPIO 27 or pin 13 on the Raspberry Pi)

servo = AngularServo(SERVO_PIN, min_angle=0, max_angle=180,
                     min_pulse_width=0.0005, max_pulse_width=0.0025)

current_angle = 0
direction = 1
min_angle = 0  # I used this range for my servo for physical limits (0-63), you will have a different one
max_angle = 63 # I used this range for my servo for physical limits (0-63), you will have a different one
step_size = 1
step_delay = 0.04
running = True

def listen_for_input():
    global direction
    while running:
        user_input = input()
        if user_input.strip() == "1":
            print(f"{current_angle} degrees current angle")
            direction *= -1
            print(f"Reversing loop direction. Now looping {'0 -> 63' if direction == 1 else '63 -> 0'}")

listener_thread = threading.Thread(target=listen_for_input, daemon=True)
listener_thread.start()

print("Looping 0-63 degrees. Type 1 and press Enter to reverse loop direction.")

try:
    while True:
        current_angle += direction * step_size

        if current_angle > max_angle:
            current_angle = min_angle
        elif current_angle < min_angle:
            current_angle = max_angle

        servo.angle = current_angle
        sleep(step_delay)

except KeyboardInterrupt:
    running = False
    servo.detach()
    print("\nStopped.")