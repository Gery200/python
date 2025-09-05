elso_szam = int(input("Kérem az első számot:"))
masodik_szam = int(input("Kérem a második számot:"))
harmadik_szam = int(input("Kérem a harmadik számot:"))

egyenlet = elso_szam * masodik_szam /(harmadik_szam*masodik_szam) - elso_szam / 45 +(harmadik_szam/masodik_szam)

print(f"Végösszeg: {egyenlet:.2f}")