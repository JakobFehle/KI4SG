# encoding=utf8
import sys
from findnutr import *

#rezept = Rezept(r'../raw/2.raw')

#print "Kcal: " + str(rezept.naehrwerte['GCAL'])
#print "Fett: " + str(rezept.naehrwerte['ZF'])
#print "Masse: " + str(rezept.menge) + " Gramm"

#rezept.zutatenanzeigen()

testjson = {
		u"recipe_href" : u"/rezept/368835/broetchenteig-ohne-mehl.html",
		u"ingredients_string" : u"20000 g:Mehl",
	}

rezept = Rezept(testjson)
rezept.zutatenanzeigen()

print "Kcal: " + str(rezept.naehrwerte['GCAL'])
print "Fett: " + str(rezept.naehrwerte['ZF'])
print "Masse: " + str(rezept.menge) + " Gramm"

'''
Beispielzutat = Rezepteintrag(u"20000",u"g",u"Mehl")
if(Beispielzutat.besteZutat != ""):
    kalorien = Beispielzutat.besteZutat.naehrwerte['GCAL']
    print "Kcal: " + str(kalorien)
   ''' 

    