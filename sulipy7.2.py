import random

szamlista = []
paros = []

for x in range(5):
    szamlista.append(random.randint(1,10))
   
   
for x in szamlista:
        if  x % 2 == 0:
            paros.append(x) 
  
    
print(f"A szamlista elemeinke összege: {sum(paros)}")