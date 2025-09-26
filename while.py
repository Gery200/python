#A
szamlalo = 0
while szamlalo < 10:
    print(f"lépés")
    szamlalo += 1  #fontos mert a kezoerteket irjuk felul és ezt nézi a ciklus
    
#B
szamlalo = 1
while szamlalo <= 10:
    print(f"{szamlalo}. lépés")
    szamlalo += 1
    
#eloltesztelo ciklus esetén nem biztos hogy egyszer is le kell fusson 
szamlalo = 1
while szamlalo > 10:
    print(f"{szamlalo}. lépés")
    szamlalo += 1