# Inheritance (Kalıtım): Miras alma

# Person => name, lastname, age, eat(), run(), drink()
# Student(Person), Teacher(Person)

# Animal >> Dog(Animal), Cat(Animal)


class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('Person Created')

    def who_am_i(self):
        print('I am a person')

    def eat(self):
        print('I am eating')

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.StudentNumber = number
        print('Student Created')

    def who_am_i(self):
        print('I am a student')

    def sayHello(self):
        print('Hello I am a student')

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch

    def who_am_i(self):
        print(f'I am a {self.branch} teacher')

p1 = Person('Caner', 'Aylan')
s1 = Student('Hilal', 'Gül', 258)
t1 = Teacher('Aysun', 'Aylan', 'Math')

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName + ' ' + str(s1.StudentNumber))

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()

p1.eat()
s1.eat()

s1.sayHello()