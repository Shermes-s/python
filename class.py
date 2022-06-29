# # class

# class Person:
#     # class attributes
#     address = 'no information'
#     #contrustor (yapıcı metod)
#     def __init__(self, name, year):
#         # object attributes
#         self.name = name
#         self.birthYear = year
#         print('init metodu çalıştı')

#     # instance methods
#     def intro(self):
#         print(f'Hello There. I am {self.name}')

#     def calculateAge(self):
#         return 2019 - self.birthYear

# # object (instance)
# p1 = Person(name = 'Caner', year = 1999)
# p2 = Person(name = 'Aylan', year = 1999)

# #updating
# # p1.name = 'Ahmet'
# # p1.address = 'İstanbul'
# p1.intro()
# print(p1.calculateAge())
# p2.intro()
# print(p2.calculateAge())

# # accessing object attributes
# print(f'P1 : name: {p1.name} year: {p1.birthYear} address: {p1.address}')
# print(f'P2 : name: {p2.name} year: {p2.birthYear} address: {p2.address}')

# print(p1)
# print(p2)



class Circle:
    # Class object attribute
    pi = 3.14

    def __init__(self, yaricap = 1):
        self.yaricap = yaricap

    # Methods
    def cevreHesapla(self):
        return 2 * self.pi * self.yaricap

    def alanHesapla(self):
        return self.pi * (self.yaricap**2)

c1 = Circle() # yaricap = 1
c2 = Circle(5)

print(f'c1 : alan = {c1.alanHesapla()} çecre = {c1.cevreHesapla()}')
print(f'c2 : alan = {c2.alanHesapla()} çecre = {c2.cevreHesapla()}')