# author: Monika Zamlynska
# e-mail: monika.zamlynska@gmail.com
# 2022-08-18

#!/usr/bin/env python

import RPi.GPIO as GPIO # import biblioteki do GPIO
from mfrc522 import SimpleMFRC522 # import biblioteki do sensora RFID
from time import sleep # import dodatków do sleep'owania procesów

import time # importowanie daty i godziny

GPIO.setwarnings(False)

# deklarowanie numerów pin

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(10, GPIO.OUT, initial = GPIO.LOW)

reader = SimpleMFRC522() # deklaracja modulu do sensora RFID

plik = open('rfid_login.log','a')

dzisiejsza_data = datetime.datetime.now()

try:

	id, text =  reader.read() # czytanie z sensora RFID

	if(id == 876685318415): # jezeli ID karty wynosi tyle co podane, to zapal zielona diode LED
		GPIO.output(8, GPIO.HIGH)
		print("Witaj ", text,  "! Masz uprawnienia na wejscie do serwerowni")

		# dodawanie logu do pliku
		plik.write("\n")
		print (time.strftime("[ %Y-%m-%d %H:%M]    "))
		plik.write("AUTORYZACJA: [")
		plik.write(str(id))
		plik.write("]: ")
		plik.write(text)

		sleep(1)
	else:
		GPIO.output(10, GPIO.HIGH) # jezeli nie, to zapal czerwona diode LED
		print("Niestety nie masz uprawnien na wejscie do serwerowni!!! Skontaktuj się z Administratorem")

		# dodawanie logu do pliku
		plik.write("\n")
		plik.write("NIEAUTORYZOWANE: [")
		plik.write(str(id))
		plik.write("]: ")
		plik.write(text)

		sleep(1)

finally:

	GPIO.cleanup()

# zmiana monisia 5