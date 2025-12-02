szöveglista = []

#forrás beolvasása
with open('forras.txt' , 'r' , encoding='utf') as forrasfajl:
    szoveg =  forrasfajl.read() 
    szöveglista = list(map(str, szoveg.strip().split(' ')))

for szo in szöveglista:
    if szo[-1] == '.' or szo[-1] == ',':
        szo.rstrip('.,')
       
            
        
        
aszavak = []

for x in szöveglista:
    if x[0] == "a" or x[0] == "a": 
        aszavak.append(x)
        
with open('kement.txt' , 'a' , encoding="utf-8") as szavak:
             print(f"\n ezek az a betuvel kezdodo szavak: {aszavak}" , file=szavak)
        
#forrás beolvasása csak megjelenítéssel

for x in szöveglista:
    print(x)     