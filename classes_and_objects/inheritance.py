class Base:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_legal(self):
        return self.age > 18

    def print_data(self):
        print(self.name, self.age)


class Derived(Base):
    def __init__(self, name, age, dept):
        super().__init__(name, age)
        self.dept = dept

    def print_data(self):
        print(self.name, self.age, self.dept)


class Derived2(Base):
    def __init__(self, name, age, dept):
        Base.__init__(self, name, age)
        self.dept = dept

    def print_data(self):
        print(self.name, self.age, self.dept)

    def is_legal(self):
        return self.age > 25


s1 = Base('Shailesh', 22)
s1.print_data()
print(s1.is_legal())

s2 = Derived("Shubham", 22, "QQQ")
s2.print_data()
print(s2.is_legal())

s3 = Derived2("Chetan", 23, "WWW")
s3.print_data()
print(s3.is_legal())
print("------------------------------------------------------------------------")

print(f'isinstance(s3, Base)        =>  {isinstance(s3, Base)}')
print(f'isinstance(s3, Derived)     =>  {isinstance(s3, Derived)}')
print(f'isinstance(s3, Derived2)    =>  {isinstance(s3, Derived2)}')
print(f'issubclass(Derived, Base)   =>  {issubclass(Derived, Base)}')
print(f'issubclass(Base, Base)      =>  {issubclass(Base, Base)}')
