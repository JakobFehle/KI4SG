from readprep import *

rezept = Rezept(r'../raw/1.raw')

print "Kcal: " + str(rezept.naehrwerte['GCAL'])
print "Fett: " + str(rezept.naehrwerte['ZF'])
print "Masse: " + str(rezept.menge) + " Gramm"

#rezept.zutatenanzeigen()

