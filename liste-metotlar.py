urunler = ["samsung s20","samsung s21","samsung s22"]
fiyatlar = [5000,4000,7000]

#ekleme

# urunler.append("iphone 11")
# urunler.insert(1, "iphone x")
# urunler.insert(-1, "iphone 12")
# urunler.insert(len(urunler), "iphone 13")

#silme

# urunler.remove("samsung s20")
# urunler.pop() # en sondakini siler
# urunler.pop(0) # parametreye göre siler

# del urunler[0]
# del urunler

#urunler.clear()

# urunler2 = urunler
# urunler3 = urunler.copy()
# urunler[0] = "değiştir"


#urunler.extend(urunler)

urunler4 = urunler + urunler + ["iphone 9"]

print(urunler)
print(urunler4)

#sırlama

sonuc = min(fiyatlar)
sonuc = max(fiyatlar)
sonuc = min(urunler)
sonuc = max(urunler)

fiyatlar.sort()
fiyatlar.reverse()
urunler.sort()


sonuc = urunler.count("samsung s20")
sonuc = urunler.index("samsung s22")

print(fiyatlar)
print(urunler)
print(sonuc)

# print(urunler2)
# print(urunler3)

isimler = []

isim = input("İsim: ")
isimler.append(isim)

isim = input("İsim: ")
isimler.append(isim)

isim = input("İsim: ")
isimler.append(isim)

print(isimler)