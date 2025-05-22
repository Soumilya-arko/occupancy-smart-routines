import RPi.GPIO as GPIO
import time

# --- Configuration ---
PIR_PIN = 17  # GPIO pin connected to HC-SR501 OUT

# --- GPIO Setup ---
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
print("Initializing PIR sensor...")
time.sleep(60)  # Allow sensor to initialize (as per datasheet)
print("Ready for motion detection!")

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion Detected!")
        else:
            print("No motion.")
        time.sleep(1)  # Delay to reduce CPU usage

except KeyboardInterrupt:
    print("Motion detection stopped by user.")

finally:
    GPIO.cleanup()
