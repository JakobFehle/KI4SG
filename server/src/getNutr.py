# encoding=utf8
import sys
from readprep import *

#rezept = Rezept(r'../raw/2.raw')

#print "Kcal: " + str(rezept.naehrwerte['GCAL'])
#print "Fett: " + str(rezept.naehrwerte['ZF'])
#print "Masse: " + str(rezept.menge) + " Gramm"

#rezept.zutatenanzeigen()


rezept = Rezept(r'../../../json/rec_10recipes.json')

print "Kcal: " + str(rezept.naehrwerte['GCAL'])
print "Fett: " + str(rezept.naehrwerte['ZF'])
print "Masse: " + str(rezept.menge) + " Gramm"



    