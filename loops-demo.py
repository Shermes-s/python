import random

x = random.randint(1,10)
can = int(input('kaç hak kullanmak istersinz: '))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input('Tahmin: '))
    if x == tahmin:
        print(f'Tebrikler {sayac}. tahminde bildiniz. Toplam puanınız: {100 - (100 / can) * (sayac-1)}')
        break
    elif x > tahmin:
        print('yukarı')
    else:
        print('aşağı')
    if hak == 0:
        print(f'hakkınız bitti. Tutulan sayı: {x}')
