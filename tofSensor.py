import time, board, adafruit_vl53l1x

i2c = board.I2C()

tofSensor = adafruit_vl53l1x.VL53L1X(i2c)

tofSensor.distance_mode = 2 # Long range mode
tofSensor.timing_budget = 100 # ms
tofSensor.start_ranging()

while 1:
	if (tofSensor.data_ready):
		print(f"Distance: {tofSensor.distance}cm")
		tofSensor.clear_interrupt()
	time.sleep(0.1)
