class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return self.first + '.' + self.last + '@email.com'
    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
emp_1.fullname = 'Jill Don'

print(emp_1.fullname)
print(emp_1.email)
print()


emp_1.first = 'Jack'
emp_1.last = 'Barber'

print(emp_1.fullname)
print(emp_1.email)
print()

del emp_1.fullname

print(emp_1.first) # None
print(emp_1.last)  # None