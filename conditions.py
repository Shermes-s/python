# sayi1 = 30
# sayi2 = 30

# if(sayi1 > sayi2):
#     print("sayi1 sayi2 den büyük")
# elif(sayi1 == sayi2):
#     print("sayi ve sayi2 eşit")
# else:
#     print("sayi1 sayi2 den küçük")

# username = "shermes"
# password = "12345"

# if(username == "shermes"):
#     if(password == "12345"):
#         print("uygulmaya giriş yapıldı.")
#     else:
#         print("parola yanlış")
# else:
#     print("username yanlış")


vize1 = float(input("Vize 1: "))
vize2 = float(input("Vize 2: "))
final = float(input("Final: "))

ortalama = ((vize1 + vize2) / 2) * 0.4 + (final * 0.6)

# sonuc = ortalama >= 50 and final >= 50

print(ortalama)

if(ortalama):
    print("geçtiniz")
else:
    if(final >= 70):
        print("final notu geçtiniz")
    else:
        print("kaldınız")