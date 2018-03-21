import os
from subprocess import *

def multiScriptHandler(x):
    p = Popen([x, "ArcView"], shell=True, stdin=PIPE, stdout=PIPE)
    output = p.communicate()
    print output[0]
i = 1
while i <30000:
    multiScriptHandler(r'writeToDb.py')
    multiScriptHandler(r'writeToDb.py')
    multiScriptHandler(r'writeToDb.py')
    multiScriptHandler(r'writeToDb.py')
    multiScriptHandler(r'writeToDb.py')
    multiScriptHandler(r'writeToDb.py')
    multiScriptHandler(r'writeToDb.py')
    multiScriptHandler(r'writeToDb.py')
    multiScriptHandler(r'writeToDb.py')
    multiScriptHandler(r'writeToDb.py')
    print "Iterationslevel: " + str(i)
    i=i+1