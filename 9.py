szam = int(input("Kérek egy számot: "))

if szam % 2 == 0:
    print(f"Az eredmény: {szam / 2}")
    print(f"ez a szám páros")
else:
    print(f"Az Reedmény: {szam / 2:.2f}")
    print(f"maradék: {szam % 2}")
    print(f"ez a szám páratlan")