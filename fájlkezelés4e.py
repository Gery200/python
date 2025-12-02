import random

számlista = []

for _ in range(1000):
    számlista.append(random.randint(1,10000))
    
számlista.sort()

kiirando = ";".join(map(str, számlista))

with open('kimenet3.txt' , 'w' , encoding='utf-8') as adatfolyam:
    print(kiirando)
    print(kiirando , file=adatfolyam)