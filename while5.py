import random
lista = []
index = 0 

for x in range(200):
     lista.append(random.randint(0,20))
     

lista.sort()
print(f"kezdeti lista: {lista}")

    
#lista.pop() #mindenkori utolso elem eltuntetése
eltávolítando = lista[0]
lista.remove(eltávolítando) # elso találatnál eltávolítja az elemet , ismétlésnél nem csinál semmit

print(f"átalakított lista: {lista}")
     
     
"""print(lista [10:20], end=" \n ")
print(f"elemek osszege: {sum(lista[1:30])}")
"""

lista.clear() # torli a lista tartalmat 
lista.insert() # a megadott index helyére rakja be az elemet, a többit hátra tolja
lista.count()# egy szám hányszor fordul elo