import os
from subprocess import *

def multiScriptHandler(x,json):
    p = Popen([x, "ArcView"], shell=True, stdin=PIPE, stdout=PIPE)
    output = p.communicate()
    print output[0]
i = 1

while i <12:
    with io.open(dateiname, encoding="utf-8") as json_file:
    self.json = (json.load(json_file))[i]
    multiScriptHandler(r'findnutr.py,',json)
    print "Iterationslevel: " + str(i)
    i=i+1