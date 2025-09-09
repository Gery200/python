szam_1 = int(input("Kérem az első számot: "))
szam_2 = int(input("Kéreem a második számot: "))


ossz = szam_1 + szam_2
kiv = szam_1 - szam_2
hany = szam_1 / szam_2
szor = szam_1 * szam_2
mar = szam_1 % szam_2

print(f"a két szám összege: {ossz} \n"
      f"a két szám különbsége: {kiv} \n"
      f"a két szám hányadosa: {hany} \n"
      f"a két szám szorzata:{szor}")


if mar == 0:
    print(f"ennek a szának nincs maradéka")
elif mar < 5:
    print(f"a maradék kevesebb mint 5")
else:
    print(f"A maradék több mint 5 ")