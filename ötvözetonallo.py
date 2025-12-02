with open('forras.txt', 'r', encoding='utf-8') as adatfolyam:
    tartalom = adatfolyam.read()

szoveglista = list(map(str, tartalom.strip().split(" ")))

szoveglista = [szo.strip("., ") for szo in szoveglista]# a szo elejerol es vegerol is eltavolitja

for szo in szoveglista:
    if szo[-1] == "." or szo[-1] == ",":
        pass


#for szo in szoveglista:
#    print(szo)


#hány szo van a forrasban
print(f"A szavak száma a forrásban: {len(szoveglista)}")

# hany a betuvel kezdodo szo van
abetu = []
bbetu = []
cbetu = []
dbetu = []
nvegzodik = []
kbetu = []
minta = []
haromkari = []
for szo in szoveglista:
    if szo[0] == "a" or szo[0] == "A":
        abetu.append(szo)
    elif szo[0] == "b" or szo[0] == "B":
        bbetu.append(szo)
    elif szo[0] == "c" or szo[0] == "C":
        cbetu.append(szo)
    elif szo[0] == "d" or szo[0] == "D":
        dbetu.append(szo)
    elif szo[-1] == "n":
        nvegzodik.append(szo)
    elif "k" in szo or "K" in szo:
        kbetu.append(szo)
    elif "ni" in szo:
        minta.append(szo)
    elif len(szo) == 3:
        haromkari.append(szo)
    


print(f" (A) vagy (a) betuvel kezdodo szavak: {abetu}\n")
print(f" (B) vagy (b) betuvel kezdodo szavak: {bbetu}\n")
print(f" (C) vagy (c) betuvel kezdodo szavak: {cbetu}\n")
print(f" (D) vagy (d) betuvel kezdodo szavak: {dbetu}\n")
print(f" (n) betuvel vegzodik szavak: {nvegzodik}\n")
print(f" (k) vagy (K) betu van benne: {kbetu}\n")
print(f" Van benne ni: {minta}\n")
print(f" HArom karakterbol all: {haromkari}")


with open('iluvhuzzalan.txt', 'a', encoding='utf-8') as myluvhuzzalan:
    print(f" HArom karakterbol all: {haromkari}", file=myluvhuzzalan)
