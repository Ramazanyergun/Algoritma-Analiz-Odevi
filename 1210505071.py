import random
Dizi = []
for i in range(1000):
    Dizi.append(random.randint(0,100000))

def merge(Dizi):
    if len(Dizi) > 1:
        orta = len(Dizi) // 2
        solDizi = Dizi[:orta]
        sagDizi = Dizi[orta:]

        merge(solDizi)
        merge(sagDizi)
        mergeSort(Dizi,sagDizi,solDizi)

def mergeSort(Dizi,solDizi,sagDizi):
    i = 0
    j = 0
    k = 0
    while i < len(solDizi) and j < len(sagDizi):
        if solDizi[i] < sagDizi[j]:
            Dizi[k] = solDizi[i]
            i = i + 1
        else:
            Dizi[k] = sagDizi[j]
            j = j + 1
        k = k + 1
    while i < len(solDizi):
        Dizi[k] = solDizi[i]
        i = i + 1
        k = k + 1
    while j < len(sagDizi):
        Dizi[k] = sagDizi[j]
        j = j + 1
        k = k + 1
        
merge(Dizi)
print(Dizi)