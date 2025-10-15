szoveg = str("Lorem ipsum dolor sit, amet consectetur adipisicing elit. Totam ipsum voluptate molestiae nemo suscipit sunt tenetur obcaecati. Expedita deleniti atque sint tenetur dolorem vel corporis ducimus amet quibusdam, doloribus perferendis?")

print(f"Első betű: {szoveg[0]}")
print(f"utólsó betű: {szoveg[-1]}")
print(f"szöveg hossza: {len(szoveg)}")


# szavak száma 
szavak = 0
for szo in szoveg:
    if szo == " " : 
        szavak += 1 

print(f"A szavak száma {szavak}")

# a bekért betüből hány darab van ? 

              
Bekért_betu = str(input("melyik betut keresem"))
betu_szama = 0 
for betu in szoveg:
    if Bekért_betu == betu in szoveg:
        print(f"találat")
        betu_szama += 1 
    else: 
        print(f"Nincsen találat")
        
print(f"a keresett betu ennyiszer szerepel : {Bekért_betu}")

index = 0 
while index < betu_szama:
    szoveg.remove()