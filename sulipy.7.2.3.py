szoveg = "janiarkeolotizmus"

bete = str(input("kérek egy betűt!: "))


if bete in szoveg:
    print(f"a szóban megvan ez a betü")
else:
    print(f"a Szóban nincs meg ez a betü")
    
print(f"az alap szó: {szoveg}")