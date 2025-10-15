import random


szamlista = [1,2,3,4,5,6,7,8,9,10]
szamlista2 = []
osztahto2 = []
nemoszt2 = []
oszt3 = []

for x in szamlista:
    if x % 2 == 0:
        osztahto2.append(x)

print(f"ezek a szamok osztatoak 2-vel: {osztahto2}")

##############################################################

szamlista.sort(reverse=True)


print(f" vissza fele:{szamlista}")

####################################################################

for x in szamlista:
    if x % 2 != 0:
        nemoszt2.append(x)
        
nemoszt2.sort(reverse=True)
print(f"a paratlan szamok visszafele 1 és 10 kozott: {nemoszt2}")

#########################################################################

word = str(input("kérem az adott szöveget: "))
word1 = True

while word1:
    print(f"a megadott szoveg: {word}")
    kéréds = str(input(f"ki irjam mégeszer (i/n):"))
    if kéréds == 'n':
        word1 = False
        print(f"a program vége")
        
##################################################################################

paros = int(input("kérek egy páros számot"))
paros1 = True

while paros1:
    if paros % 2 == 0:
        print(f"a megadot szam: {paros}")
        paros1 = False
    else:
        print(f"ez a szám nem páros")
        paros = int(input("kérek egy páros számot"))
        
######################################################################################

for x in range(20):
    szamlista2.append(random.randint(1,12))

for x in szamlista2:
    if x % 3 == 0 :
        oszt3.append(x)

print(f"ezek a 3-mal osztahto szamok {oszt3} \n"
      f"összesen {len(oszt3)} 3-mal osztahto szam volt ")