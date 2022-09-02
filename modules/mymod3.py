import math

def myfloor(x):
    return math.floor(x)

def myceil(x):
    return math.ceil(x)

class Employee():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def fullname(self):
        return self.fname + ' ' + self.lname

