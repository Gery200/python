# szukseges modul meghivasa
import random

#szereplo eletereje konstansként eltárolva változoban
hös_hp = 100
ellenseg_hp = 75




#ki mekkorat üt az adott körben , ehhez sorsolunk véletlenszámot
hös_hit = random.randint(0 , 200)
ellenseg_hit = random.randint(0 , 120)


#dobokockval dobunk es ezzel dontjuk el hogy ki ut 
ütes = random.randint(1 , 6)

if ütes == 1 or ütes == 3 or ütes == 5 or ütes == 6:
    print(f"A hős üt: \n"
          f"\tsebzés: {hös_hit}\n"
          f"Ellenség életereje: {ellenseg_hp - hös_hit}")
else:
    print(f"Ellenség üt ! \n"
          f"sebzés: {ellenseg_hit}\n"
          f"Hős életereje: {hös_hp - ellenseg_hit}\n")
    

if (hös_hp - ellenseg_hit) > 0 and (ellenseg_hp - hös_hit ) <= 0:
    print(f"\n A hős még él"
          f"\n a hős már halott ")
        
    
if (ellenseg_hp - hös_hit) > 0 and (hös_hp ellenseg_hit ) >= 0:
    print(f"\n Az ellesnség még él"
          f"\n az ellensgé már halott ")

