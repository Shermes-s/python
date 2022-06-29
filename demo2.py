r = float(input("Yarı çap bilgisi giriniz: "))
pi = 3.14
alan = pi * (r ** 2)
cevre = 2 * pi * r
result = "Alan: " + str(alan) + " - Çevre: " + str(cevre)
print(result)





km = float(input("KM Bilgisi giriniz: "))
mil = round(km / 1.609344,2)
print(mil)