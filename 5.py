import math


szam = int(input("Kérek egy számot: "))

hatvany = szam  ** 2
gyok = int(math.sqrt(szam)) 

print(f"A szám hatványa: {hatvany}")
print(f"A szám gyöke: {gyok: .2f}")