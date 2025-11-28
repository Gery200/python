import random
számlista = []

for _ in range(100):
    számlista.append(random.randint(1, 100))

számlista.sort()

with open('kimenet2.txt' , 'a' , encoding='utf-8') as adatfolyam:
    print(f"{számlista}" , sep=",")
    print(f"{számlista}", sep="," ,  file=adatfolyam)