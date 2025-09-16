valtozo = int(input("Kérek egy adatot: "))


print(f"A változo tipusa :{type(valtozo)}")


if type (valtozo) == int or  type (valtozo) == float:
    print(f"ez egy egész szám")
    print(f" Hatványra emelve: {valtozo ** 2}")
elif type (valtozo) == str:
    print(f"a muvelet nem végezheto el ")
