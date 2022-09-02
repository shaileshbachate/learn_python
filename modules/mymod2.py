def multiply(x, y):
    return x*y

divide = lambda x, y: x/y

student = {'name': 'shailesh', 'roll': 103}


class Manager():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def fullname(self):
        return self.fname + ' ' + self.lname

