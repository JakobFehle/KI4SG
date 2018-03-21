#!/usr/bin/python2.7

import mysql;
import mysql.connector;

#Verbindung erstellen
try:
    connection = mysql.connector.connect(host = "localhost", user = "user", passwd = "Passwort", db = "Datenbank1")
except:
    print "Keine Verbindung zum Server"
    exit(0)

#Tabelle erzeugen
cursor = connection.cursor()
cursor.execute("CREATE TABLE test (id int(1), text varchar(255))")
cursor.close()

#Datensatz einfuegen
cursor = connection.cursor()
cursor.execute("INSERT INTO test (id,text) VALUES (%s,%s)",("1","Hallo Welt",))
cursor.execute("INSERT INTO test (id,text) VALUES (%s,%s)",("2","Hallo Welt",))
cursor.execute("INSERT INTO test (id,text) VALUES (%s,%s)",("3","Hallo Welt",))
cursor.close();
connection.commit()

#Datensaetze auslesen
cursor = connection.cursor()
cursor.execute("SELECT * from test")
result = cursor.fetchall()
cursor.close()

for data in result:
    print "Nummer: " + str(data[0]) + "; Text: " + data[1]