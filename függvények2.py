def összeg (a,b) -> int:
    return a+b

def kukolnbsehg (a,b) -> int:
    return a+b

def szorzat (a,b) -> int:
    return a*b

def oszt (a,b) -> float:
    return a/b

def maradek (a,b) -> int:
    return a % b

beszám1 = int(input("adja meg az első számot: "))
beszám2 = int(input("adja meg a második számot: "))

print(f"A két szám összege {összeg(beszám1 , beszám2)}")
print(f"A két szám különbsége {kukolnbsehg(beszám1 , beszám2)}")
print(f"A két szám hányadosa {oszt(beszám1 , beszám2)}")
print(f"A két szám szorzata {szorzat(beszám1 , beszám2)}")
print(f"A két szám maaradeka {maradek(beszám1 , beszám2)}")