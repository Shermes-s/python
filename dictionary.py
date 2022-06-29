# key : value

# 34 => İstanbul
# 53 => Rize

sehirler = ["İstanbul","Rize"]
plakalar = ["34","53"]

print(plakalar[0], sehirler[0])
print(plakalar[1], sehirler[1])

print(plakalar[sehirler.index("İstanbul")])

plakalar2 = {
    'İstanbul' : 34,
    'Rize' : 53,
    'Kocaeli' : 41
}

plakalar3 = {
    34 : 'İstanbul',
    53 : 'Rize',
    41 : 'Kocaeli'
}

print(plakalar2["İstanbul"])
print(plakalar3[41])

rehber = {
    "Caner Aylan" : ["123456789","345678912"],
    "Bengin Aygün" : {
        "ev" : "234567891",
        "iş" : "456789123",
        "cep" : "567891234",
        "adres" : {
            "mahalle" : "gülsuyu",
            "cadde" : "eski üsküdar",
            "no" : 49,
            "şehir" : "istanbul"
        }
    }
}

print(rehber["Caner Aylan"][0])
print(rehber["Bengin Aygün"]["cep"])
print(rehber["Bengin Aygün"]["adres"]["cadde"])