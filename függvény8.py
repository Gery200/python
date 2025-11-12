import random

def sorsol(lista) -> list:
    hány = int(input(f"hány számot sorsoljak ki ?"))
    mettol = int(input("Mettől sorsoljak"))
    meddig = int(input("Meddig sorsoljak"))
    lista = []
    for x in range(hány):
        lista.append(random.randint(mettol, meddig))
    return lista
    
számlista = sorsol()
print(f"A lista elemei: {számlista}")
