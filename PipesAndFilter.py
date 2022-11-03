import math
import numpy as geek

##############################################
##               PIPELINE                   ##
##############################################

class Pipeline:
    def __init__(self, input):
        self.filters = list()
        self.input = input
        self.interim = list()
        self.errors = list()
 
    def add(self, filter):
        self.filters.append(filter)
 
    def execute(self):
        print("Executing pipeline...")
        i = 0
        for filter in self.filters:
            self.input = filter(self.input)
            self.interim.append(round(self.input, 3))
            if math.isnan(self.input):
                self.errors.append(i)
            i = i + 1
        sink = self.input
        return round(sink, 3)
        

##############################################
##               FILTER                     ##
##############################################

def filter_double(input):
    return input * 2
 
def filter_halve(input):
    return input / 2

def filter_minus_one(input):
    return input * -1

def filter_square_root(input):
    return geek.sqrt(input) 
