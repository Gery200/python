import random

szamlista = []
ketto = []


for _ in range(5):
    szamlista.append(random.randint(0, 100))

for x in szamlista:
    if x % 2 == 0 : 
        ketto.append(x)





with open('kiement5.txt' , 'a' , encoding='utf-8') as adatfolyam:
    print(f" \n A sorsolt szamok listaja: {szamlista} "
          f" \n A kettővel osztahtó számok listaja: {ketto}" , file=adatfolyam)
