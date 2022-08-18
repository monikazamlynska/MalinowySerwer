
import time # biblioteka dla czasu
import board # bibilioteka do importu pinów z board'a
import adafruit_dht # biblioteka sensora DHT

dhtDevice = adafruit_dht.DHT11(board.D17) # czytanie z sensora DHT na pinie 17

while True:
	try: # wyjatek
		temperature_c = dhtDevice.temperature # wyciagnij temperature z sensora DHT
		humidity = dhtDevice.humidity # wyciagnij cisnienie z sensora DHT

		print("Temperature: {:.1f}*C    Humidity: {}% ".format(temperature_c, humidity)) # wypisz na ekran
	
	except RuntimeError as error: # obsluga bledow Runtime
		print(error.args[0]) # wyswietl blad
		time.sleep(2.0) # timer
		continue
	except Exception as error:  # obsluga bledow 
		dhtDevice.exit() 
		raise error

	time.sleep(2.0)

