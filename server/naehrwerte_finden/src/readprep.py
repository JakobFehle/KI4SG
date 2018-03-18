# coding=utf-8

from __future__ import division
from findnutr import *

import subprocess
import treetaggerwrapper
import math

class Zeiteinheit:
	def __init__(self,wortl,inminuten,satzNr,nebensatzNr,wortNr):
		self.wortlaut=wortl
		self.inminuten=inminuten
		self.satzNummer=satzNr
		self.nebensatzNummer=nebensatzNr
		self.wortNummer=wortNr

class Zeitquantitaet:
	def __init__(self,wortl,faktor,satzNr,nebensatzNr,wortNr):
		self.wortlaut=wortl
		self.faktor=faktor
		self.satzNummer=satzNr
		self.nebensatzNummer=nebensatzNr
		self.wortNummer=wortNr

class ZeitManager:
	def __init__(self):
		self.zeiteinheiten=[]
		self.zeitquantitaeten=[]
		
	def vorgangszeitverbrauchSchaetzen(self, vorgangsmanager):
		zeitv=0.0
		for vorg in vorgangsmanager.vorgaenge:
			if vorg.typ==1:
				zeitv=zeitv+vorg.zeitverbrauch
			else:
				zeitv=zeitv+vorg.zeitverbrauch*len(vorg.zutatenRelationen)
		self.vorgangsZeitverbrauch=zeitv
	
	
	def neueZeiteinheit(self,wortl,inminuten,satzNr,nebensatzNr,wortNr):
		self.zeiteinheiten.append(Zeiteinheit(wortl,inminuten,satzNr,nebensatzNr,wortNr))
	def neueZeitquantitaet(self,wortl,faktor,satzNr,nebensatzNr,wortNr):
		self.zeitquantitaeten.append(Zeitquantitaet(wortl,faktor,satzNr,nebensatzNr,wortNr))
	def zeitrelationenFinden(self):
		self.zeitliste=[] # [insgesamt,quanindex,einhindex]
		self.zeitDirekt=0
		for einhindex,zeiteinh in enumerate(self.zeiteinheiten):
			gefundenezeit=-1
			quindex=-1
			for quanindex,zeitquanti in enumerate(self.zeitquantitaeten):
				if ((zeitquanti.wortNummer==zeiteinh.wortNummer-1) or (zeitquanti.wortNummer==zeiteinh.wortNummer-3)) and (zeitquanti.satzNummer==zeiteinh.satzNummer):
					if gefundenezeit==-1:
						gefundenezeit=zeitquanti.faktor
						quindex=quanindex
					else:
						
						gefundenezeit=(zeitquanti.faktor+gefundenezeit)/2.0
						break
			if gefundenezeit==-1:
				gefundenezeit=0	# Falls keine Zeitquantitaet zu einer Einheit gefunden werden kann verwende 0 (auch 1 waere moeglich/sinnvoll)
			self.zeitliste.append([gefundenezeit*zeiteinh.inminuten,quindex,einhindex])
			self.zeitDirekt=self.zeitDirekt+gefundenezeit*zeiteinh.inminuten
	def ausgabe(self):
		print "Insgesamter Zeitverbrauch: "+str(self.vorgangsZeitverbrauch+self.zeitDirekt)+" Minuten<br /><br />"
		print u"Geschätzte Zeit für die Vorgänge: ".encode("iso-8859-1")+str(self.vorgangsZeitverbrauch)+" Minuten<br />"
		print "Direkt gefundener Zeitverbrauch: "+str(self.zeitDirekt)+" Minuten<br />"
		#for zeitlistenEintraege in self.zeitliste:
		#	if zeitlistenEintraege[1]==-1:
		#		print "   ? ->"+self.zeiteinheiten[zeitlistenEintraege[2]].wortlaut.encode("iso-8859-1")+"<br />"
		#	else:
		#		print "   "+str(zeitlistenEintraege[0])+" Minuten ("+self.zeiteinheiten[zeitlistenEintraege[2]].wortlaut.encode("iso-8859-1")+")<br />"
		
class VorgangsManager:
	def __init__(self):
		self.vorgaenge=[]
	def neuerVorgang(self, wortl, unterg, oberg, obergID,typ,zeitverbrauch,satzNr,nebensatzNr,wortNr):
		self.vorgaenge.append(Vorgang(wortl, unterg, oberg, obergID,typ,zeitverbrauch,satzNr,nebensatzNr,wortNr))
		return len(self.vorgaenge)-1
	def getVorgang(self,vorgangsNr):
		return self.vorgaenge[vorgangsNr]
	def ausgabe(self):
		for vorg in self.vorgaenge:
			vorg.ausgabe()
	
class Vorgang:
	def __init__(self, wortl, unterg, oberg, obergID,typ,zeitverbrauch,satzNr,nebensatzNr,wortNr):
		self.wortlaut=wortl
		self.untergruppe=unterg
		self.obergruppe=oberg
		self.obergruppenID=obergID
		self.zeitverbrauch=zeitverbrauch
		self.zutatenRelationen={}
		self.satzNummer=satzNr
		self.nebensatzNummer=nebensatzNr
		self.wortNummer=wortNr
		self.typ=typ
	def ausgabe(self):
		print self.wortlaut.encode("iso-8859-1")

class ZutatenManager:
	def __init__(self):
		self.zutaten=[]
	def neueZutat(self, zutatAusZutatenliste, bewertung,satzNr,nebensatzNr,wortNr):
		self.zutaten.append(Zutat(zutatAusZutatenliste, bewertung,satzNr,nebensatzNr,wortNr))
		return len(self.zutaten)-1
	def getZutat(self,zutatenNr):
		return self.zutaten[zutatenNr]
	def ausgabe(self):
		for zut in self.zutaten:
			zut.ausgabe()
	def relationenZuZutatenlisteZuordnen(self,vorgMan):
		for zuta in self.zutaten:
			zuta.relationenZuZutatenlisteZuordnen(vorgMan)
	
class Zutat:
	def __init__(self,zutatAusZutatenliste,bewertung,satzNr,nebensatzNr,wortNr):
		self.zutatenlistenZutat=zutatAusZutatenliste
		self.wortlaut=self.zutatenlistenZutat[1].suchNachVorUmschreiben
		self.zugehoerigkeitsBewertung=bewertung
		self.vorgangsRelationen={}
		self.satzNummer=satzNr
		self.nebensatzNummer=nebensatzNr
		self.wortNummer=wortNr
		
	def ausgabe(self):
		print self.wortlaut.encode("iso-8859-1")
	def relationenZuZutatenlisteZuordnen(self,vorgMan):
		
		if len(self.zutatenlistenZutat)<3:
			self.zutatenlistenZutat.append({})
		for rel in self.vorgangsRelationen:
			if vorgMan.getVorgang(rel).obergruppe in self.zutatenlistenZutat[2]:
				if vorgMan.getVorgang(rel).untergruppe not in self.zutatenlistenZutat[2][vorgMan.getVorgang(rel).obergruppe]:
					self.zutatenlistenZutat[2][vorgMan.getVorgang(rel).obergruppe].append(vorgMan.getVorgang(rel).untergruppe)
			else:
				self.zutatenlistenZutat[2][vorgMan.getVorgang(rel).obergruppe]=[vorgMan.getVorgang(rel).untergruppe]
		
class WerkzeugManager:
	def __init__(self):
		self.werkzeuge=[]
	def neuesWerkzeug(self, wortl, unterg, oberg, obergID,satzNr,nebensatzNr,wortNr):
		schonvorhanden=-1
		for windex,werk in enumerate(self.werkzeuge):
			if unterg==werk.untergruppe:
				schonvorhanden=windex
		if schonvorhanden==-1:
			self.werkzeuge.append(Werkzeug(wortl, unterg, oberg, obergID,satzNr,nebensatzNr,wortNr))
			return len(self.werkzeuge)-1
		else:
			return windex
	def getWerkzeug(self,werkzeugNr):
		return self.werkzeuge[werkzeugNr]
	def ausgabe(self):
		for werk in self.werkzeuge:
			werk.ausgabe()
			print "<br />"
	
class Werkzeug:
	def __init__(self,wortl, unterg, oberg, obergID,satzNr,nebensatzNr,wortNr):
		self.wortlaut=wortl
		self.untergruppe=unterg
		self.obergruppe=oberg
		self.obergruppenID=obergID
		self.satzNummer=satzNr
		self.nebensatzNummer=nebensatzNr
		self.wortNummer=wortNr

	def ausgabe(self):
		print self.obergruppe.encode("iso-8859-1")+" (Wortlaut '"+self.wortlaut.encode("iso-8859-1")+"' wurde als '"+self.untergruppe.encode("iso-8859-1")+"' erkannt)"
	
class ContainerwortManager:
	def __init__(self):
		self.containerwoerter=[]
	def neuesContainerwort(self, wortl, satzNr,nebensatzNr,wortNr):
		self.containerwoerter.append(Containerwort(wortl, satzNr,nebensatzNr,wortNr))
	def getContainerwort(self,containerwortNr):
		return self.conteinerwoerter[containerwortNr]

class Containerwort:
	def __init__(self,wortl, satzNr,nebensatzNr,wortNr):
		self.wortlaut=wortl
		self.satzNummer=satzNr
		self.nebensatzNummer=nebensatzNr
		self.wortNummer=wortNr

class ZubereitungsBeschreibung:

	def __init__(self, dateiname):
		self.rezept = Rezept(dateiname) # Rezept einlesen und Zutaten finden
		self.wortListen=WortListenVerwaltung()
		self.beschreibung = self.beschreibungsvorverarbeitung(self.rezept.beschreibung) # Vorverarbeitung der Beschreibung
		#print self.beschreibung.encode("iso-8859-1")
		#self.beschreibungMitWortTags=[]	
		
		self.vorgangsMan=VorgangsManager()
		self.zutatenMan=ZutatenManager()
		self.werkzeugMan=WerkzeugManager()
		self.containerwortMan=ContainerwortManager()
		self.zutatenVorgangsPaare=[]
		self.zeitMan=ZeitManager()
		
		# Abbruch bei leerer Beschreibung	
		if self.beschreibung=='':
			print >> sys.stderr, 'Ungueltige Rezeptbeschreibung'
		
		# Gueltige Rezeptbeschreibung
		else:
			
			self.beschreibungMitTags = self.postagger(self.beschreibung)
			
			
			self.beschreibungMitTags = self.bruchumwandler(self.beschreibungMitTags)
			
			self.zutatenliste = [[self.erstesWort(zut.suchNachVorUmschreiben).lower(),zut] for zut in self.rezept.zutaten]
				

				
			self.findeWorttypen()
			
			self.findeRelationen()
			
			self.zutatenMan.relationenZuZutatenlisteZuordnen(self.vorgangsMan)
			
			self.zeitMan.zeitrelationenFinden()
			
			self.zeitMan.vorgangszeitverbrauchSchaetzen(self.vorgangsMan)
			
#			print "<h3>Werkzeuge:</h3>",
			
#			self.werkzeugMan.ausgabe()
			
#			print "<h3>Zeitverbrauch:</h3>",
			
#			self.zeitMan.ausgabe()

#			print "<h3>Zutaten:</h3>",
			#erstdurchlauf=True
			for zutatenl in self.zutatenliste:
				#print zutatenl[0].encode("iso-8859-1")
				#if erstdurchlauf==False:
				#	print ',',
				#erstdurchlauf=False
				#print '<span style="cursor:pointer; color: #0000BB;" onclick=\'$("zutat").value="'+zutatenl[1].suchNachVorUmschreiben.encode("iso-8859-1")+'"\'>',
#				print zutatenl[1].suchNachVorUmschreiben.encode("iso-8859-1")+': ',
				if len(zutatenl)>2:
					for vorgindex in zutatenl[2]:
						#für die evaluation
						self.zutatenVorgangsPaare.append(zutatenl[1].suchNachVorUmschreiben+'@'+vorgindex)
#						print vorgindex.encode("iso-8859-1")+" ",
				
#				print ""
			self.zutatenVorgangsPaare=set(self.zutatenVorgangsPaare)
				#print '</span>',
#			print ''
				
			#self.zutatenliste = zut for zut in (1,2,3)
			
			#print self.zutatenliste


							
			#print "<br /><br /><h3>Beschreibung:</h3>",
			
			#print self.beschreibung.encode("iso-8859-1")
			
			#for worter in self.beschreibungMitTags:
			#	print worter[0].encode("iso-8859-1"),
			#	if len(worter)>3:
			#		#print worter[3]
			#		if worter[3][0]=='Zutat':
			#			print ' ('+self.zutatenMan.zutaten[worter[3][1]].wortlaut.encode("iso-8859-1")+') ',
			#		elif worter[3][0]=='Vorgang':
			#			print ' ('+self.vorgangsMan.vorgaenge[worter[3][1]].obergruppe.encode("iso-8859-1")+') ',
			#		elif worter[3][0]=='Werkzeug':
			#			print ' ('+self.werkzeugMan.werkzeuge[worter[3][1]].obergruppe.encode("iso-8859-1")+') ',
				
			#print self.rezept.beschreibung.encode("iso-8859-1")
			

	def bruchumwandler(self,beschreibung):
		for index,wort in enumerate(beschreibung):
			ganzzahl=-1
			if wort[0]=='/':
				if (index>0) and (index<len(beschreibung)-1):
					zaehler=self.wortListen.istZeitquantitaet(beschreibung[index-1][0])
					nenner=self.wortListen.istZeitquantitaet(beschreibung[index+1][0])
					if  zaehler!=-1 and nenner!=-1:
						neuezahl=zaehler/nenner
						if (index>1):
							ganzzahl=self.wortListen.istZeitquantitaet(beschreibung[index-2][0])
							if ganzzahl!=-1:
								neuezahl=neuezahl+ganzzahl
								
						wort[0]=str(neuezahl)
						
						del beschreibung[index+1]
						del beschreibung[index-1]
						if ganzzahl!=-1:
							del beschreibung[index-2]
			if wort[0]==',':
				if (index>0) and (index<len(beschreibung)-1):
					vorKomma=self.wortListen.istZeitquantitaet(beschreibung[index-1][0])
					nachKomma=self.wortListen.istZeitquantitaet(beschreibung[index+1][0])
					if vorKomma!=-1 and nachKomma!=-1:
						neuezahl=self.wortListen.istZeitquantitaet(str(beschreibung[index-1][0])+'.'+str(beschreibung[index+1][0]))
						if neuezahl!=-1:
							wort[0]=str(neuezahl)
							del beschreibung[index+1]
							del beschreibung[index-1]
					
		
		return beschreibung
	
	

			
	def findeRelationen(self):

			
		for vorgIndex,vorg in enumerate(self.vorgangsMan.vorgaenge):


			sucheWarErfolgreich=False


			if (self.wortListen.istPartiPer(vorg.wortlaut)):
				for zutIndex,zut in enumerate(self.zutatenMan.zutaten):
					if (zut.wortNummer==vorg.wortNummer+1):
						vorg.zutatenRelationen[zutIndex]=1.0
						zut.vorgangsRelationen[vorgIndex]=1.0
						sucheWarErfolgreich=True
						break
					elif (zut.wortNummer>vorg.wortNummer+1):
						break



			if sucheWarErfolgreich==False:
				# Falls im selben Satz wie der Vorgang vor dem Vorgang keine Zutat steht, wird im selben Satz hinter der Zutat gesucht
				for zutIndex,zut in enumerate(self.zutatenMan.zutaten):
					if (zut.satzNummer==vorg.satzNummer) and (zut.nebensatzNummer==vorg.nebensatzNummer):
						if (zut.wortNummer>vorg.wortNummer):
							#print vorg.wortlaut.encode("iso-8859-1")+' -> '+zut.wortlaut.encode("iso-8859-1")
							vorg.zutatenRelationen[zutIndex]=1.0
							zut.vorgangsRelationen[vorgIndex]=1.0
							sucheWarErfolgreich=True
						else:
							break

			if sucheWarErfolgreich==False:
				satznummerDerErstenZutatDieVorVorgangSteht=-1
				nebensatznummerDerErstenZutatDieVorVorgangSteht=-1
				for zutIndex in range(len(self.zutatenMan.zutaten)-1,-1,-1):
					zut=self.zutatenMan.zutaten[zutIndex]
					
					#if (vorg.typ!=1) and (zut.satzNummer<vorg.satzNummer-2):
					#	break
					
					if ((zut.wortNummer<vorg.wortNummer) and (satznummerDerErstenZutatDieVorVorgangSteht==-1)):
						
						satznummerDerErstenZutatDieVorVorgangSteht=zut.satzNummer
						nebensatznummerDerErstenZutatDieVorVorgangSteht=zut.nebensatzNummer
						
					if satznummerDerErstenZutatDieVorVorgangSteht!=-1:
						if vorg.typ==1: # typ=1 -> erhitzen
							vorg.zutatenRelationen[zutIndex]=1.0
							zut.vorgangsRelationen[vorgIndex]=1.0
						elif satznummerDerErstenZutatDieVorVorgangSteht==zut.satzNummer: # and (zut.nebensatzNummer!=vorg.nebensatzNummer or zut.satzNummer<vorg.satzNummer or nebensatznummerDerErstenZutatDieVorVorgangSteht==zut.nebensatzNummer):
							#print vorg.wortlaut.encode("iso-8859-1")+' ~> '+zut.wortlaut.encode("iso-8859-1")
							vorg.zutatenRelationen[zutIndex]=1.0
							zut.vorgangsRelationen[vorgIndex]=1.0
						else:
							break
						
					
					
			



	def findeWorttypen(self):
		satznummer=0
		nebensatznummer=0
		wortnummer=0
		
		for woerterInBeschreibung in self.beschreibungMitTags:
			
			woerterInBeschreibung[0]=woerterInBeschreibung[0].strip()
			
			originalWortInBeschreibung=woerterInBeschreibung[0]
			
			woerterInBeschreibung[0]=self.wortListen.ersetzungsregelSuchen(woerterInBeschreibung[0])
			
			erfolgreichZugeordnet=False
			#typ='Unzugeordnet'
			#data=''
			#print woerterInBeschreibung[0]+' ('+woerterInBeschreibung[1]+')'
			
			if woerterInBeschreibung[0]!='' and len(woerterInBeschreibung)>1:
				#print woerterInBeschreibung
			#	if (self.wortListen.istVerb(woerterInBeschreibung[0])):
			#		woerterInBeschreibung[1]='V'
				
			
			#[0, 'Unzugeordnet'],[1, 'Werkzeug'],[2, 'Zutat'],[3, 'Containerwort'],[4, 'Vorgang'],[5,'Komma'],[6,'Punkt']	
			
				zutatenGruppenListe=[u'brot',u'obst',u'gemüse',u'gewürze',u'fisch',u'fleisch']
			
				wortnummer=wortnummer+1
				
				zeiteinheit=self.wortListen.istZeiteinheit(woerterInBeschreibung[0].lower())
				zeitquantitaet=self.wortListen.istZeitquantitaet(woerterInBeschreibung[0].lower())
				
				if woerterInBeschreibung[0]=='.':
					satznummer=satznummer+1
					nebensatznummer=0
					erfolgreichZugeordnet=True
				elif woerterInBeschreibung[0]==',':
					nebensatznummer=nebensatznummer+1
					erfolgreichZugeordnet=True
				elif 'alle' == woerterInBeschreibung[0].lower():
					wortnummer=wortnummer-1
					erfolgreichZugeordnet=True
					for zut in self.zutatenliste:
						wortnummer=wortnummer+1
						zutindex=self.zutatenMan.neueZutat(zut,1.0,satznummer,nebensatznummer,wortnummer)
						woerterInBeschreibung.append(['Zutat',zutindex])
				elif zeiteinheit!=-1:
					self.zeitMan.neueZeiteinheit(woerterInBeschreibung[0],zeiteinheit,satznummer,nebensatznummer,wortnummer)
					
				elif zeitquantitaet!=-1:
					self.zeitMan.neueZeitquantitaet(woerterInBeschreibung[0],zeitquantitaet,satznummer,nebensatznummer,wortnummer)
				
				elif woerterInBeschreibung[0].lower() in zutatenGruppenListe:
					
					for zut in self.zutatenliste:
						if zut[1].zutatenGruppe==woerterInBeschreibung[0].lower():
							erfolgreichZugeordnet=True		
							zutindex=self.zutatenMan.neueZutat(zut,1.0,satznummer,nebensatznummer,wortnummer)
							woerterInBeschreibung.append(['Zutat',zutindex])
							wortnummer=wortnummer+1
					if erfolgreichZugeordnet==True:
						wortnummer=wortnummer-1
					else:
						erfolgreichZugeordnet=True		
				
				# falls vom Postagger ein Nomen gefunden wird:
				elif woerterInBeschreibung[1][0]=='N':
					
					zutatenZugehoerigkeitsIndikatorWort=self.wortListen.enthaeltZutatenZugehoerigkeitsIndikatorWort(woerterInBeschreibung[0])
					if (zutatenZugehoerigkeitsIndikatorWort!=''):
						
						for zut in self.zutatenliste:
							if zutatenZugehoerigkeitsIndikatorWort in zut[0]:
								#typ='Zutat'
								#data=[zut,1.0]
								erfolgreichZugeordnet=True
								zutindex=self.zutatenMan.neueZutat(zut,1.0,satznummer,nebensatznummer,wortnummer)
								woerterInBeschreibung.append(['Zutat',zutindex])
								break
					
					if erfolgreichZugeordnet==False:	
						werkzeug=self.wortListen.werkzeugSuchen(woerterInBeschreibung[0])
						if werkzeug[0]!='':
							erfolgreichZugeordnet=True
							#typ='Werkzeug'
							#data=werkzeug
							werkindex=self.werkzeugMan.neuesWerkzeug(woerterInBeschreibung[0], werkzeug[0], werkzeug[2], werkzeug[1],satznummer,nebensatznummer,wortnummer)
							woerterInBeschreibung.append(['Werkzeug',werkindex])
							
					if erfolgreichZugeordnet==False:	
						containerwort=self.wortListen.istContainerwort(woerterInBeschreibung[0])
						if containerwort:
							erfolgreichZugeordnet=True
							self.containerwortMan.neuesContainerwort(woerterInBeschreibung[0],satznummer,nebensatznummer,wortnummer)
							#typ='Containerwort'
							#data=woerterInBeschreibung[0]
					
					
					if erfolgreichZugeordnet==False:	
						passtZusammen=max([[zut,self.passtZusammenBewertung(woerterInBeschreibung[0].lower(),self.wortListen.ersetzungsregelSuchen(zut[0]).lower())] for zut in self.zutatenliste], key=lambda l: l[1])
						
						if (passtZusammen[1]>0.35):							
							
							# Zutat aus Zutatenliste
							#typ='Zutat'
							#data=passtZusammen
							erfolgreichZugeordnet=True
							zutindex=self.zutatenMan.neueZutat(passtZusammen[0],passtZusammen[1],satznummer,nebensatznummer,wortnummer)
							woerterInBeschreibung.append(['Zutat',zutindex])
				
				if erfolgreichZugeordnet==False:
					#print woerterInBeschreibung[0]
					gefundenerVorgang=self.wortListen.vorgangSuchen(woerterInBeschreibung[0])
					if gefundenerVorgang[0]!='':
						# Wort ist Vorgang 
						#typ='Vorgang'
						#data=gefundenerVorgang
						erfolgreichZugeordnet=True
						vorindex=self.vorgangsMan.neuerVorgang(woerterInBeschreibung[0], gefundenerVorgang[0], gefundenerVorgang[2], gefundenerVorgang[1],gefundenerVorgang[3],gefundenerVorgang[4],satznummer,nebensatznummer,wortnummer)
						woerterInBeschreibung.append(['Vorgang',vorindex])
					#print '->'+gefundenerVorgang[2]
			
			
			
						
			
			#self.beschreibungMitWortTags.append([originalWortInBeschreibung,WortTag(typ,data),woerterInBeschreibung[1]])
			








			
				
	def loescheSonderzeichen(self, zeichenkette):
		zeichenkette=zeichenkette.replace('&nbsp;',' ')
		zeichenkette=zeichenkette.replace("&auml;",u"ä")
		zeichenkette=zeichenkette.replace("&szlig;",u"ß")
		zeichenkette=zeichenkette.replace("&uuml;",u"ü")
		zeichenkette=zeichenkette.replace("&ouml;",u"ö")
		zeichenkette=zeichenkette.replace("&Auml;",u"Ä")
		zeichenkette=zeichenkette.replace("&Uuml;",u"Ü")
		zeichenkette=zeichenkette.replace("&Ouml;",u"Ö")
		
		zeichenkette =zeichenkette.replace("(n)","")
		zeichenkette =zeichenkette.replace("(e)","")
		zeichenkette =zeichenkette.replace("(s)","")
		zeichenkette =zeichenkette.replace("(er)","")
		zeichenkette=zeichenkette.replace("(","")
		zeichenkette=zeichenkette.replace(")","")
		zeichenkette=zeichenkette.replace(";",",")
		#zeichenkette = re.sub('\(.*\)', " ", zeichenkette)
		
		zeichenkette=re.sub(u'[^A-Za-z0-9üöäÜÖÄéèáàíìêîôúùûß/.,\- ]',' ',zeichenkette)
		zeichenkette=zeichenkette.strip()
		return zeichenkette
	
	
	def erstesWort(self, satz):
		lookfor = satz
		if (lookfor.find(' ')>=0):
			lookfor=lookfor[:lookfor.find(' ')]
		return lookfor

	
	def beschreibungsvorverarbeitung(self, beschreibung):
		
		beschreibungtemp = beschreibung.replace("<br />"," ") # Zubereitungsbeschreibung kopieren und BR-Tags loeschen
		beschreibungtemp = beschreibungtemp.replace("<br>"," ")
		beschreibungtemp = beschreibungtemp.replace("<br/>"," ")
	
		beschreibungtemp=self.wortListen.abkuerzungenEntfernen(beschreibungtemp)
		
		beschreibungtemp = beschreibungtemp.replace("-"," - ")
		beschreibungtemp = beschreibungtemp.replace("/"," / ")
		
		beschreibungtemp=beschreibungtemp.replace(u'½','1/2')
		beschreibungtemp=beschreibungtemp.replace(u'¾','3/4')
		beschreibungtemp=beschreibungtemp.replace(u'¼','1/4')
		
		beschreibungtemp=self.loescheSonderzeichen(beschreibungtemp)
		
		
		
		
		return beschreibungtemp
	

	def postagger(self, beschreibungtemp):
		return treetag.tagText(beschreibungtemp)
	
		
	def postagger2(self, beschreibungtemp):
		beschreibungAufgeteiltInWorte = re.split(re.compile('(\W+)', re.UNICODE), beschreibungtemp)
		posTaggerDateiOutput = open(configuration.getAttribute('tempdir')+'rezept.tmp', 'w')

		# posTaggerDatei.write( codecs.BOM_UTF8 )
		
		for woerter in beschreibungAufgeteiltInWorte: # Woerter zeilenweise in Datei schreiben
			if woerter.strip()!='': # Leerzeichen ignorieren
				posTaggerDateiOutput.write((woerter.strip()+'\n').encode('utf-8'))
		posTaggerDateiOutput.close()
		self.runShellCommand(configuration.getAttribute('postagger') + " inFile="+configuration.getAttribute('tempdir')+"rezept.tmp,outFile="+configuration.getAttribute('tempdir')+"taggrez.tmp,paramFile="+configuration.getAttribute('postaggerparamfile')+",ruleFile="+configuration.getAttribute('postaggerrulefile'))
		
		
		posTaggerDateiInput = codecs.open(configuration.getAttribute('tempdir')+'taggrez.tmp', "r", "utf-8")
		beschreibungNachPostagger = posTaggerDateiInput.read()
		posTaggerDateiInput.close()
		
		# Array der Form
		# ((Wort1, Tag1), (Wort2, Tag2), (Wort3, Tag3), ...)
		# bilden
		beschreinungNachPostaggerArray = []
		for woerter in beschreibungNachPostagger.split('\n'):
			paarAusWortUndTag = woerter.split('\t')
			if len(paarAusWortUndTag)==2:
				beschreinungNachPostaggerArray.append(paarAusWortUndTag)
		
		return beschreinungNachPostaggerArray
	
	def passtZusammenBewertung(self, begriff1, begriff2):
		#print begriff1.encode("iso-8859-1")+" = "+begriff2.encode("iso-8859-1")
		if (begriff1=='' or begriff2==''):
			return 0.0
		elif (begriff1==begriff2):
			return 1.0
		else:
	
			begriff1umgeschrieben=regeln.bezeichnungumschreiben(begriff1)
			begriff2umgeschrieben=regeln.bezeichnungumschreiben(begriff2)
				
			laenggemz=self.laengsteGemeinsameZeichenkette(begriff1.lower(),begriff2.lower())
			
			lgz0 = len(laenggemz)
			
			#if (begriff1.lower().find(laenggemz)==0) or (begriff2.lower().find(laenggemz)==0):
			#	lgz1=lgz0
			#else:
			#	lgz1=0
						
			laenggemz2=self.laengsteGemeinsameZeichenkette(begriff1umgeschrieben.lower(),begriff2umgeschrieben.lower())					
			if (begriff1umgeschrieben.lower().find(laenggemz2)==0) or (begriff2umgeschrieben.lower().find(laenggemz2)==0):
				lgz2=len(laenggemz2)
			else:
				lgz2=0
				
			return lgz0*0.66/(len(begriff1)+len(begriff2))+lgz2*1.09/(len(begriff1umgeschrieben)+len(begriff2umgeschrieben))-0.06
	
	
	# Anzahl gemeinsamer Buchstaben
	def anzahlGemeinsamerBuchstaben(self,s1,s2):
		zaehler=0
		for buchstaben in s1:
			gefunden=s2.find(buchstaben)
			if gefunden>=0:
				if (gefunden-1>=0):
					s2=s2[gefunden-1:gefunden+1]
				else:
					s2=s2[0:gefunden+1]
				zaehler=zaehler+1
		return zaehler
	
	
	
	# Levenshtein-Distanz pro durchschnittliche Wortlaenge
	def levenshteinProWortlaenge(self,s1,s2):
		if (len(s1)>0 and len(s2)>0):
			return self.levenshtein(s1,s2)*2/float(len(s1)+len(s2))
		else:
			return -1

	
	# Berechnung der Levenshtein-Distanz
	# Uebernommen aus http://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
	def levenshtein(self,s1, s2):
		if len(s1) < len(s2):
			return self.levenshtein(s2, s1)
		if not s1:
			return len(s2)
	
		previous_row = xrange(len(s2) + 1)
		for i, c1 in enumerate(s1):
			current_row = [i + 1]
			for j, c2 in enumerate(s2):
				insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
				deletions = current_row[j] + 1       # than s2
				substitutions = previous_row[j] + (c1 != c2)
				current_row.append(min(insertions, deletions, substitutions))
			previous_row = current_row
	
		return previous_row[-1]
	
	
	# Ermittlung der laengsten gemeinsamen Zeichenfolge in zwei Strings
	def laengsteGemeinsameZeichenkette(self,S1, S2):
		# from http://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Longest_common_substring#Python
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
		return S1[x_longest-longest: x_longest]
		
	# Ermittlung der Grundform eines Verbs
	def stemverb(self,verb):
		#morphologyausgabe = subprocess.Popen(configuration.getAttribute('morphology') + ' ' + verb, shell=True, stdout=subprocess.PIPE).communicate()[0]
		morphologyausgabe = self.runShellCommand(configuration.getAttribute('morphology') + ' ' + verb)[0]
		
		kategor=morphologyausgabe.find('Kategorie: V')
		if (kategor>=0):
			morphologyausgabe=morphologyausgabe[kategor:]
		
		grundformAnfang = morphologyausgabe.find('Grundform: ')+11
		findekomma=morphologyausgabe.find(',',grundformAnfang)
		findeklammer=morphologyausgabe.find(']',grundformAnfang)
		
		if (findekomma==-1 and findeklammer==-1):
			grundformEnde=-1
		else:
			if (findekomma==-1):
				findekomma=999
			if (findeklammer==-1):
				findeklammer=999
			grundformEnde = min([findekomma,findeklammer])
		
		if (grundformAnfang>=0 and grundformEnde>=0):
			return morphologyausgabe[grundformAnfang:grundformEnde]
		else:
			return ''

			
	# Fuehrt einen Shell-Befehl aus und liefert ein Tuple aus Stdout und Stderr
	def runShellCommand(self, cmd):
		return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

class WortListenVerwaltung:
	def __init__(self):
		self.vorgangsObergruppen=self.vorgangsObergruppenEinlesen('ProcedureListMainGroup')
		self.vorgangsUntergruppen=self.untergruppenEinlesen('ProcedureListSubGroup')
		self.werkzeugObergruppen=self.obergruppenEinlesen('ToolsListMainGroup')
		self.werkzeugUntergruppen=self.untergruppenEinlesen('ToolsListSubGroup')
		self.ersetzungsregeln=self.ersetzungsregelnEinlesen()
		self.abkuerzungen=self.dateiEinlesen(configuration.getAttribute('abbreviations'))
		#self.falschzugeordneteVerben=self.dateiEinlesen(configuration.getAttribute('verbs'))
		self.containerWoerter=self.dateiEinlesen(configuration.getAttribute('containerwords'))
		self.zutatenZugehoerigkeitsIndikatorWoerter=self.dateiEinlesen(configuration.getAttribute('nouns'))
		self.zeiteinheiten=self.zeiteinheitenEinlesen()
		self.zeitquantitaeten=self.zeitquantitaetenEinlesen()
		
	
	def istZeiteinheit(self,wort):
		if wort in self.zeiteinheiten:
			return self.zeiteinheiten[wort]
		else:
			return -1
	
	
	def istZeitquantitaet(self,wort):
		if wort in self.zeitquantitaeten:
			return self.zeitquantitaeten[wort]
		else:
			wort=wort.replace(',','.')
			#if '-' in wort:
			#	woerter=wort.split('-')
			#	try:
			#		zahlenWert=(float(woerter[0])+float(woerter[1]))/2.0
			#		return zahlenWert
			#	except ValueError:
			#		return -1
			#else:
			try:
				zahlenWert=float(wort)
				return zahlenWert
			except ValueError:
				return -1
		
	
	
	
	def istPartiPer(self, wort):
		vorsilben=["ge","ab","an","auf","aus","be","bei","da","dar","de","durch","ein","ent","er","fort","ge","her","hin","hinter","los","mit","nach","nieder",u"über","um","unter","ver","vor","weg","wieder","zer","zu",u"zurück","zusammen","zwischen"]
		nachsilben=["ene","ener","enes","enen","enem","te","ter","tes","ten","tem"]
		
		hatvorsilbe=False
		hatnachsilbe=False
	
		for vorsilbe in vorsilben:
			if wort.startswith(vorsilbe):
				hatvorsilbe=True
		for nachsilbe in nachsilben:
			if wort.endswith(nachsilbe):
				hatnachsilbe=True
		#if (("ge" in wort) or ("ver" in wort) or ("zer" in wort) or ("be" in wort) or ("de" in wort)) and (wort[-4:]=="ener" or wort[-4:]=="enes" or wort[-3:]=="ene" or wort[-3:]=="nen" or wort[-3:]=="ten" or wort[-3:]=="tem" or wort[-3:]=="nem" or wort[-1]=="te" or wort[-1]=="tes" or wort[-1]=="ter"):
		if hatvorsilbe and hatnachsilbe:
			return True
		else:
			return False
	
	def enthaeltZutatenZugehoerigkeitsIndikatorWort(self,wort):
		gefunden=''
		for wor in self.zutatenZugehoerigkeitsIndikatorWoerter:
			if wor in wort:
				gefunden=wor
				break
		return gefunden
			
	
	
	def istContainerwort(self,wort):
		if wort in self.containerWoerter:
			return True
		else:
			return False
	
	
	#def istVerb(self,wort):
	#	if wort in self.falschzugeordneteVerben:
	#		return True
	#	else:
	#		return False
	
	
	
	# Sucht, ob ein Begriff aus der Liste der Vorgaenge in einem Wort enthalten ist.
	# Gibt ['',-1,''] zurueck, falls kein Eintrag gefunden werden konnte,
	# ansonsten: [Untergruppenbezeichnung, Obergruppen_ID, Obergruppenbezeichnung, Vorgangstyp, Zeitverbauch]
	def vorgangSuchen(self, wort):
		gefundenereintrag=['',-1,'']
		for untergruppeneintraege in self.vorgangsUntergruppen:
			if untergruppeneintraege[0].lower() in wort.lower():
				gefundenereintrag=[untergruppeneintraege[0],untergruppeneintraege[1],self.vorgangsObergruppen[untergruppeneintraege[1]][0],self.vorgangsObergruppen[untergruppeneintraege[1]][1],self.vorgangsObergruppen[untergruppeneintraege[1]][2]]
				break
		return gefundenereintrag


	# Sucht, ob ein Begriff aus der Liste der Werkzeuge gleich einem Wort ist.
	# Gibt ['',-1,''] zurueck, falls kein Eintrag gefunden werden konnte,
	# ansonsten: [Untergruppenbezeichnung, Obergruppen_ID, Obergruppenbezeichnung]
	def werkzeugSuchen(self, wort):
		gefundenereintrag=['',-1,'']
		for untergruppeneintraege in self.werkzeugUntergruppen:
			if untergruppeneintraege[0].lower() == wort.lower():
				gefundenereintrag=[untergruppeneintraege[0],untergruppeneintraege[1],self.werkzeugObergruppen[untergruppeneintraege[1]]]
				break
		return gefundenereintrag

	def ersetzungsregelSuchen(self,wort):

		if wort.lower() in self.ersetzungsregeln:
			return self.ersetzungsregeln[wort.lower()]
		else:
			return wort
		
		
	def abkuerzungenEntfernen(self, text):
		for abk in self.abkuerzungen:
			ab=abk.split('@')
			if ab[1]=='':
				text=text.replace(ab[0],' ')
			else:
				text=text.replace(ab[0],ab[1])
		return text

		
	def dateiEinlesen(self,dateiname):
		datei = codecs.open(dateiname, "r", "utf-8")
		inhalt = datei.read()
		datei.close()
		return inhalt.split('\n')
	
	def zeiteinheitenEinlesen(self):
		Tabelle=configuration.getAttribute('TimeUnits')	
		SQLRequest="SELECT einheit, inminuten FROM %s ORDER BY id ASC"% (Tabelle)
		datenbank.DBCursorDict.execute(SQLRequest)
		einhListe=datenbank.DBCursorDict.fetchall()
		einheitenListe={}
		for eintr in einhListe:
			einheitenListe[eintr['einheit'].lower()]=eintr['inminuten']
		return einheitenListe

	def zeitquantitaetenEinlesen(self):
		Tabelle=configuration.getAttribute('TimeQuantities')	
		SQLRequest="SELECT quantitaet, faktor FROM %s ORDER BY id ASC"% (Tabelle)
		datenbank.DBCursorDict.execute(SQLRequest)
		quaListe=datenbank.DBCursorDict.fetchall()
		quantiListe={}
		for eintr in quaListe:
			quantiListe[eintr['quantitaet'].lower()]=eintr['faktor']
		return quantiListe
	
	def ersetzungsregelnEinlesen(self):
		Tabelle=configuration.getAttribute('DescriptionReplacementRules')	
		SQLRequest="SELECT suche, ersetze FROM %s ORDER BY id ASC"% (Tabelle)
		datenbank.DBCursorDict.execute(SQLRequest)
		regListe=datenbank.DBCursorDict.fetchall()
		regelListe={}
		for eintr in regListe:
			regelListe[eintr['suche'].lower()]=eintr['ersetze']
		return regelListe
	


	def vorgangsObergruppenEinlesen(self,tabelle):
		obergruppenTabelle=configuration.getAttribute(tabelle)	
		SQLRequest="SELECT id, bezeichnung, typ, zeitverbrauchinminuten FROM %s ORDER BY id ASC"% (obergruppenTabelle)
		datenbank.DBCursorDict.execute(SQLRequest)
		obgListe=datenbank.DBCursorDict.fetchall()
		obergruppenListe={}
		for eintr in obgListe:
			obergruppenListe[(eintr['id'])]=[eintr['bezeichnung'],eintr['typ'],eintr['zeitverbrauchinminuten']]
		return obergruppenListe

	
	
		
	def obergruppenEinlesen(self,tabelle):
		obergruppenTabelle=configuration.getAttribute(tabelle)	
		SQLRequest="SELECT id, bezeichnung FROM %s ORDER BY id ASC"% (obergruppenTabelle)
		datenbank.DBCursorDict.execute(SQLRequest)
		obgListe=datenbank.DBCursorDict.fetchall()
		obergruppenListe={}
		for eintr in obgListe:
			obergruppenListe[(eintr['id'])]=eintr['bezeichnung']
		return obergruppenListe
			
	def untergruppenEinlesen(self,tabelle):
		untergruppenTabelle=configuration.getAttribute(tabelle)
		SQLRequest="SELECT obergruppen_id, bezeichnung FROM %s ORDER BY id ASC"% (untergruppenTabelle)
		datenbank.DBCursorDict.execute(SQLRequest)
		untListe=datenbank.DBCursorDict.fetchall()
		untergruppenListe=[]
		for eintr in untListe:
			untergruppenListe.append([eintr['bezeichnung'],eintr['obergruppen_id']])
		return untergruppenListe

class treetagger:
	def __init__(self):
		self.tagger = treetaggerwrapper.TreeTagger(TAGLANG='de',TAGDIR=configuration.getAttribute('tagdir'))
	def tagText(self,text):
		tags = self.tagger.TagText(text)
		tagsarray = [t.split('\t') for t in tags]
		return tagsarray

treetag = treetagger()