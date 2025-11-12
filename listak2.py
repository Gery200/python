import random

szamlista = []

#lista feltoltese szamokkal

for x in range (5000):
    szamlista.append(random.randint(-500, 500)) #hozzáadás
    
#lista kiiratasa
#print(szamlista, sep="")


#lista bejarasa
for x in szamlista:
    print(x, sep="")
    
