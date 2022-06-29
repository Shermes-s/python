# urunler = ["iphone 12", "samsung s22", "iphone 13","iphone 13 pro"]

# # for urun in urunler:
# #     if urun.startswith('i'):
# #         print(urun)

# adet = 0

# for urun in urunler:
#     if urun.find('iphone') > -1:
#         print(urun)
#         adet += 1

# print(adet)

# fiyatlar = [8000, 10000, 13000, 17000]

# for fiyat in fiyatlar:
#     if fiyat >= 10000:
#         print(fiyat)



# telefonlar = [
#     {"urun_ad":"iphone 8","fiyat": 4000},
#     {"urun_ad":"iphone x","fiyat": 6000},
#     {"urun_ad":"iphone 12","fiyat": 8000},
#     {"urun_ad":"iphone 13","fiyat": 14000},
#     {"urun_ad":"iphone 13 pro","fiyat": 24000},
# ]

# toplam = 0

# for telefon in telefonlar:
#     toplam += telefon["fiyat"]
#     print(toplam)

# for telefon in telefonlar:
#     if telefon["fiyat"] > 8000:
#         print(telefon["urun_ad"])




# sayilar = [1,3,6,8,9]

# i = 0
# toplam = 0
# while i <= 50:
#     toplam += i
#     i += 1
# #     print(toplam)

# i = 0
# while i < len(sayilar):
#     print(sayilar[i])
#     i += 1 


# adet = int(input('Kaç adet ürün eklemek istersiniz? '))
# urunler = []

# i = 0

# while i < adet:
#     urunAdi = input("Ürün adı: ")
#     fiyat = float(input("fiyat: "))
#     urunler.append({
#         "urunadi": urunAdi,
#         "fiyat": fiyat
#     })
#     i+=1

# for urun in urunler:
#     print(f'Ürün adı: {urun["urunadi"]} {urun["fiyat"]}')



# sayilar = [1,3,6,8,9]

# for i in range(1, 100, 2):
#     sayilar.append(i)

# print(sayilar)

# list comprehension

# sayilar2 = [i+i for i in range(1, 100)]
# isim = 'Caner'

# sonuc = [i.upper() for i in isim]

# print(sayilar2)
# print(sonuc)

sayilar = [1,5,7,8,34]
sonuc = []

# for sayi in sayilar:
#     if sayi % 2 == 0:
#         sonuc.append(sayi)

# sonuc = [sayi for sayi in sayilar if sayi % 2 == 0]
# # sonuc = [sayi if sayi % 2 == 0 else "tek sayi" for sayi in sayilar]
# sonuc = ["çift sayi" if sayi % 2 == 0 else "tek sayi" for sayi in sayilar]

# print(sonuc)


fiyatlar = [2000, 5000, 8000, 0, 7000]
vergiler = []

# for fiyat in fiyatlar:
#     if fiyat > 0:
#         vergiler.append(fiyat*1.18)



vergiler = [fiyat*1.18 for fiyat in fiyatlar if fiyat > 0]

print(vergiler)