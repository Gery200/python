import random

szamlista = []

for x in range (5):
    szamlista.append(random.randint(1,7))


bekeres = int(input(f"mely számok szerepelhetnek a listában"))

if bekeres in szamlista:
    print(f"ez a szám szerepel a számlistában")
else:
    print(f"ez a szám nem szerepel a számlistában")
    
print(f"az alap számlista: {szamlista}")