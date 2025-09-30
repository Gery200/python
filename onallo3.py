import random

szam1 = int(input("adj meg egy kezdoerteket"))
szam2 = int(input("adj meg egy vegerteket"))

szamlista = []
osztok = []
osztahtosz =  []

for x in range ( szam1 , szam2):
    szamlista.append(random.randint(szam1 , szam2))

o1 = int(input("elso oszto: "))
o2 = int(input("masodik oszto: "))
o3 = int(input("harmadik oszto: "))
o4 = int(input("nefgyedik oszto: "))
o5 = int(input("otodik oszto: "))




for x in szamlista:
   if x % o1 == 0 :
      osztahtosz.append(x)
if x % o2 == 0 :
      osztahtosz.append(x)
      if x % o3 == 0:
          osztahtosz.append(x)
if x % o4 == 0:
    osztahtosz.append(x)

if x % o5 == 0:
    osztahtosz.append(x)



print(f"a generált számok: {szamlista} \n" )

osztahtosz.sort(reverse=True)    
print(f"ezeket a számokat lehet osztani: {osztahtosz}")