msg = "sıfırdan ileri seviye python programlama kursu. ben caner aylan"

sonuc = msg.upper()
sonuc = msg.lower()
sonuc = msg.title()
sonuc = msg.capitalize()

sonuc = msg.upper().isupper()
sonuc = "  deneme   ".strip()
sonuc = msg.split('.')

sonuc = msg.index('python')
sonuc = msg.startswith('sıfırdan')
sonuc = msg.endswith('aylan')

sonuc = msg.replace('caner','ercan')
sonuc = msg.lower().replace(' ','-').replace('.','').replace('ı','i')+'.html'

sonuc = 'abcd'.isalpha()
sonuc = '1abcd'.isalpha()

sonuc = '123'.isdigit()
sonuc = '123a'.isdigit()



print(sonuc)