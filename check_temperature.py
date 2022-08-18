# author: Monika Zamlynska
# e-mail: monika.zamlynska@gmail.com
# 2022-08-18

#!/usr/bin/env python

import time # biblioteka time
import w1thermsensor # biblioteka do sensora temperatury DS18B20

sensor = w1thermsensor.W1ThermSensor() # deklaracja zmiennej sensora

while True:
	temperature = sensor.get_temperature() # pobieranie temperatury
	print("Temperature: {:.1f}*C ".format(temperature)) # wypisywanie temperatury
	time.sleep(1)

