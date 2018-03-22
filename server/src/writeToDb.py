#!/usr/bin/python2.7
import json
import io
import mysql
import mysql.connector
from findnutr import *
#Verbindung erstellen



def createTable():
    try:
        connection = mysql.connector.connect(host="localhost", user="root", passwd="asdfgh", db="newschema")
        print "Connection established!"
        try:
            cursor = connection.cursor()
            cursor.execute(
                "CREATE TABLE RecipeNuts (RezeptID varchar(255), Kcal varchar(255),Eiweis varchar(255), Kohlenhydrate varchar(255), Fett varchar(255), Calcium varchar(255), Kalium varchar(255), Eisen varchar(255), Zink varchar(255), Magnesium varchar(255), Ballaststoffe varchar(255), Linolsaeure varchar(255), Linolensaeure varchar(255), Iodid varchar (255), VitaminA varchar(255), VitaminC varchar(255), VitaminE varchar(255), VitaminB1 varchar(255), VitaminB2 varchar(255), VitaminB6 varchar(255), VitaminB12 varchar(255) )")
            cursor.close()
            print "Database sucessfully created!"
        except:
            print "Database already created!"
            cursor.close()
            #Shouldnt we exit now?
            exit(127)
    except:
        print "Couldnt connect to database"
        exit(0)

    return;


def writeNuts(recipe_href,kcal,eiweis,kohlenhydrate,fat,calcium,kalium,eisen,zink,magnesium,ballaststoffe,linolsaeure, linolensaeure,iodid,va,vc,ve,vb1,vb2,vb6,vb12):
    """try:
        connection = mysql.connector.connect(host="localhost", user="root", passwd="asdfgh", db="kochbar")
        print "Connection established!"
    except:
        print "Couldnt connect to database"
        exit(0)"""
    # Exception Handling remove for the sake of perfomance...

    connection = mysql.connector.connect(host="localhost", user="root", passwd="asdfgh", db="newschema")

 #Datensatz einfuegen
    cursor = connection.cursor()
    cursor.execute("INSERT INTO recipenuts (RezeptID,Kcal,Eiweis,Kohlenhydrate,Fett,Calcium,Kalium,Eisen,Zink,Magnesium,Ballaststoffe,Linolsaeure,Linolensaeure,Iodid,VitaminA,VitaminC,VitaminE,VitaminB1,VitaminB2,VitaminB6,VitaminB12) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(recipe_href,kcal,eiweis,kohlenhydrate,fat,calcium,kalium,eisen,zink,magnesium,ballaststoffe,linolsaeure, linolensaeure,iodid,va,vc,ve,vb1,vb2,vb6,vb12,))
    cursor.close();
    connection.commit()

#Datensaetze auslesen
#Removed for the sake of perfomance..
    """
    cursor = connection.cursor()
    cursor.execute("SELECT * from RecipeNuts")
    result = cursor.fetchall()
    cursor.close()

    for data in result:
        print "RezeptID: " + str(data[0]) + "; KCAL: " + data[1]+ ",Eiweis: " +data[2]"""

    return;






# Try to create the nuts table
#createTable()

# Example of calling writeNuts, writing a recipe nutrition set to the previously made table
writeNuts("/rezept/501707/Gefuellte-Zucchini-und-Paprika.html","1018.48","6029.25","11432.25","68.37","593.45","1311.09","6029.25","7639.2","139.6","3637.4","2679.93","766.98","164.625","621.76","38200.0","3194.5","2601.75","1578.35","1643.75","4.8")