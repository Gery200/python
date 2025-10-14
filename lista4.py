#modoluk meghivasa
import random

# lista létrehozása
szamlista = []
szamlista2 = [3,5,6,7,89]
szoveglista  = ["alma" , "korte" , "Cinege"]

# lista feltoltese random szamokkal
for x in range(1000): # hany elmet sorsolok
    szamlista.append(random.randint(0 , 1000)) # 0 és 1000 között sorsolok random szamokat(0 és 1000 is benne van )

szamlista.sort()


'''
# 1 elem vagy intervallum lekérése
print(f"{szamlista}") # komplett lista kiirása
print(f"{szamlista[67]}") # indexu elem kiirasa
print(f"{szamlista[5:12]}") #az 5 és a 12 elem kozotti rész kiírása
print(f"{szamlista[:5]}") # elso 5 elem kiírása
print(f"{szamlista[5:]}") # az 5-dik elem után lévő elemek kiírása
print(f"{szamlista[-1]}") # mindenkori utolso elem kiírása
# ez bármilyen művelteben fehasználható 
# itt nem történik bejárás 


# lista metódusai(bejárás neélkülikek)
szamlista.append() # lista végére szúr be ey elemet
szamlista.insert() # a lista megadott indexére szur be egy elemet , a lista utána lévő elemeinke indexei növekszik egyet 
szoveglista.pop() # alapértelmetés szerint a lista végéről eltünteti a mindekori utoso 
szamlista.remove() # a megadott elemet tünteti el (csak az első találatot) 
szamlista.clear() # a lista megmarad de a tartalamat üríti 
szamlista.sort() # növekvő sorrenbe rendezés
szamlista.reverse() # csökkenő sorrendbe rendezés(reverse=True)
szamlista.copy() # egy új listába másolja a  lisza tartalmát 
# ezek mindegyike at kiinduló listát módosítja


# lista bejárása 
# A megoldás (for - ciklusa) - kézenekvőbb
# minden elemen elvégzi ugyanazt a műveletet (indexxel nem kell foglalkozni)
for x in szamlista: 
    print(x ) # kiírja az indexszen lévő elemet 

# B emgoldás (while) - itt az indexszet neked kell kezelni , ha nem elmeld az index értékét és a feltétel igaz , akkor végtelen ciklus , azaz rossz feltétel megadás esetén egyszer sem, fut le 
index = 0 
while index < len(szamlista):
    print(szamlista[index])
    index +1 # ha ez nincs itt akkor végtelen ciklus 
    
'''
    
# # # # # 
# feladat: szétválogatás 
tizzel = []  
nem_o_tizzel = []


for x in szamlista: 
    if x %10 ==  0: 
        tizzel.append(x)
    else:
        nem_o_tizzel.append(x)
        
print(f"tízzel osztahtó: {tizzel}")

