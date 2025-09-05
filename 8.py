szam = int(input("Kérek egy számot: "))

if szam <= 500 and szam >= -500:
    print("a szám 500 vagy annál kisebb")
elif szam < -500:
    print("A szám kisebb, mint -500!")
else:
    print("A szám nagybb, mint 500")