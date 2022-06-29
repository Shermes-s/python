urunAdi = "elma"
fiyat = 15
miktar = 2.5

# sonuc = str(miktar) + " kg " + urunAdi + " için ödemeniz gereken ücret " + str(fiyat * miktar) + " TL."

# format

# sonuc =  "{} kg {} için ödemeniz gereken ücret {} TL.".format(miktar, urunAdi, (fiyat * miktar))
# sonuc =  "{0} kg {1}{1} için ödemeniz gereken ücret {2} TL.".format(miktar, urunAdi, (fiyat * miktar))
# sonuc =  "{m} kg {u}{u} için ödemeniz gereken ücret {t} TL.".format(m = miktar, u = urunAdi, t = (fiyat * miktar))

# f-string

sonuc = f"{miktar} kg {urunAdi} için ödemeniz gereken ücret {(miktar * fiyat)} TL."

print(sonuc)