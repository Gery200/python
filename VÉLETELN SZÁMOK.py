import random

jatekos_1_dsz = random.randint(1 , 6)
jatekos_2_dsz = random.randint(1 , 6)

print(f"eslő játékos által dobott szám: {jatekos_1_dsz} \n"
        f"A második játékos által dobott szám: {jatekos_2_dsz}")


if jatekos_1_dsz > jatekos_2_dsz:
    print("Az első játékos nyert! \n")
elif jatekos_1_dsz < jatekos_2_dsz:
    print("A második játékos nyert! \n")
elif jatekos_1_dsz == jatekos_2_dsz:
    print(f"Dönteteln")