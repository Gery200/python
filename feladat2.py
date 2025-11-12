import random

lista = []

lista3 = []
lista5 = []
lista7 = []
maradek = []


kilepesi_pont = 0

while kilepesi_pont != 6667:
    kilepesi_pont = random.randint(1,6667) #bug
    print(f"A sorsolt számok: {kilepesi_pont}")
    lista.append(kilepesi_pont)
    
    if kilepesi_pont % 3 == 0 :
        lista3.append(kilepesi_pont)
    elif kilepesi_pont % 5 == 0 :
        lista5.append(kilepesi_pont)
    elif kilepesi_pont % 7 == 0:
        lista7.append(kilepesi_pont)
    else:
        maradek.append(kilepesi_pont)
    
<<<<<<< HEAD
=======
    
    print(f"A 3-mal osztahto oszthato szamok \n {lista3} \n"
          f"Az 5-el osztahto szamok \n {lista5} \n"
          f"A 7-el osztahto szamok \n {lista7} \n"
          f"a maradék számok \n {maradek}")
>>>>>>> 17a253e84a1f2026879a1e2295e4f987bd3f8810
