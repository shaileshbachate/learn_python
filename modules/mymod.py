def add(x, y):
    return x+y
    
def subtract(x, y):
    return x-y

person = {
    "name": "Shailesh",
    "age": 22,
    "roll": 103
}


class Developer():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def fullname(self):
        return self.fname + ' ' + self.lname
