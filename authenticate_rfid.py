# author: Monika Zamlynska
# e-mail: monika.zamlynska@gmail.com
# 2022-08-18

#!/usr/bin/env python

import RPi.GPIO as GPIO # import biblioteki do GPIO
from mfrc522 import SimpleMFRC522 # import biblioteki do sensora RFID
from time import sleep # import dodatków do sleep'owania procesów
import datetime

# polaczenie z baza danych

import psycopg2 # biblioteka do polaczenia z psql
from psycopg2 import Error # biblioteka do obslugi bledow w psql

GPIO.setwarnings(False)

# deklarowanie numerów pin

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(10, GPIO.OUT, initial = GPIO.LOW)

reader = SimpleMFRC522() # deklaracja modulu do sensora RFID

try:

	# Połączenie do istniejacej bazy danych
	connection = psycopg2.connect(user="admin",
								  password="Stronk2k3",
								  host="127.0.0.1",
								  port="5432",
								  database="rfid_logs")

	# Testowanie polaczenia do bazy danych
	cursor = connection.cursor()

	rfid, text =  reader.read() # czytanie z sensora RFID

	if(id == 876685318415): # jezeli ID karty wynosi tyle co podane, to zapal zielona diode LED
		GPIO.output(8, GPIO.HIGH)
		print("Witaj ", text,  "! Masz uprawnienia na wejscie do serwerowni")

		# dodawanie logu do pliku

		username = text
		time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
		status = 'AUTORYZOWANE'

		# Dodawanie wpisu do bazy danych z logami

		cursor.execute("INSERT INTO rfid_login (ID, USERNAME, RFID, TIME, STATUS) VALUES (DEFAULT, %s, %s, %s, %s)", (username, rfid, time, status))

		connection.commit()
		print("Rekord dodany pomyslenie")
		# Fetch result
		cursor.execute("SELECT * from rfid_logs")
		record = cursor.fetchall()
		print("Rekord: ", record)

		sleep(1)
	else:
		GPIO.output(10, GPIO.HIGH) # jezeli nie, to zapal czerwona diode LED
		print("Niestety nie masz uprawnien na wejscie do serwerowni!!! Skontaktuj się z Administratorem")

		# dodawanie logu do pliku:

		username = text
		time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
		status = 'NIEAUTORYZOWANE'

		cursor.execute("INSERT INTO rfid_login (ID, USERNAME, RFID, TIME, STATUS) VALUES (DEFAULT, %s, %s, %s, %s)", (username, rfid, time, status))

		connection.commit()
		print("Rekord dodany pomyslenie")
		# Fetch result
		cursor.execute("SELECT * from rfid_logs")
		record = cursor.fetchall()
		print("Rekord: ", record)

		sleep(1)

except (Exception, Error) as error:
    print("Wystapil blad w trakcie polaczenia z bazą PostgreSQL", error)

finally:

	GPIO.cleanup()
	if (connection):
		cursor.close()
		connection.close()
		print("Polaczenie z baza PostgreSQL zostalo zamkniete")

# poprawki
