# encoding=utf8

import json
import io
from pprint import pprint
from findnutr import *


class CompileJsons:
    
    def __init__(self):
    
        self.resultJson = []
        self.__calcualteNutr()
        
    def __calcualteNutr(self):
        with io.open(r"../../json/rec_10recipes.json", encoding="utf-8") as json_file:
            self.jsonFile = json.load(json_file)
            for jsonData in self.jsonFile:
                rezept = Rezept(jsonData)
                self.resultJson.append(rezept.returnJson())
                
        self.resultFile=json.dumps(self.resultJson, ensure_ascii=False, encoding='utf-8')
        with io.open("test.json","w",encoding="utf-8") as resultFile:
            resultFile.write(self.resultFile)
           
compileJsons=CompileJsons()