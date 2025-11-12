import random

def sorsol(hány = int(5) , mettől = int(1), meddig = int(90)) -> list:
    lista = []
    for _ in range(hány):
        lista.append(random.randint(mettől, meddig))
        lista.sort()
    return lista

for _ in range(52):   
    számlista = sorsol()
    print(f"Az 5os lotto nyero szamai: {számlista}")

