nevek = []


kisa = str(input(f"adjon meg szavakat kis a bteuvel: "))

kisa1 = True

while kisa1 == True:
    kisa = str(input(f"adjon meg szavakat kis a bteuvel: "))
    if kisa[0] == 'a' :
        nevek.append(kisa)
    if kisa == "":
        kisa1 = False
        print(f"A kis a betűs szavak: {nevek}")
        
        
    
    

