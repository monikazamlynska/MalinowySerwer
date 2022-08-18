# author: Monika Zamlynska
# e-mail: monika.zamlynska@gmail.com
# 2022-08-18

#!/usr/bin/env python

import RPi.GPIO as GPIO # import biblioteki do GPIO
from mfrc522 import SimpleMFRC522 # import biblioteki do sensora RFID
from time import sleep # import dodatków do sleep'owania procesów

GPIO.setwarnings(False)

# deklarowanie numerów pin

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(10, GPIO.OUT, initial = GPIO.LOW)

reader = SimpleMFRC522() # deklaracja modulu do sensora RFID

try:

	id, text =  reader.read() # czytanie z sensora RFID

	if(id == 876685318416): # jezeli ID karty wynosi tyle co podane, to zapal zielona diode LED
		GPIO.output(8, GPIO.HIGH)
		sleep(1)
	else:
		GPIO.output(10, GPIO.HIGH) # jezeli nie, to zapal czerwona diode LED
		sleep(1)

finally:

	GPIO.cleanup()
