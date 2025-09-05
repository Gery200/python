import math

a = int(input("Kérek egy számot: "))
b = int(input("Kérek egy másik számot: "))

hatvany = math.pow(a, b)

gyok = math.sqrt(a)

print(f"hatvány: {hatvany: .2f}\n"
      f"a szám gyöke kerekítve: {math.ceil(gyok)}\n"
      f"A szám gyöke: {gyok}\n"
      f"az (a) szám tipusa {type(a)}\n"
      f"a (b) szám tipusa {type(b)}\n"
      f"a hatvány tipusa :{type(gyok)}\n"
      f"a gyök tipusa: {type(gyok)}\n")


