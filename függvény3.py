

import random
import math

szám = int(6)
sin = math.sin(szám)

szam2 = int(8)
cos = math.cos(szam2)

print(f"A szám sinusa:{sin}.2f")
print(f"A szám Cosinusa:{cos}.2f")
print(f"A függvény tangense:{math.tan(szam2):.2f}")
print(f"A fuggvény {math.floor(2.6)}") # az alatt levő első egész szám
print(f"A fuggvény {math.ceil(2.6)}") # a felett levő elso egész szám
print(f"A pi értéke:{math.pi}")
print(f"{math.pow(2, 4)}") # matematikai függvénnyel való megoldás
print(f"{4**2}")

szamlista = []


    

#print(f"{szamlista}")

kerekítettlista = []
for x in szamlista:
    kerekítettlista.append(round(x , 2))

print(F"{kerekítettlista}")


masodidhatvany = []
for x in szamlista:
    masodidhatvany.append(pow(x , 2))
    
    
masodidhatvany.sort(reverse=True)
print(f"masodik hatvany {masodidhatvany}")


lefele = []
felfele = []

for x in szamlista:
    lefele.append(math.floor(x))

print(f"{lefele}")


for x in szamlista:
    felfele.append(math.ceil(x))
    
print(f"{felfele}")


for x in range (500):
    szamlista.append(round(random.random()))
    
print(f"{szamlista}")


szamolo1 = []
szamolo2 = [] 


db = 0 
for i in range(len (szamlista) -2):
    if szamlista[i] == 1 and szamlista[i+1] == 1 and szamlista[i+2]==1:
        db +=1
        
print(f"az 111 minta elofudulasainka szama :" ,db)
    
    

    