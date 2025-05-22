import RPi.GPIO as GPIO
import time

# Pin Definitions
PIR_PIN = 17     # GPIO pin for PIR OUT
LED_PIN = 4     # GPIO pin for LED

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

print("Waiting for PIR to stabilize (1 min)...")
time.sleep(60)  # Initial warm-up period for PIR per datasheet

print("PIR ready. Monitoring motion...")

try:
    while True:
        motion = GPIO.input(PIR_PIN)

        if motion:
            print("Motion detected → Blinking LED")
            # Blink LED continuously while motion is detected
            while GPIO.input(PIR_PIN) == 1:
                GPIO.output(LED_PIN, GPIO.HIGH)
                time.sleep(0.3)
                GPIO.output(LED_PIN, GPIO.LOW)
                time.sleep(0.3)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)  # Ensure LED is off when no motion
            time.sleep(0.5)

except KeyboardInterrupt:
    print("Program stopped by user.")
    GPIO.cleanup()
