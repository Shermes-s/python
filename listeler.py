isimler = ["Caner","Ali","Deniz"]

print(isimler[1])

# list, tuple, set, dictionary

# list ==> sıralanabilir, değiştirilebilir, tekrarlanabilir.

notlar = [70, 80, 50]

print(f"{isimler[0]} isimli öğrencinin notu: {notlar[0]}")

ogrenci1 = ["Caner", 70]
ogrenci2 = ["Ali", 80]
ogrenci3 = ["Deniz", 50]

# nesned list ==> iç içe liste
ogrenciler = [
    ["Caner", 70],
    ["Ali", 80],
    ["Deniz", 50]
]

print(f"{ogrenciler[0][0]} isimli öğrencinin notu: {ogrenciler[0][1]}")

markalar = ["opel","mazda","toyota","bmw","bmw"]

sonuc = markalar[:3]
sonuc = markalar[0:3]
sonuc = markalar[1:3]
sonuc = markalar[1:]
sonuc = markalar[::-1]

markalar[0] = "renault"
markalar[-1] = "mercedes"

markalar[0:2] = ["citroen","audi","honda"]

print(markalar)

# urunler 
# fiyatlar

urunler = [
    [],
    []
]