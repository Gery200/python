import random
szamlista = []

for x in range (100):
    szamlista.append(random.randint(0 , 500))

'''szamlista.sort() # növekvő lista (A számlistát is rendezi)
print(f"Elemek: {szamlista}")
szamlista.sort(reverse=True) # csökkenő lista
print(f"Elemek: {szamlista}")
'''

#szétválogatás lista bejárással
harommal = []
ottel = []
hettel = []
kilenccel = []
tizel = []

#a másik lehetőség lenne 5 bejárás 5 vizsgálattal (erőforrásigényesebb ,de muködne)
for x in szamlista: # végig megyunk mindegyik elemen és megvizsgáljuk őket 
    if x % 3 == 0:
        harommal.append(x)
    if x % 5 == 0:
        ottel.append(x)
    if x % 7 == 0:
        hettel.append(x)
    if x % 9 == 0:
        kilenccel.append(x)
    if x % 10 == 0:
        tizel.append(x)
      
print(f"Hárommal osztahto szamok: {harommal} \n"
      f"ottel osztahto szamok: {ottel} \n"
      f"hettel osztahto szamok: {hettel} \n"
      f"kilencce osztato szamok: {kilenccel} \n"
      f"tizzel osztahto szamok: {tizel} \n")