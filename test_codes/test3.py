import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for Trig and Echo
TRIG = 4
ECHO = 17
LED_PIN = 27


# Set up the GPIO pins
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

def measure_distance():
    # Send a 10us pulse to trigger the sensor
    GPIO.output(TRIG, True)
    time.sleep(0.00001)  # 10 microseconds
    GPIO.output(TRIG, False)

    # Wait for the echo to start
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
        

    # Wait for the echo to end
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        
    # Calculate the pulse duration
    pulse_duration = pulse_end - pulse_start

    # Calculate distance in cm (speed of sound is 34300 cm/s)
    distance = pulse_duration * 17150  # distance in cm
    print(distance)
    return distance

try:
    while True:
        dist = measure_distance()
        print(f"Distance: {dist:.2f} cm")
        if dist<5:
            GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
            time.sleep(0.2)
            GPIO.output(LED_PIN, GPIO.LOW)   # Turn off LED
            time.sleep(0.2)
        
        time.sleep(0.2)  # Wait for 1 second before the next measurement

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()  # Clean up GPIO on exit
    
