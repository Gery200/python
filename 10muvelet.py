import random
import math
from datetime import datetime, date, time, timedelta
import os



def abetu () -> str:
    alista2 = []
    for x in tartalom:
        if x[0] == "a":
            alista2.append(x)
    return  alista2

print(f"{abetu}")


def datum():
    return datetime.now
 
def olvasas():
    with open('forras11.txt' , 'r' , encoding='utf-8') as fajl1:
        adatfolyam = fajl1.read()
        fajl.close()


def cleanterminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

def bbetu ():
    blista = []
    for x in tartalom:
        if x[0] == "b":
            blista.append(x)
    return blista



now = datetime.now()
print("Current datetime:", now)

today = date.today()
print("Today's date:", today)


with open('forras.txt' , "r" , encoding='utf-8') as fajl:
    tartalom = fajl.read()


elvalasztok = ["," , "?" , "!" , "." , "-"]

for jel in elvalasztok:                             #az a alábbi karaktereket kivesszuk a listabol (kicseréljuk)
    tartalom = tartalom.replace(jel, " ")


tartalom = tartalom.lower()  # az összes betűt kicsivé tesszük

szavak = tartalom.split()
tartalom = tartalom.lower()


print(f"Szavak száma: {len(szavak)}")  # a szavak száma a listában

tisztott = []

for szo in szavak:             #kiszedjuk az ures helyeket a szövegből (letisztítjuk)
    if szo != "":
       tisztott.append(szo)

szavak = tisztott

alista = []

for x in tisztott:         # az A betus szavak listája
    if x[0] == "a":   
        alista.append(x)

alista.sort()

print(f"\nAz a betus szavak listája:{alista}") # az abetus szavak 
print(f" \nEnnyi a betus szo van : {len(alista)}") # a betűs szavak száma

cda = []

for x in tisztott:
    if 'acc' == x:      # az acc betűsor szerepel e a listában
        cda.append(x)

print(f"ennyiszer szerepel a ism szó kombináció a szövegben: {len(cda)}") # az acc betűsor ennyiszer szerepel a listában

blista = []

for x in tisztott:
    if x[0] == "b":     #B vel kezdődő szavak kiszűrése
        blista.append(x)

print(f"B-vel kezdődő szavak szám: {len(blista)}")



with open('abckimenet.txt' , 'a' , encoding='utf-8') as abcd :   #kiírjuk az a betüs szavakat egy listába
        print(f"Az abc betus szavak: {alista}" , file=abcd)


