szam_1 = int(input("Kérem az első számot: "))
szam_2 = int(input("kérem a második számot: "))

if szam_1 > 143:
    print(f"Túl nagy a szám")
elif szam_1 < 0:
    print(f"a szám nem lehet minusz")

if szam_2 > 143:
    print(f"Túl nagy a szám")
elif szam_2 < 0:
    print(f"a szám nem lehet minusz")
else:
    hatvany = szam_1 ** szam_1
    hatvany_2 = szam_2 ** szam_2

hatvany = szam_1 ** szam_1
hatvany_2 = szam_2 ** szam_2




print(f"az első szám önmagára emelt hatványa: {hatvany} \n"
      f"a második szám önmagára emelt hatványa: {hatvany_2} \n"
      f"az első szám {len(str((hatvany)))} számjegyből áll \n"
      f"a második szám {len(str((hatvany_2)))} számjegyből áll \n"
      f"A számjegyek száma osztva a számmal: {hatvany / len(str((hatvany))) }")