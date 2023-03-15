import random
Dizi = []
for i in range(100):
   Dizi.append(random.randint(0,100))

def sirala(Dizi):
   
    for i in range(len(Dizi)):
        for j in range(0, len(Dizi)-i-1):
            if Dizi[j] > Dizi[j+1]:
                Dizi[j], Dizi[j+1] = Dizi[j+1], Dizi[j]
    return Dizi

print(sirala(Dizi))