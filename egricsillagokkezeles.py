with open('./forras2.txt' , 'r' , encoding='utf-8') as adatfolyam:
    tartalom = adatfolyam.read()
    
szöveglista = list(map(str, tartalom.strip().split(" ")))

szöveglista = [szó.strip(".,") for szó in szöveglista] # eltávplítja a szó végéről és elejéről 

szöveglista = [szó.rstrip(".,") for szó in szöveglista] #a rear strip csak a végéről törli

for szó in szöveglista:
    print(szó)
    
print(f"A szavak száma a szövegben: {len(szöveglista)}")