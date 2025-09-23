import random

szam_1 = random.randint(1,3)
szam_2 = random.randint(2,4)

eredmeny = szam_1 == szam_2

if eredmeny == True:
    print(f"A két szám egyenlő! \n"
          f"Az első szám: {szam_1} \n"
          f"a második szám: {szam_2}")
else:
    print(f"a két szám nem egyenlő!")