import RPi.GPIO as GPIO
import time

# GPIO setup
PIR_PIN = 2     # GPIO pin for PIR OUT
LED_PIN = 4     # GPIO pin for LED

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

print("Motion detection started. Press Ctrl+C to exit.")

try:
    while True:
        motion = GPIO.input(PIR_PIN)
        if motion:
            GPIO.output(LED_PIN, GPIO.HIGH)
            print("Motion Detected: LED ON")
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            print("No Motion: LED OFF")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Program stopped.")
    GPIO.cleanup()


