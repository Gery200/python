import random

veleteln_szam = random.randint(-300 , 300)

print(f"A sorsolt szám: {veleteln_szam}")   


if veleteln_szam % 3 == 0:
    print(f"ez a szám osztahto 3-mal \n"
          f"Az eredmény {veleteln_szam / 3}")