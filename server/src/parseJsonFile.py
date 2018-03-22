# encoding=utf8

import json
import io
from pprint import pprint
from writeToDb import *
from findnutr import *


class CompileJsons:
    
    def __init__(self):
    
        self.resultJson = []
        self.__calcualteNutr()
        
    def __calcualteNutr(self):
        with io.open(r"../../json/final_recipe_0to30000.json", encoding="utf-8") as json_file:
            self.jsonFile = json.load(json_file)
            for jsonData in self.jsonFile:
                rezept = Rezept(jsonData)
                nutr = rezept.returnNutrArray()

                writeNuts(nutr[0],nutr[1],nutr[2],nutr[3],nutr[4],nutr[5],nutr[6],nutr[7],nutr[8],nutr[9],nutr[10],nutr[11],nutr[12],nutr[13],nutr[14],nutr[15],nutr[16],nutr[17],nutr[18],nutr[19],nutr[20])
           
compileJsons=CompileJsons()