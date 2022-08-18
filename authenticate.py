# author: Monika Zamlynska
# e-mail: monika.zamlynska@gmail.com
# 2022-08-18

#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)

reader = SimpleMFRC522()

try:

	id, text =  reader.read()

	if(id == 876685318416):
		GPIO.output(8, GPIO.HIGH)
		sleep(1)
	else:
		GPIO.output(10, GPIO.HIGH)
		sleep(1)


finally:


	GPIO.cleanup()
