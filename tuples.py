_list = [3,5,7]
_tuple = (1,3,6,7)
_tuple2 = (1,7)

print(type(_list))
print(type(_tuple))

# tuple ==> sıralanabilir, değiştirilemez, tekrarlanabilir.

sonuc = _tuple[0]
sonuc = len(_tuple)
sonuc = len(_list)

_list[0] = 10
# _tuple[0] = 10 hata verir

_list.append(10)
# _tuple.append(10) hata verir

sonuc = _tuple + _tuple2
sonuc = _tuple + tuple(_list)

_tuple3 = 10,20,30

print(type(_tuple3))
print(_tuple3)