import random

def sorsol(hány: int, mettől:int, meddig:int) -> list:
    lista = []
    for _ in range(hány):
        lista.append(random.randint(mettől, meddig))
    return lista
    
számlista = sorsol(5, 1, 90)
#számlista2 = sorsol(100, 1, 300)

print(f"A lista elemei: {számlista}")
#print(f"-   -   -")
#print(f"A számlista2 lista elemei: {számlista2}")