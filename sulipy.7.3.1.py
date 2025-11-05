import random

szamlista = []
paros = []


for x in range(5):
    szamlista.append(random.randint(1,10))
    


for x in szamlista:
    if x % 2 == 0 :
        paros.append(x)
    
print(f"a lista elemei:{szamlista}\n")
print(f"a lisrtaban a párps számok: {paros}")