import random
Dizi = []
for i in range(1000):
   Dizi.append(random.randint(0,100000))

def en_buyuk_sayi(Dizi):
    en_buyuk = Dizi[0]
    for i in range(1, len(Dizi)):
        if Dizi[i] > en_buyuk:
            en_buyuk = Dizi[i]
    return en_buyuk

print(Dizi)
print(en_buyuk_sayi(Dizi))
