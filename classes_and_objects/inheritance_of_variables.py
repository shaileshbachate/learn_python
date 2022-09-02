class Test:
    def __init__(self):
        self.x = 0

class Derived_Test(Test):
    def __init__(self):
        self.y = 1


def main():
    b = Derived_Test()
    print(b.x,b.y)

main()  # AttributeError: 'Derived_Test' object has no attribute 'x'
# Error because class B inherits A but variable x isn’t inherited
# Explanation: Since the invoking method, Test.__init__(self), isn’t present in the derived class, variable x can’t be inherited.
