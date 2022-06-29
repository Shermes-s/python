from math import prod


p1 = {
    "name" : "samsung s20",
    "price" : 6000
}

# sonuc = p1["name"]
# sonuc = p1.get("price")
# sonuc = p1.keys()
# sonuc = p1.values()
sonuc = p1.items()

# p1["price"] = 7000

for x in p1.keys():
    print(x)

for x in p1.values():
    print(x)

for key,value in p1.items():
    print(key,value)

# p1["price"] = 7000
p1.update({
        "name" : "samsung s21",
        "price" : 7000,
        "description" : "iyi telefon"
})

p1["color"] = "red"
p1["color"] = "blue"

p1.pop("color")
p1.popitem()

# p1.clear()

# del p1 # tekrar kullanırsak hata verir

p2 = {
    "name" : "samsung s22",
    "price" : 8000
}
# p1 = p2
p1 = p2.copy()
p1["price"] = 9000

products = [p1,p2,{"name" : "samsung s23","price" : 8000}]

for p in products:
    for key,value in p.items():
        print(key,value)

print(products)