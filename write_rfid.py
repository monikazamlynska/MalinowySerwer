# author: Monika Zamlynska
# e-mail: monika.zamlynska@gmail.com
# 2022-08-18


#!/usr/bin/env python

import RPi.GPIO as GPIO # import biblioteki do GPIO
from mfrc522 import SimpleMFRC522 # import biblioteki do sensora RFID

reader = SimpleMFRC522() # deklaracja modulu do sensora RFID

try:

	text = input("Nowe dane do karty RFID: ")
	print("Przyloz karte RFID: ")
	reader.write(text)
	print("Wczytywanie...")
finally:

	GPIO.cleanup()
