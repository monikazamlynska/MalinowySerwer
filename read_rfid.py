# author: Monika Zamlynska
# e-mail: monika.zamlynska@gmail.com
# 2022-08-18

#!/usr/bin/env python

import RPi.GPIO as GPIO # import biblioteki do GPIO
from mfrc522 import SimpleMFRC522 # import biblioteki do sensora RFID

reader = SimpleMFRC522() # deklaracja modulu do sensora RFID

# deklaracja wyjatkow
try:

	id, text =  reader.read() # pobierz wartosci z karty RFID
	print("Numer ID: {:.1f} " .format(id)) # wypisz wartosci ID z karty RFID
	print("Wlasciciel: ", text) # wypisz wartosci tekstowe  z karty RFID

finally:

	GPIO.cleanup()
