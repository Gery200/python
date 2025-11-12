import random

def sorsol(hány = int(6) , mettől = int(1), meddig = int(45)) -> list:
    lista = []
    for _ in range(hány):
        lista.append(random.randint(mettől, meddig))
        lista.sort()
    return lista

for x in range(1):   
    számlista = sorsol()
    print(f"{x+1}.hét nyero szamai: {számlista}")


# szétválogatás



def valogatas( paros  , paratlan , grander):
    paros = []
    paratlan = []
    grander = []
    for i in range(20):
        grander.append()
    for x in számlista:
        if x % 2 == 0 :
            paros.append(x)
        else:
            paratlan.append(x)
        
        
szlista = valogatas
print(f"2vel osztahto szamok: {szlista}")