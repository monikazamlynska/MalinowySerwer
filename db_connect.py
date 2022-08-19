# author: Monika Zamlynska
# e-mail: monika.zamlynska@gmail.com
# 2022-08-18

#!/usr/bin/env python

import psycopg2 # biblioteka do polaczenia z psql
from psycopg2 import Error # biblioteka do obslugi bledow w psql

try:
    # Połączenie do istniejacej bazy danych
    connection = psycopg2.connect(user="admin",
                                  password="Stronk2k3",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="rfid_logs")

    # Testowanie polaczenia do bazy danych
    cursor = connection.cursor()

    # Wyswietlanie infomacji związanych z baza danych
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")

    # Wykonywanie jakiegos zapytania SQL (sprawdzenie wersji bazy)
    cursor.execute("SELECT version();")

    # Pobieranie wyniku
    record = cursor.fetchone()
    print("Jestes polaczony z - ", record, "\n")

# obługa wyjatku i bledow
except (Exception, Error) as error:
    print("Wystapil blad w trakcie polaczenia z bazą PostgreSQL", error)

finally:
    if (connection):
        cursor.close()
        connection.close()
        print("Polaczenie z baza PostgreSQL zostalo zamkniete")

