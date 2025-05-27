import time
import board
import adafruit_scd4x

i2c = board.I2C()
scd4x = adafruit_scd4x.SCD4X(i2c)
scd4x.start_periodic_measurement()

time.sleep(5)

if scd4x.data_ready:
    print(scd4x.CO2)
