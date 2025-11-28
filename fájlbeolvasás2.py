with open('forrasa.txt' , 'r' , encoding='utf-8') as adatfolyam:
    tartalom = adatfolyam.read()
    
szöveglista = list(map(str, tartalom.split(" ")))

#print(szamok)

for szó in szöveglista:
    print(szó)
    
print(f"A szavak száma a szövegben{len(szöveglista)}")