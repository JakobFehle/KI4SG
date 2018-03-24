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
		u"ingredients_string" : u"3 Stk:Ei \n 180 g:Mehl \n 300 ml: Milch \n 100 g:Zucker",
	}

rezept = Rezept(testjson)
rezept.zutatenanzeigen()

print "Kcal: " + str(rezept.naehrwerte['GCAL'])
print "Fett: " + str(rezept.naehrwerte['ZF'])
print "Masse: " + str(rezept.menge) + " Gramm"



    