with open('./forras6.txt' , 'r' , encoding='utf-8') as adatfolyam:
    tartalom = adatfolyam.read()
    
szöveglista = list(map(str, tartalom.strip(" ").split(" ")))

szöveglista = [szó.strip(".,") for szó in szöveglista] # eltávplítja a szó végéről és elejéről 

szöveglista = [szó.rstrip(".,") for szó in szöveglista] #a rear strip csak a végéről törli



#print(szamok)

for szó in szöveglista:
    print(szó)
    
print(f"A szavak száma a szövegben{len(szöveglista)}")

# hány (a) betűs szó van a listában

a_betus_szavak = []
for szó in szöveglista:
    if szó[0] == "a" or szó[0] == "A":
        a_betus_szavak.append(szó)
        
print(f"(a) betüvel kezdődő szavak listája: {a_betus_szavak}")


#1
bcd_betus_szavak = []
for szó in szöveglista:
    if szó[0] == "b" or szó[0] == "B":
        bcd_betus_szavak.append(szó)
    if szó[0] == "c" or szó[0] == "C":
        bcd_betus_szavak.append(szó)
    if szó[0] == "d" or szó[0] == "d":
        bcd_betus_szavak.append(szó)
        
print(f"a,b,c,d betus szavak: { bcd_betus_szavak}")
 
k_betus_szavak = []
  
#2
k_lista = []
for x in szöveglista:
    if x[-1] == "n":
        k_lista.append(x)
  
print(f"ennyi kra vegzodo suo van : {k_lista}")
#3     
for szó in szöveglista:
    if szó[0] == "k" or szó[0] == "K":
        k_betus_szavak.append(szó)
        
print(f"ennyi k betus szo van : {len(k_betus_szavak)}")

#4
lo = 0

for x in szöveglista:
    if "lo" in x :
        lo += 1
     
     
print(lo)   
#5

harom = []

for x in szöveglista:
    if len(x) == 3 :
        harom.append(x)
    

with open('kimenet5.txt' ,'w' , encoding='utf-8') as adatfolyam:
        print(harom , file=adatfolyam)    


    
