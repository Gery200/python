import random

szamlista = []

for x in range(5):
    szamlista.append(random.randint(1,10))
    
print(f"A szamlista elemeinke összege: {sum(szamlista)}")