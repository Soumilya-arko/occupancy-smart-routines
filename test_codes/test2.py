import RPi.GPIO as GPIO
import time

a = [1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1]
# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Use GPIO 3
LED_PIN = 3
# Set up the pin as output
GPIO.setup(LED_PIN, GPIO.OUT)

c=0

try:
    while (c<len(a)): 
        print("Running ... \n")
        if a[c] == 1:
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(1)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(1)
            
        c+=1

except KeyboardInterrupt:
    print("Stopped by User")

finally:
    GPIO.cleanup()
