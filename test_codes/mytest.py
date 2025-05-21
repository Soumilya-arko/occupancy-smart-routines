import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Use GPIO 2
LED_PIN = 3
# Set up the pin as output
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        print("Running ... \n")
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
        time.sleep(0.2)
        GPIO.output(LED_PIN, GPIO.LOW)   # Turn off LED
        time.sleep(0.2)
        
        
except KeyboardInterrupt:
    print("Stopped by User")

finally:
    GPIO.cleanup()

