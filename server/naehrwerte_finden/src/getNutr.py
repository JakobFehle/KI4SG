# encoding=utf8
from readprep import *

#rezept = Rezept(r'../raw/2.raw')

#print "Kcal: " + str(rezept.naehrwerte['GCAL'])
#print "Fett: " + str(rezept.naehrwerte['ZF'])
#print "Masse: " + str(rezept.menge) + " Gramm"

#rezept.zutatenanzeigen()

rezept = Rezept1(r'../../../json/rec_1recipe.json')

print "Kcal: " + str(rezept.naehrwerte['GCAL'])
print "Fett: " + str(rezept.naehrwerte['ZF'])
print "Masse: " + str(rezept.menge) + " Gramm"

rezept.zutatenanzeigen()

