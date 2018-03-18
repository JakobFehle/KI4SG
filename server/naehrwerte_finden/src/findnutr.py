# encoding=utf8
from __future__ import division
import codecs
import MySQLdb
import sys
import re
import json
import io
from glob import glob
from operator import itemgetter

from readconfig import *

rezeptJson = r'''{
            "recipe_href" : "/rezept/501707/Gefuellte-Zucchini-und-Paprika.html",
            "title" : "Gefüllte Zucchini und Paprika",
            "description" : "die letzte Zucchini aus eigener Ernte",
            "ratings" : 21,
            "average_rating" : 5,
            "numstars" : 5,
            "comments" : 8,
            "favorites" : 2,
            "views" : 204,
            "servings" : 2,
            "ingredients_string" : "1:Zucchini \n 2:Paprika rot \n 200 g:Feta \n 250 g:Schinken \n optional für die Soße \n 1:Zwiebel frisch \n 300 g:Passierte Tomaten \n :Pfeffer \n :Salz \n :Majoran getrocknet",
            "preparation_instructions" : "Anmerkung: Es war die letzte Zucchini aus eigener Ernte in diesem Jahr und darum habe ich noch eine Paprika gefüllt. \n Die Zucchini (meine war etwa 25 cm lang) und Paprika waschen und halbieren. Zucchini mit einem Löffel auskratzen, das Fruchtfleisch kann man für die Soße verwenden. Von den Paprikas die Kerne und entfernen. Paprika fein würfeln. \n Den Feta, eine Paprika und auch den Schinken fein würfeln (oder gleich fein gewürfelten Schinken verwenden). Alle Würfelchen gut miteinander vermischen \n Zucchini und die 2 halben Paprika in die leicht gefettete Auflaufform setzen und mit der vorbereiteten Füllung füllen. \n Wer dazu eine Soße mag: Das Fruchtfleisch der Zucchini und eine Zwiebel klein schneiden, passierte Tomaten zufügen umrühren und nach persönlichem Geschmack würzen. Die Soße dann  in die Auflaufform geben und die Zucchini und Paprika dort hinein setzen. \n Im vorgeheizten Backofen etwa 20 min. bei 180°C backen",
            "difficulty" : "leicht",
            "duration" : 30,
            "price" : "1",
            "kj" : 447,
            "kcal" : 107,
            "protein" : 10.9,
            "carbohydrates" : 1.3,
            "fat" : 6.6,
            "date" : "2014-11-19",
            "num_ingredients" : 9,
            "class_sweet" : 0
        }'''

class DatenBank:
# Diese Klasse bildet ein Interface zu den verwendeten Datenbank-Tabellen. Ein Objekt der Klasse wird global instanziiert, sodass alle Klassen darauf zugreifen können.

	def __verbindeDB(self):
		self.DBConnection = MySQLdb.connect(self.__Database_Host, self.__Database_User, self.__Database_Password, self.__Database_DatabaseName,use_unicode=True)
		self.DBCursor = self.DBConnection.cursor()
		self.DBCursorDict = self.DBConnection.cursor(MySQLdb.cursors.DictCursor)
	def __schliesseDB(self):
		self.DBCursor.close()
		self.DBCursorDict.close()
		self.DBConnection.close()
	def __init__(self):
		self.__Database_Host=configuration.getAttribute('Database_Host') # Die Adresse des Datenbank-Servers, zum Beispiel "localhost".
		self.__Database_User=configuration.getAttribute('Database_User') # Der Benutzername für den Zugang zur Datenbank.
		self.__Database_Password=configuration.getAttribute('Database_Password') # Das Passwort für den Zugang zur Datenbank.
		self.__Database_DatabaseName=configuration.getAttribute('Database_DatabaseName') # Der Name der verwendeten Datenbank.

		self.IngredientsTable=configuration.getAttribute('IngredientsTable') # Der Name der Nährwert-Tabelle.
		self.IngredientsRulesTable=configuration.getAttribute('IngredientsRulesTable') # Der Name Tabelle für die Bezeichnungs-Regeln.
		self.QuantityRulesTable=configuration.getAttribute('QuantityRulesTable') # Der Name Tabelle für die Mengen-Regeln.

		self.DBCursor=''
		self.DBConnection=''


		self.__verbindeDB()
	def __del__(self):
		self.__schliesseDB()


class Zutat:
# Instanzen dieser Klasse stellen einen Eintrag aus der Nährwerttabelle dar, welcher aus einer Beschreibung (zum Beispiel "Hühnerei roh") und Nährwertangaben besteht.
# Für jede Instanz kann eine Eignung bestimmt werden, die angibt, wie gut der Eintrag aus der Nährwerttabelle zum Rezepteintrag passt.
# Objekte dieser Klasse werden ausschließlich von der Klasse "Rezepteintrag" benötigt, ansonsten ist es nicht sinnvoll, die Klasse "Zutat" zu instanziieren oder deren Funktionen aufzurufen.


	def __init__(self,bezeichnung,inhaltsstoffid,naehrwer):
	# Instanziiert wird die Klasse unter Angabe der Beschreibung aus der Nährwertdatenbank (zum Beispiel "Hühnerei roh"),
	# der ID des Eintrags im Bundeslebensmittelschlüssel und der Nährwerte, die im Bundeslebensmittelschlüssel angegeben sind.


		self.name = '' # Die Beschreibung des Eintrags aus der Nährwerttabelle, beispielsweise "Hühnerei roh".
		self.id = '' #  Die ID des jeweiligen Eintrags des Bundeslebensmittelschlüssels.
		self.__suchName = '' # Vorverarbeitete Beschreibung.
		self.qualitaet = 100.0 # Die berechnete Eignung des Eintrages der Nährwerttabelle zum Rezepteintrag.
		self.naehrwerte=naehrwer # Die Nährwerte des Eintrags, wie sie im Bundeslebensmittelschlüssel angegeben sind.

		self.id = inhaltsstoffid
		self.name = bezeichnung

		self.__suchName = self.name.lower()
		self.__suchName=self.__suchName.replace("&auml;",u"ä")
		self.__suchName=self.__suchName.replace("&szlig;",u"ß")
		self.__suchName=self.__suchName.replace("&uuml;",u"ü")
		self.__suchName=self.__suchName.replace("&ouml;",u"ö")
		self.__suchName=self.__suchName.replace("&auml;",u"Ä")
		self.__suchName=self.__suchName.replace("&uuml;",u"Ü")
		self.__suchName=self.__suchName.replace("&ouml;",u"Ö")


		self.__suchName=self.__suchName.replace("(n)","")
		self.__suchName=self.__suchName.replace("(e)","")
		self.__suchName=self.__suchName.replace("(s)","")
		self.__suchName=self.__suchName.replace("(er)","")

		#self.__suchName = re.sub('\(.*\)', " ", self.__suchName)
		self.__suchName=self.__suchName.replace("(","")
		self.__suchName=self.__suchName.replace(")","")
		self.__suchName=re.sub(u'[^A-Za-z0-9üöäÜÄÖéèáàíìêîôúùûß ]',' ',self.__suchName)

	def feature(self, featureid, bezeichnung):
	# Für das Ranking berechnet diese Funktion eine Komponente des Merkmalsvektors zu einer bestimmten Beschreibung aus der Zutatenliste.
	# Die Nummer der Komponente kann durch die "featureid" übergeben werden. Ein möglicher Aufruf ist also feature(1, 'Eier frisch').


		# Komponente nicht sinnvoll!
		#if (featureid==15):
		#	fn=0
		#	for zutatenteil in bezeichnung.split():
		#		if regeln.stopword(zutatenteil)==False and len(zutatenteil)>1:
		#			if (zutatenteil.lower() in self.__suchName.lower()) and (zutatenteil[1].lower()!=zutatenteil[1]):
		#				fn=fn+1
		#	return fn

		bezeichnung=bezeichnung.lower()
		if (featureid==1):
			if (self.__suchName.replace(' ','')==bezeichnung.replace(' ','')):
				return 1
			else:
				return 0
		if (featureid==2):
			if (self.__suchName.replace(' ','')==regeln.stemsentence(bezeichnung).replace(' ','')):
				return 1
			else:
				return 0
		if (featureid==3):
			if (self.__suchName.split()[0]==bezeichnung.split()[0]):
				return 1
			else:
				return 0
		if (featureid==4):
			fn=0
			for zutatenteil in bezeichnung.split():
				if regeln.stopword(zutatenteil)==False and len(zutatenteil)>2:
					if (zutatenteil in self.__suchName.lower().split()):
						fn=fn+1
			return fn
		if (featureid==5):
			fn=0
			for zutatenteil in bezeichnung.split():
				if regeln.stopword(zutatenteil)==False and len(zutatenteil)>2:
					if not(zutatenteil in self.__suchName.lower().split()) and (zutatenteil in self.__suchName.lower()):
						fn=fn+1
			return fn
		if (featureid==6):
			fn=0
			for zutatenteil in self.__suchName.lower().split():
				if regeln.stopword(zutatenteil)==False and len(zutatenteil)>2:
					if not(zutatenteil in bezeichnung.split()) and (zutatenteil in bezeichnung):
						fn=fn+1
			return fn
		if (featureid==7):
			fn=0
			for zutatenteil in bezeichnung.split():
				if regeln.stopword(zutatenteil)==False and len(zutatenteil)==2:
					if (zutatenteil in self.__suchName.lower().split()):
						fn=fn+1
			return fn
		if (featureid==8):
			fn=0
			for zutatenteil in bezeichnung.split():
				if regeln.stopword(zutatenteil)==False and len(zutatenteil)==2:
					if not(zutatenteil in self.__suchName.lower().split()) and (zutatenteil in self.__suchName.lower()):
						fn=fn+1
			return fn
		if (featureid==9):
			fn=0
			for zutatenteil in self.__suchName.lower().split():
				if regeln.stopword(zutatenteil)==False and len(zutatenteil)==2:
					if not(zutatenteil in bezeichnung.split()) and (zutatenteil in bezeichnung):
						fn=fn+1
			return fn
		if (featureid==10):
			return len(self.name)

		if (featureid==11):
			# from http://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Longest_common_substring#Python
			S1=self.__suchName.lower()
			S2=bezeichnung
			M = [[0]*(1+len(S2)) for i in xrange(1+len(S1))]
			longest, x_longest = 0, 0
			for x in xrange(1,1+len(S1)):
				for y in xrange(1,1+len(S2)):
					if S1[x-1] == S2[y-1]:
						M[x][y] = M[x-1][y-1] + 1
						if M[x][y]>longest:
							longest = M[x][y]
							x_longest  = x
					else:
						M[x][y] = 0
			return len(S1[x_longest-longest: x_longest])

		if (featureid==12):
			bezeichnung=bezeichnung.replace("(n)","")
			bezeichnung=bezeichnung.replace("(s)","")
			bezeichnung=bezeichnung.replace("(er)","")
			bezeichnung=bezeichnung.replace("(e)","")

			klammerl=bezeichnung.find('(')
			klammerr=bezeichnung.find(')')
			if klammerl>=0 and klammerr>0 and klammerl+1<klammerr:
				wortzwischenklammern=bezeichnung[klammerl+1:klammerr]
				if wortzwischenklammern in self.__suchName.lower():
					return 1
				else:
					return 0
			else:
				return 0
		if (featureid==13):
			for zutatenteil in bezeichnung.split():
				if regeln.stopword(zutatenteil)==False and len(zutatenteil)>2:
					if (("ge" in zutatenteil) or ("ver" in zutatenteil) or ("zer" in zutatenteil) or ("be" in zutatenteil)) and (zutatenteil[-4:]=="ener" or zutatenteil[-4:]=="enes" or zutatenteil[-3:]=="ene" or zutatenteil[-2:]=="en" or zutatenteil[-1]=="t"):
						if zutatenteil in self.__suchName.lower():
							return 1
			return 0
		if (featureid==14):
			partper=False
			for zutatenteil in bezeichnung.split():
				if regeln.stopword(zutatenteil)==False and len(zutatenteil)>2:
					if (("ge" in zutatenteil) or ("ver" in zutatenteil) or ("zer" in zutatenteil) or ("be" in zutatenteil)) and (zutatenteil[-4:]=="ener" or zutatenteil[-4:]=="enes" or zutatenteil[-3:]=="ene" or zutatenteil[-2:]=="en" or zutatenteil[-1]=="t"):
						partper=True
			if not(partper) and ("roh" in self.__suchName.lower().split()):
				return 1
			else:
				return 0

	def bewertefeature(self, bezeichnungvorverarbeitet, bezeichnung):
	# Diese Funktion wird von der Klasse "Rezepteintrag" aufgerufen, um die verschiedenen Komponenten der Merkmalsvektoren zu berechnen und zu gewichten.
	# Übergeben wird dabei die Zutaten-Beschreibung aus der Zutaten-Liste des Rezeptes, sowohl verarbeitet als auch unangetastet.


		#gewicht_f3=-0.0528
		#gewicht_f4=0.0
		#gewicht_f5=0.0
		#gewicht_f6=0.2203
		#gewicht_f7=0.1081
		#gewicht_f8=0.2443
		#gewicht_f9=0.0
		#gewicht_f10=-0.0177
		#gewicht_f11=0.0288
		#gewicht_f12=0.1907
		#gewicht_f13=0.3018
		#gewicht_f14=0.2168

		#gewicht_f3=1.0
		#gewicht_f4=1.0
		#gewicht_f5=1.0
		#gewicht_f6=1.0
		#gewicht_f7=1.0
		#gewicht_f8=1.0
		#gewicht_f9=1.0
		#gewicht_f10=-1.0
		#gewicht_f11=1.0
		#gewicht_f12=1.0
		#gewicht_f13=1.0
		#gewicht_f14=1.0

		#gewicht_f3=-0.2334
		#gewicht_f4=0.0
		#gewicht_f5=0.0
		#gewicht_f6=1.19246
		#gewicht_f7=0.0
		#gewicht_f8=1.14236
		#gewicht_f9=0.0
		#gewicht_f10=-0.118
		#gewicht_f11=0.19466
		#gewicht_f12=0.0
		#gewicht_f13=0.8321
		#gewicht_f14=0.8823


		gewicht_f3=0.0
		gewicht_f4=0.20472
		gewicht_f5=0.0
		gewicht_f6=0.40135
		gewicht_f7=0.0
		gewicht_f8=0.31531
		gewicht_f9=0.0
		gewicht_f10=-0.12158
		gewicht_f11=0.19197
		gewicht_f12=0.06512
		gewicht_f13=0.0
		gewicht_f14=0.22208

		if (self.feature(1,bezeichnungvorverarbeitet)==1): #exact match
			self.qualitaet=99999.0
		elif (self.feature(2,bezeichnungvorverarbeitet)==1): #exact stemmed match
			self.qualitaet=99999.0
		else:
			self.qualitaet=0.89175046+gewicht_f3*self.feature(3,bezeichnungvorverarbeitet)+gewicht_f4*self.feature(4,bezeichnungvorverarbeitet)+gewicht_f5*self.feature(5,bezeichnungvorverarbeitet)+gewicht_f6*self.feature(6,bezeichnungvorverarbeitet)+gewicht_f7*self.feature(7,bezeichnungvorverarbeitet)+gewicht_f8*self.feature(8,bezeichnungvorverarbeitet)+gewicht_f9*self.feature(9,bezeichnungvorverarbeitet)+gewicht_f10*self.feature(10,bezeichnungvorverarbeitet)+gewicht_f11*self.feature(11,bezeichnungvorverarbeitet)+gewicht_f12*self.feature(12,bezeichnung)+gewicht_f13*self.feature(13,bezeichnungvorverarbeitet)+gewicht_f14*self.feature(14,bezeichnungvorverarbeitet)



	def bewerte(self,bezeichnung):
	# Obsolete Funktion zum Ranking. Wurde durch "bewertefeature" ersetzt.


		#bezeichnung=re.sub(u'[^A-Za-z0-9üöäÜÖÄß ]',' ',bezeichnung)

		self.qualitaet = 100.0
		bezeichnung=bezeichnung.lower()
		#print "BEZ: "+bezeichnung.encode("iso-8859-1")+" BEZ: "+self.__suchName.encode("iso-8859-1")
		#print self.name.encode("iso-8859-1")+":"
		#print regeln.stemsentence(self.__suchName).replace(' ','').encode("iso-8859-1")+" = "+regeln.stemsentence(bezeichnung).replace(' ','').encode("iso-8859-1")
		if (self.__suchName.replace(' ','')==bezeichnung.replace(' ','')):
			self.qualitaet=self.qualitaet+200.0
		elif (self.__suchName.replace(' ','')==regeln.stemsentence(bezeichnung).replace(' ','')):
			self.qualitaet=self.qualitaet+200.0
		if (self.__suchName.split()[0]==bezeichnung.split()[0]):
			self.qualitaet=self.qualitaet+10.0
		for zutatenteil in bezeichnung.split():
			if regeln.stopword(zutatenteil)==False and len(zutatenteil)>2:
				if (zutatenteil in self.__suchName.lower().split()):
					self.qualitaet=self.qualitaet+10.0
				elif (zutatenteil in self.__suchName.lower()):
					self.qualitaet=self.qualitaet+6.0
		for zutatenteil in self.__suchName.lower().split():
			if regeln.stopword(zutatenteil)==False and len(zutatenteil)>2:
				if not(zutatenteil in bezeichnung.split()) and (zutatenteil in bezeichnung):
					self.qualitaet=self.qualitaet+6.0

		self.qualitaet=self.qualitaet-len(self.name)*0.5


	def anzeigen(self):
	# Zur Ausgabe der ermittelten Informationen.
		print "Bezeichnung: "+self.name.encode("iso-8859-1")


class Rezepteintrag:
# Jede Instanz dieser Klasse verkörpert einen Eintrag der Zutaten-Liste, bestehend aus Bezeichnung (zum Beispiel "Salz", "Mehl"),
# Mengeneinheit (zum Beispiel "Gramm", "Liter") und Mengenquantum (zum Beispiel "3", "5").
# Die Klasse speichert alle Einträge aus der Nährwertdatenbank, die für eine Zuordnung in Frage kommen, als Instanzen der Klasse "Zutat".
# Zu jedem Eintrag der Nährwerttabelle wird die Eignung der Zuordnung bestimmt, um den am besten passenden Eintrag auswählen zu können.
# Danach wird versucht, die Masse des Rezepteintrags in Gramm zu bestimmen.


	def __init__(self, menge, mengeneinheit, bezeichnung):
	# Instanziiert wird ein Objekt der Klasse, indem Mengenquantum, Mengeneinheit und Zutaten-Beschreibung aus der Zutaten-Liste übergeben werden.
	# Ein möglicher Aufruf wäre also: Rezeipteintrag('3', 'Stück', 'Ei(er), frisch').


		self.bezeichnung = '' # Der Wortlaut, mit dem die Zutat in der Zutatenliste des Rezeptes umschrieben wird, zum Beispiel "Ei(er), frisch".
		self.menge = '' # Das Quantum der in der Zutatenliste umschriebenen Menge, bei der Zutat "3 Stück Ei(er), frisch" ist dies zum Beispiel "3".
		self.mengeneinheit = '' # Die Einheit der Menge aus der Zutatenliste, beispielsweise "Stück", "Gramm" oder "Liter".
		self.__gefundeneZutaten = [] # Alle Einträge aus der Nährwertdatenbank, die für eine Zuordnung in Frage kommen.
		self.mengeInG = -1 # Die unter Berücksichtigung des Mengenquantums, der Mengeneinheit und der am besten passenden Zutat aus der Nährwerttabelle berechnete Masse des Rezepteintrags in der Einheit Gramm.


		self.suchNach = '' # Vorverarbeitete, durch Bezeichnungsregeln angepasste Zutatenbeschreibung
		self.suchNachVorUmschreiben='' # Vorverarbeitete Zutatenbeschreibung

		self.besteZutat = '' # Die Zutat aus der Nährwerttabelle, die sich im Ranking als am besten geeignet herausgestellt hat, um die Beschreibung aus der Zutaten-Liste zu repräsentieren. Bei der Zutat "3 Stück Ei(er), frisch" wäre dies beispielsweise "Hühnerei roh".
		self.zweitbesteZutat = '' # Die Zutat aus der Nährwerttabelle, die sich im Ranking als am zweitbesten geeignet herausgestellt hat.



		self.bezeichnung = bezeichnung.replace('&nbsp;',' ')
		self.menge = menge.replace('&nbsp;',' ')
		self.mengeneinheit = mengeneinheit.replace('&nbsp;',' ')


		self.bezeichnung=self.bezeichnung.replace("&auml;",u"ä")
		self.bezeichnung=self.bezeichnung.replace("&szlig;",u"ß")
		self.bezeichnung=self.bezeichnung.replace("&uuml;",u"ü")
		self.bezeichnung=self.bezeichnung.replace("&ouml;",u"ö")
		self.bezeichnung=self.bezeichnung.replace("&Auml;",u"Ä")
		self.bezeichnung=self.bezeichnung.replace("&Uuml;",u"Ü")
		self.bezeichnung=self.bezeichnung.replace("&Ouml;",u"Ö")

		self.suchNach = self.bezeichnung

		self.suchNach =self.suchNach.replace("(n)","")
		self.suchNach =self.suchNach.replace("(e)","")
		self.suchNach =self.suchNach.replace("(s)","")
		self.suchNach =self.suchNach.replace("(er)","")
		self.suchNach=self.suchNach.replace("(","")
		self.suchNach=self.suchNach.replace(")","")
		#self.suchNach = re.sub('\(.*\)', " ", self.suchNach)

		self.suchNach=re.sub(u'[^A-Za-z0-9üöäÜÖÄéèáàíìêîôúùûß ]',' ',self.suchNach)


		self.suchNach=self.suchNach.strip()

		self.suchNachVorUmschreiben=self.suchNach


		self.suchNach=regeln.bezeichnungumschreiben(self.suchNach)

		#print "'"+self.suchNach+"'"
		#if (len(sys.argv)<=1) or (sys.argv[1]!='errors'):
		self.__findeZutaten()
		self.__bewerteZutaten()
		self.__findeMengeInG()

		self.zutatenGruppe=''
		if self.besteZutat!='':
			zutatenGruppenListe={'B':u'brot','F':u'obst','G':u'gemüse','R':u'gewürze','T':u'fisch','U':u'fleisch','V':u'fleisch','W':u'fleisch'}
			zutGruppe=self.besteZutat.id[0]
			if zutGruppe in zutatenGruppenListe:
				self.zutatenGruppe=zutatenGruppenListe[zutGruppe]



	def anzeigen(self):
	# Zur Ausgabe der ermittelten Informationen.

		print "Zutat:"
		if (self.mengeneinheit==''):
			print "Menge: "+self.menge.encode("iso-8859-1")+", Bezeichnung: "+self.bezeichnung.encode("iso-8859-1")
		else:
			print "Menge: "+self.menge.encode("iso-8859-1")+" Einheit: " +self.mengeneinheit.encode("iso-8859-1")+ ", Bezeichnung: "+self.bezeichnung.encode("iso-8859-1")

		print "Bester Eintrag aus der Naehrwerttabelle: "
		if self.besteZutat!="":
			self.besteZutat.anzeigen()
		else:
			print "nichts gefunden"
		print "Menge: "+str(self.mengeInG)+" g "

		print ""

	def __findeMengeInG(self):
	# Bestimmung der Masse des Rezepteintrags in der Einheit Gramm.

		umrechnungsverhaeltnis = 0.0
		if self.besteZutat!="":
			umrechnungsverhaeltnis = regeln.umrechnungsverhaeltnis(self.mengeneinheit,self.besteZutat.name)


		# Mengen fuer 1/2, 1/4 umschreiben
		mengedazu=0.0
		diemenge=self.menge
		if diemenge.find('&#189;')>=0:
			diemenge=diemenge.replace('&#189;','')
			mengedazu=mengedazu+0.5
		if diemenge.find('&#188;')>=0:
			diemenge=diemenge.replace('&#188;','')
			mengedazu=mengedazu+0.25
		if diemenge.find('&#190;')>=0:
			diemenge=diemenge.replace('&#190;','')
			mengedazu=mengedazu+0.75
		if diemenge.find('&#8539;')>=0:
			diemenge=diemenge.replace('&#8539;','')
			mengedazu=mengedazu+0.125
		diemenge=diemenge.replace(",",".")

		try:
			if umrechnungsverhaeltnis<0:
				self.mengeInG = -umrechnungsverhaeltnis
			else:
				self.mengeInG = umrechnungsverhaeltnis * (float(diemenge.strip())+mengedazu)
		except ValueError:
			self.mengeInG = mengedazu*umrechnungsverhaeltnis

		if (self.mengeInG==0.0) and (umrechnungsverhaeltnis>0.0):
			self.mengeInG = umrechnungsverhaeltnis


	def getPreprocessed(self):
		return self.suchNach.lower()

	def getFirstword(self):
		lookfor = self.suchNach
		if (lookfor.find(' ')>=0):
			lookfor=lookfor[:lookfor.find(' ')]
		return lookfor.lower()

	def getStemmedfirstword(self):
		return regeln.stemword(self.getFirstword())



	def __findeZutaten(self):
	# Ermittlung alle Einträge aus der Nährwertdatenbank, die für eine Zuordnung in Frage kommen.

		lookfor = self.suchNach

		if (lookfor.find(' ')>=0):
			lookfor=lookfor[:lookfor.find(' ')]

		lookforstemmed=regeln.stemword(lookfor)

		SQLRequest="SELECT * FROM %s WHERE LOWER(ST) LIKE LOWER('%s') OR LOWER(ST) LIKE LOWER('%s')"% (datenbank.IngredientsTable,('%%%s%%' % lookfor),('%%%s%%' % lookforstemmed))
		#print SQLRequest
		datenbank.DBCursorDict.execute(SQLRequest)
		for gefundeneZutat in datenbank.DBCursorDict.fetchall():

			#for key, value in gefundeneZutat.iteritems():
			#print gefundeneZutat
			zutatenname=gefundeneZutat["ST"]
			inhaltsstoffid=gefundeneZutat["SBLS"]
			del gefundeneZutat["SBLS"]
			del gefundeneZutat["ST"]

			del gefundeneZutat["id"]
			self.__gefundeneZutaten.append(Zutat(zutatenname,inhaltsstoffid,gefundeneZutat))

	def __bewerteZutaten(self):
	# Bewertung alle Einträge aus der Nährwertdatenbank, die für eine Zuordnung in Frage kommen.

		qualitaet=-99999.0
		for gefundenes in self.__gefundeneZutaten:
			gefundenes.bewertefeature(self.suchNach, self.bezeichnung)
			if gefundenes.qualitaet>qualitaet:
				qualitaet=gefundenes.qualitaet
				self.zweitbesteZutat=self.besteZutat
				self.besteZutat=gefundenes


class Rezept:
# Eine Instanz der Klasse "Rezept" repräsentiert ein Rezept der verwendeten Rezept-Seite "chefkoch.de".
# Im HTML-Format vorliegende Rezepte können geparst werden.
# Gespeichert werden URL des Chefkoch-Rezeptes, Titel, Zubereitungs-Beschreibung und eine Liste aller Zutaten,
# jeweils bestehend aus einer Mengeneinheit (zum Beispiel "Gramm"; "Liter"), einem Mengenquantum (zum Beispiel "3"; "5") und einer Bezeichnung (zum Beispiel "Zucker"; "Ei(er), möglichst frisch").
# Die Klasse liefert dann die Gesamtmasse aller im Rezept enthaltenen Zutaten, die enthaltenen Nährwerte aller Zutaten werden aufaddiert und sind ebenfalls abrufbar.


	def zutatenanzeigen(self):
	# Diese Funktion kann zur Ausgabe der ermittelten Informationen verwendet werden.

		print "URL: "+ self.url.encode("iso-8859-1")
		print "Titel: "+ self.titel.encode("iso-8859-1")
		print '---'
		for zutat in self.zutaten:
			zutat.anzeigen()

		print "\n\n\nNaehrwerte im Rezept:\n"

		for key in self.naehrwerte:
			print key +": "+str(self.naehrwerte[key])+", ",


	def __init__(self, dateiname):
	# Zum Instanziieren eines Objektes wird dieser Funktion Pfad und Dateiname eines Rezeptes im HTML-Format übergeben. Alle Informationen werden dann automatisch ermittelt.

		self.text = '' # Der Quelltext des Rezeptes im HTML-Format.
		self.zutaten = [] # Eine Liste aller im Rezept enthaltenen Zutaten. Jede Zutat ist dabei eine Instanz der Klasse "Rezepteintrag".
		self.url= '' # Die URL des Rezeptes.
		self.beschreibung = '' # Die Zubereitungs-Beschreibung des Rezeptes.
		self.titel = '' # Der Titel des Rezeptes.

		self.menge = 0.0 # Die Gesamtmasse des Rezeptes, also die Summe der Masse aller enthaltenen Zutaten.
		self.portionsgroese = -1 # Anzahl der Portionen, zum Beispiel "4"

		self.naehrwerte = {} # Eine Liste aller im Rezept enthaltenen Nährwerte. Enthaltene Kilokalorien sind beispielsweise über den Wert "naehrwerte['GCAL']" abrufbar, enthaltene Proteine in Milligramm über den Wert "naehrwerte['ZE']". Die Abkürzungen und Einheiten der verschiedenen Nährwerte können dem Handbuch des Bundeslebensmittelschlüssels (Seite 24-28) entnommen werden.
		self.naehrwertepro100g = {} # Eine Liste aller im Rezept enthaltenen Nährwerte pro 100g.

		self.__rezeptDateiLesen(dateiname)
		self.__zutatenFinden()

		for zutat in self.zutaten:
			if zutat.besteZutat!='' and zutat.mengeInG>0.0:
				self.menge=self.menge+zutat.mengeInG
				for key in zutat.besteZutat.naehrwerte:
					#zutat.besteZutat.naehrwerte[key]
					if key in self.naehrwerte:
						self.naehrwerte[key]=self.naehrwerte[key]+(float(zutat.besteZutat.naehrwerte[key])*zutat.mengeInG)
					else:
						self.naehrwerte[key]=float(zutat.besteZutat.naehrwerte[key])*zutat.mengeInG

		for key in self.naehrwerte:
			self.naehrwerte[key]=self.naehrwerte[key]/100.0


		# Pro 100g
		if (self.menge>0.0):
			for key in self.naehrwerte:
				self.naehrwertepro100g[key]=float(self.naehrwerte[key])*100.0/self.menge

	def __rezeptDateiLesen(self,dateiname):
	# Einlesen der Rezeptdatei

		datei = codecs.open(dateiname, "r", "utf-8")
		#datei = open(dateiname,'r')
		self.text = datei.read()
		datei.close()

	def __zutatenFinden(self):
	# Parsen der Rezeptdatei

		if (self.text.find('h1 class="big"')>=0):
			self.titel = self.text[self.text.find('h1 class="big"'):]
			self.titel = self.titel[self.titel.find('>')+1:self.titel.find('</h1')]
		else:
			self.titel = 'nicht gefunden'

		self.url = self.text[:self.text.find('\n')]
		if (self.url.find('URL:')==0):
			self.url=self.url[4:]
		else:
			self.url='nicht gefunden'

		if (self.text.find('<div id="rezept-zubereitung"')>=0):
			self.beschreibung=self.text[self.text.find('<div id="rezept-zubereitung"')+5:]
			self.beschreibung=self.beschreibung[self.beschreibung.find('>')+1:]
			self.beschreibung=self.beschreibung[:self.beschreibung.find('</div>')].strip()
		else:
			self.beschreibung='nicht gefunden'

		#Zeit
		self.zeit=0
		zeitanfang=self.text.find('Zubereitungszeit:')
		if (zeitanfang>=0):
			zeitanfang=self.text.find('class="n">',zeitanfang)+10
			zeitende=self.text.find('</span>',zeitanfang)
			if (zeitanfang>=0 and zeitende>=0):
				self.zeit=self.text[zeitanfang:zeitende]


		#Portionsgroese
		portionsgroeseanfang=self.text.find('<input type="text" name="divisor" size="2" value="')
		if (portionsgroeseanfang>=0):
			portionsgroeseanfang=portionsgroeseanfang+50
			portionsgroeseende=self.text.find('"',portionsgroeseanfang)
			self.portionsgroese=self.text[portionsgroeseanfang:portionsgroeseende]
			if (not(self.portionsgroese.isdigit())):
				self.portionsgroese=-1
		else:
			self.portionsgroese=-1

		#Find critical section (surrounded by the "zutaten" table)
		tmptext=self.text[self.text.find('table class="zutaten"'):]
		tmptext=tmptext[:tmptext.find("</table")]
		#Read the table-fields
		beg=tmptext.find('<td')
		ingrcounter=0;
		while (beg>=0):


			tmptext=tmptext[tmptext.find('>',beg)+1:]
			ingredient=tmptext[:tmptext.find('</td')]
			#remove remaining tags (e.g. <a..>)
			ingredientTagStart=ingredient.find('<')
			ingredientTagStop=ingredient.find('>',ingredientTagStart)
			while ((ingredientTagStart>=0) and (ingredientTagStop>=0)):
				ingredient=ingredient[:ingredientTagStart]+ingredient[ingredientTagStop+1:]
				ingredientTagStart=ingredient.find('<')
				ingredientTagStop=ingredient.find('>',ingredientTagStart)
			if (ingrcounter%2==0):
				amount=ingredient
			else:
				if (ingredient.strip().lower().find(u'für')!=0 and ingredient.strip().lower().find(u'außerdem')!=0 and ingredient.strip().lower().find(u'zum')!=0):
					amount=amount.strip()
					amountunit = ''
					unitbreak = amount.find('&nbsp;')
					if (unitbreak>=0):
						amountunit = amount[unitbreak+6:]
						amount = amount[:unitbreak]


					self.zutaten.append(Rezepteintrag(amount.strip(), amountunit.strip(), ingredient.strip()))
			ingrcounter=ingrcounter+1
			beg=tmptext.find('<td')


class Regeln:
# Diese Klasse stellt verschiedene Hilfsfunktionen zur Verfügung.
# Ein Objekt der Klasse wird global instanziiert, so dass alle Klassen darauf zugreifen können.

	def __init__(self):
		datei = codecs.open(configuration.getAttribute('stopwords'), "r", "utf-8")
		self.__stopwords = datei.read().split()
		datei.close()

	def bezeichnungumschreiben(self, bezeichnung):
	# Der Funktion wird eine Bezeichnung übergeben, die dann anhand der Bezeichnungs-Regeln umgeschrieben und zurückgegeben wird.
		if (bezeichnung==''):
			return ''
		else:

			SQLRequest="SELECT toingredient FROM %s WHERE ingredient=LOWER('%s') ORDER BY replacewords"% (datenbank.IngredientsRulesTable,bezeichnung)

			datenbank.DBCursor.execute(SQLRequest)
			foundingr=datenbank.DBCursor.fetchall()
			if foundingr:
				return foundingr[0][0]
			else:
				newbez=''
				for splitbez in bezeichnung.split():
					SQLRequest="SELECT toingredient FROM %s WHERE ingredient=LOWER('%s') AND replacewords=1"% (datenbank.IngredientsRulesTable,splitbez)
					datenbank.DBCursor.execute(SQLRequest)
					foundingr=datenbank.DBCursor.fetchall()
					if foundingr:
						newbez=newbez+' '+foundingr[0][0]
					else:
						newbez=newbez+' '+splitbez
				return newbez.strip()

	def umrechnungsverhaeltnis(self,einheit,bezeichnung):
	# Anhand übergebener Mengeneinheit und einer Zutaten-Beschreibung aus der Nährwerttabelle liefert diese Funktion ein Umrechnungsverhältnis für die Masse der Zutat in Gramm.
	# Beispielsweise ergibt der Aufruf "umrechnungsverhaeltnis('Stück', 'Hühnerei roh') das Verhältnis "50", woraus dann folgt, dass "3 Stück Hühnerei roh" eine Masse von 3 x 50 Gramm haben.
	# Falls keine Menge ermittelt werden kann, wird 0 zurückgegeben, falls es sich um eine konstante Menge handelt,
	# die nicht mehr mit dem Mengenquantum multipliziert werden sollte (z.B. bei "Prise Salz"), wird der zurückgegebene Wert mit -1 multipliziert, so dass dieser kleiner 0 ist.


		SQLRequest="SELECT grams,constamount,ingredient FROM %s WHERE unit=LOWER('%s') AND ingredient=LOWER('%s') ORDER BY ingredient DESC"% (datenbank.QuantityRulesTable,einheit,bezeichnung)
		datenbank.DBCursor.execute(SQLRequest)
		foundquan=datenbank.DBCursor.fetchall()
		if foundquan:
			if foundquan[0][1]==1:
				return -foundquan[0][0]
			else:
				return foundquan[0][0]
		else:
			bezeichnung=bezeichnung.split()[0]

			abschneidenab=-1
			abschneidzeichen=',(/'
			for zeichen in abschneidzeichen:
				abschneiden=einheit.find(zeichen)
				if (abschneiden>0) and ((abschneidenab==-1) or (abschneiden<abschneidenab)):
					abschneidenab=abschneiden
			if abschneidenab>0:
				einheit=einheit[:abschneidenab]

			SQLRequest="SELECT grams,constamount,ingredient FROM %s WHERE unit=LOWER('%s') AND (ingredient='' OR ingredient=LOWER('%s') ) ORDER BY ingredient DESC"% (datenbank.QuantityRulesTable,einheit,bezeichnung)
			datenbank.DBCursor.execute(SQLRequest)
			foundquan=datenbank.DBCursor.fetchall()
			if foundquan:
				if foundquan[0][1]==1:
					return -foundquan[0][0]
				else:
					return foundquan[0][0]
			else:
				SQLRequest="SELECT grams,constamount,ingredient FROM %s WHERE unit='' AND ingredient=LOWER('%s') ORDER BY ingredient DESC"% (datenbank.QuantityRulesTable,bezeichnung)

				datenbank.DBCursor.execute(SQLRequest)
				foundquan=datenbank.DBCursor.fetchall()
				if foundquan:
					if foundquan[0][1]==1:
						return -foundquan[0][0]
					else:
						return foundquan[0][0]
				else:
					return 0

	def stopword(self,word):
	# Die Funktion liefert "true", falls ein übergebenes Wort in der verwendeten Stopwortliste enthalten ist, ansonsten wird "false" zurückgegeben.

		if word in self.__stopwords:
			return True
		else:
			return False

	def stemsentence(self, sentence):
	# Diese Funktion führt alle Wörter in einem übergebenen Satz auf deren Wortstamm zurück und liefert den umgeformten Satz zurück.

		retsent=''
		for words in sentence.split():
			retsent=retsent+' '+self.stemword(words)
		return retsent.strip()


	def stemword(self,word):
	# Diese Funktion verwendet den auf "http://snowball.tartarus.org/algorithms/german/stemmer.html" beschriebenen "Snowball-Stemmer",
	# um ein übergebenes Wort auf dessen Wortstamm zurückzuführen, der dann zurückgeliefert wird.

		word=word.strip().lower()
		vowels=[u'a',u'e',u'i',u'o',u'u',u'y',u'ä',u'ö',u'ü']
		validsending=[u'b',u'd',u'f',u'g',u'h',u'k',u'l',u'm',u'n',u'r',u't']
		validstending=[u'b',u'd',u'f',u'g',u'h',u'k',u'l',u'm',u'n',u't']

		# replace ß by ss
		word=word.replace(u'ß',u'ss')

		# put u and y between vowels into upper case.
		for u in re.finditer(u'u',word):
			if (u.start()>0 and u.start()<(len(word)-1)):
				if (word[u.start()-1] in vowels) and (word[u.start()+1] in vowels):
					word=word[:u.start()]+u'U'+word[u.start()+1:]

		for y in re.finditer(u'y',word):
			if (y.start()>0 and y.start()<(len(word)-1)):
				if (word[y.start()-1] in vowels) and (word[y.start()+1] in vowels):
					word=word[:y.start()]+u'Y'+word[y.start()+1:]

		# R1 and R2 are first set up in the standard way
		r1=-1
		r2=-1
		pos=0
		for letter in word:
			if r1==-1:
				if letter in vowels:
					r1=-2
			elif r1==-2:
				if letter not in vowels:
					r1=pos+1
			elif r2==-1:
				if letter in vowels:
					r2=-2
			elif r2==-2:
				if letter not in vowels:
					r2=pos+1
			pos=pos+1
		if r1<0 or r1>=len(word):
			r1=-1
		#but then R1 is adjusted so that the region before it contains at least 3 letters
		elif (r1<3):
			r1=3
		if r2<0 or r2>=len(word):
			r2=-1

		# Step 1: Search for the longest among the following suffixes,

		# (a) em   ern   er
		if (word[-3:]==u'ern' and (r1>=0) and len(word)-r1>=3):
			word=word[:-3]
		elif (word[-2:]==u'em' and (r1>=0) and len(word)-r1>=2):
			word=word[:-2]
		elif (word[-2:]==u'er' and (r1>=0) and len(word)-r1>=2):
			word=word[:-2]

		# (b) e   en   es
		# If an ending of group (b) is deleted, and the ending is preceded by niss, delete the final s.
		elif (word[-2:]==u'en' and (r1>=0) and len(word)-r1>=2):
			word=word[:-2]
			if (word[-4:]==u'niss'):
				word=word[:-1]
		elif (word[-2:]==u'es' and (r1>=0) and len(word)-r1>=2):
			word=word[:-2]
			if (word[-4:]==u'niss'):
				word=word[:-1]
		elif (word[-1:]==u'e' and (r1>=0) and len(word)-r1>=1):
			word=word[:-1]
			if (word[-4:]==u'niss'):
				word=word[:-1]

		# (c) s (preceded by a valid s-ending)
		elif (word[-1:]==u's' and (r1>=0) and len(word)-r1>=1):
			if word[-2:-1] in validsending:
				word=word[:-1]

		# Step 2: Search for the longest among the following suffixes,

		# (a) en   er   est
		if (word[-3:]==u'est' and (r1>=0) and len(word)-r1>=3):
			word=word[:-3]
		elif (word[-2:]==u'en' and (r1>=0) and len(word)-r1>=2):
			word=word[:-2]
		elif (word[-2:]==u'er' and (r1>=0) and len(word)-r1>=2):
			word=word[:-2]

		# (b) st (preceded by a valid st-ending, itself preceded by at least 3 letters)
		elif (word[-2:]==u'st' and (r1>=0) and len(word)-r1>=2):
			if word[-3:-2] in validstending and len(word)>=6:
				word=word[:-2]


		# Step 3: d-suffixes (*) Search for the longest among the following suffixes, and perform the action indicated.

		# end   ung
		# 	delete if in R2
		# 	if preceded by ig, delete if in R2 and not preceded by e
		if ((word[-3:]==u'end' or word[-3:]==u'ung') and (r2>=0) and len(word)-r2>=3):
			if (word[-5:-3]==u'ig' and len(word)-r2>=5 and word[-6:-5]!=u'e'):
				word=word[:-5]
			else:
				word=word[:-3]

		# ig   ik   isch
		# 	delete if in R2 and not preceded by e
		if (word[-4:]==u'isch' and (r2>=0) and len(word)-r2>=4 and word[-5]!=u'e'):
			word=word[:-4]
		if ((word[-2:]==u'ig' or word[-2:]==u'ik') and (r2>=0) and len(word)-r2>=2 and word[-3]!=u'e'):
			word=word[:-2]

		# lich   heit
		# 	delete if in R2
		# 	if preceded by er or en, delete if in R1
		if (word[-4:]==u'lich' or word[-4:]==u'heit'):
			if (word[-6:-4]==u'er' or word[-6:-4]==u'en') and (r1>=0) and len(word)-r1>=6:
				word=word[:-6]
			elif ((r2>=0) and len(word)-r2>=4):
				word=word[:-4]

		# keit
		# 	delete if in R2
		# 	if preceded by lich or ig, delete if in R2
		if word[-4:]==u'keit' and r2>=0 and len(word)-r2>=4:
			if word[-6:-4]==u'ig' and r2>=0 and len(word)-r2>=6:
				word=word[:-6]
			elif word[-8:-4]==u'lich' and r2>=0 and len(word)-r2>=8:
				word=word[:-8]
			else:
				word=word[:-4]


		# turn U and Y back into lower case, and remove the umlaut accent from a, o and u.
		word=word.replace(u'U',u'u')
		word=word.replace(u'Y',u'y')
		word=word.replace(u'ü',u'u')
		word=word.replace(u'ö',u'o')
		word=word.replace(u'ä',u'a')

		return word

        
class Rezept1:
    
    def __init__(self, dateiname):

        self.json = '' # Der Quelltext des Rezeptes im HTML-Format.
        self.zutaten = [] # Eine Liste aller im Rezept enthaltenen Zutaten. Jede Zutat ist dabei eine Instanz der Klasse "Rezepteintrag".
        self.url= '' # Die URL des Rezeptes.
        self.beschreibung = '' # Die Zubereitungs-Beschreibung des Rezeptes.
        self.titel = '' # Der Titel des Rezeptes.

        self.menge = 0.0 # Die Gesamtmasse des Rezeptes, also die Summe der Masse aller enthaltenen Zutaten.
        self.portionsgroese = -1 # Anzahl der Portionen, zum Beispiel "4"

        self.naehrwerte = {} # Eine Liste aller im Rezept enthaltenen N婲werte. Enthaltene Kilokalorien sind beispielsweise 𢥲 den Wert "naehrwerte['GCAL']" abrufbar, enthaltene Proteine in Milligramm 𢥲 den Wert "naehrwerte['ZE']". Die Abk𲺵ngen und Einheiten der verschiedenen N婲werte k򮮥n dem Handbuch des Bundeslebensmittelschl𳳥ls (Seite 24-28) entnommen werden.
        self.naehrwertepro100g = {} # Eine Liste aller im Rezept enthaltenen N婲werte pro 100g.

        self.__readJson(dateiname)
        self.__parseJson()

        for zutat in self.zutaten:
            if zutat.besteZutat!='' and zutat.mengeInG>0.0:
                self.menge=self.menge+zutat.mengeInG
                for key in zutat.besteZutat.naehrwerte:
                    #zutat.besteZutat.naehrwerte[key]
                    if key in self.naehrwerte:
                        self.naehrwerte[key]=self.naehrwerte[key]+(float(zutat.besteZutat.naehrwerte[key])*zutat.mengeInG)
                    else:
                        self.naehrwerte[key]=float(zutat.besteZutat.naehrwerte[key])*zutat.mengeInG

        for key in self.naehrwerte:
            self.naehrwerte[key]=self.naehrwerte[key]/100.0


        # Pro 100g
        if (self.menge>0.0):
            for key in self.naehrwerte:
                self.naehrwertepro100g[key]=float(self.naehrwerte[key])*100.0/self.menge
                
    def zutatenanzeigen(self):
    # Diese Funktion kann zur Ausgabe der ermittelten Informationen verwendet werden.

        print "URL: "+ self.url.encode("iso-8859-1")
        print "Titel: "+ self.titel.encode("iso-8859-1")
        print '---'
        for zutat in self.zutaten:
            zutat.anzeigen()

        print "\n\n\nNaehrwerte im Rezept:\n"

        for key in self.naehrwerte:
            print key +": "+str(self.naehrwerte[key])+", ",
             
    def __readJson(self, dateiname):
        #with io.open(dateiname, encoding="utf-8") as json_file:
        #    data = json.load(json_file)
        self.json = json.loads(rezeptJson)
       

    def __parseJson(self):
        #Titel
        if (self.json['title']!=""):
            self.titel = self.json['title']
        else:
            self.titel = 'nicht gefunden'

        #URL
        if (self.json['recipe_href']!=""):
            self.url=self.json['recipe_href']
        else:
            self.url='nicht gefunden'

        #Rezeptzubereitung
        if (self.json['preparation_instructions']!=""):
            self.beschreibung=self.json['preparation_instructions']
        else:
            self.beschreibung='nicht gefunden'

        #Zeit
        self.zeit=0
        if (self.json['duration']!=""):
            self.zeit=self.json['duration']
        else:
            self.zeit='nicht gefunden'
        
        #Zutaten
        self.zutatenRaw = []
        zutaten = self.json['ingredients_string'].split('\n')
        
        zutaten = [item for item in zutaten if ":" in item]
        
        for zutatRaw in zutaten:
            self.zutatenRaw.append(zutatRaw.strip())
        
        for index, zutatRaw in enumerate(self.zutatenRaw):
            if ":" in zutatRaw:
                var1 = self.zutatenRaw[index].split(":")
                var2 = var1[0].split(" ")
                self.zutatenRaw[index] = []
                
                try:
                    self.zutatenRaw[index].append(var2[0])
                except IndexError:
                    '1'
                try:
                    self.zutatenRaw[index].append(var2[1]) 
                except IndexError:
                    '2'
                try:
                    self.zutatenRaw[index].append(var1[1]) 
                except IndexError:
                    '3'  
            else:
                self.zutatenRaw.remove(zutatRaw)
        print self.zutatenRaw

        for zutat in self.zutatenRaw:
            zutatLength = len(zutat)
            if zutatLength == 3:
                self.zutaten.append(Rezepteintrag(zutat[0].lower().strip(),zutat[1].lower().strip(),zutat[2].lower().strip()))
            elif zutatLength == 2:
                self.zutaten.append(Rezepteintrag(zutat[0].lower().strip(),'',zutat[1].lower().strip()))
            else:
                '1'
# Globale Datenbank
datenbank=DatenBank()

# Globale Regeln
regeln=Regeln()

#if (len(sys.argv)>1):
#	rezept = Rezept(sys.argv[1])
#	rezept.zutatenanzeigen()