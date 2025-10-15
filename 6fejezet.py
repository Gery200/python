print(f"nyomjon entert ha mar nem akar tobb nevet megadni")
nev = str(input(f"kérem a neveket: "))
nev1 = True

nev2 = []

nev2.append(nev)

while nev1:
    nev = str(input(f"kérem a nevet"))
    if nev == "":
        print(f"a nevek {nev2}")