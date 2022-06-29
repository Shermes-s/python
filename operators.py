# 1- Atama Operatörleri

# x = 10
# y = 20
# z = 30

# x,y,*z = 10,20,30,40

# x += 5 # x = x + 5
# x -= 5 # x = x - 5
# x *= 5 # x = x * 5
# x /= 5 # x = x / 5
# x //= 5 # x = x // 5
# x %= 5 # x = x % 5
# x **= 5 # x = x ** 5

# print(x,y,z)


# 2- Karşılaştırma Operatörleri




x,y,z = 6,10,20

email = "info@mcsdev.net"
password = "12345"

sonuc = (x == y) # False
sonuc = (z == y) # True
sonuc = (z != y) # False

isMail = (email == "info@mcsdev.net") # True
isPassword = (password == "12345") # True

sonuc = (x > y)
sonuc = (x <= y)

# print(sonuc)


# 3- Mantıksal Operatörler

# a- And

# print(isMail)
# print(isPassword)

# sonuc = isMail and isPassword
sonuc = (5 < x < 15) # durum1 = (x > 5) // durum2 = (x < 15) // sonuc = durum1 and durum2

# b- Or

# mezuniyet en az lise ve yaş en az 18 olmalı

mezuniyet = "lise"
yas = 20

sonuc = (mezuniyet == "lise" or mezuniyet == "önlisans" or mezuniyet == "lisans") and (yas >= 18)



# c- Not

sonuc = not(True)
sonuc = not(False)

# identity operatörü

a = [1,2,3]
b = a

print(a is not b)
print(1 in a)

meyveler = ["elma", "armut"]

print("muz" not in meyveler)


print(sonuc)