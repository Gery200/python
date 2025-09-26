import random

uj_szam_sorsol = True

while uj_szam_sorsol:
    print(f"szám: {random.randint(1, 200)}")
    kérdés =str(input("Sorsoljak még egy számot? (i/n)"))
    if kérdés == 'n':
        uj_szam_sorsol = False
print(">> Program vége <<")