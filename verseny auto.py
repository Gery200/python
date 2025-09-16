import random

verseny_1 = random.randint(1 , 10)
verseny_2 = random.randint(1 , 10)

print(f"az első auto sebessege: {verseny_1} \n"
      f" A második auto sebessége: {verseny_2} \n")


if verseny_1 > verseny_2:
    print(f"\taz elso auto nyerte a versenyt !")
elif verseny_1 < verseny_2:
    print(f"\tA második auto nyerte a versenyt !")
else:
    print(f"\tugyan olyan gyorsak")
    