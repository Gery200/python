import random 




def general (tól:int , ig:int , db = 6 ) -> list:
    nyeroszamok = []
    while len(nyeroszamok) < db:
        nyeroszam = random.randint(tól , ig)
        if nyeroszam in nyeroszamok:
            pass
        else:
            nyeroszamok.append(nyeroszam)

    nyeroszamok.sort()
    return nyeroszamok
        
# helytelen megkozelítés
    for x in range(db):
        nyeroszam = random.randint(tól , ig)
        if nyeroszam in nyeroszamok:
            pass
        else:
            nyeroszamok.append(nyeroszam)
            



tippek = []
index = 1 
while len(tippek) < 6 :
    tipp = int(input(f"add meg az {index}. számot: "))
    tippek.append(tipp)
    index += 1
    


print("@ ötös lottó nyeroszamok 52 hetre: ")

összes_nyeremény = 0

for hét in range (1 ,53):    
    hetiszamok = general(1 , 90)

    talalat = 0
    for x in tippek:
        if x in hetiszamok:
            talalat += 1

    #nyeremeny meghatarozasa
    nyeremeny = 0
    if talalat == 5:
        nyeremeny = 5000
    elif talalat == 4:
        nyeremeny = 3000
    elif talalat == 3:
        nyeremeny = 500
    elif talalat == 2:
        nyeremeny = 250
    

    összes_nyeremény += nyeremeny

    print(F"{hét}. hét nyerőszámai: {hetiszamok}")
    print(F"Talalatok száma: {talalat}")
    print(f"nyeremény: {nyeremeny} ft ")
    

print(f"\n összes nyeremény 52 hét alatt: {összes_nyeremény}")

#  print("@ hatos lottó nyeroszamok 52 hetre: ")
   # for _ in range (52):
#hetiszamok = general(1 , 45 , 6)
 #   print(f"{hetiszamok}")

összes_nyeremény = 0

for hét in range (1 ,53):    
    hetiszamok = general(1 , 45)

    talalat = 0
    for x in tippek:
        if x in hetiszamok:
            talalat += 1

    #nyeremeny meghatarozasa
    nyeremeny = 0
    if talalat == 6:
        nyeremeny = 10000
    elif talalat == 5:
        nyeremeny = 5000
    elif talalat == 4:
        nyeremeny = 3000
    elif talalat == 3:
        nyeremeny = 500
    elif talalat == 2:
        nyeremeny = 250
    

    összes_nyeremény += nyeremeny

    print(f"A 6os lotto nyero szamai")
    print(F"{hét}. hét nyerőszámai: {hetiszamok}")
    print(F"Talalatok száma: {talalat}")
    print(f"nyeremény: {nyeremeny} ft ")
    

print(f"\n összes nyeremény 52 hét alatt: {összes_nyeremény}")