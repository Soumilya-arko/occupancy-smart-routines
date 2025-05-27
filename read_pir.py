import RPi.GPIO as GPIO
import time

PIR_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Wait 0.1s and read
time.sleep(0.1)
motion = GPIO.input(PIR_PIN)
print(motion)

GPIO.cleanup()
