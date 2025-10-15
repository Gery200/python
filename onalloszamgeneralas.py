import random
import math 

szamlista = []
ketto = []
ot = []
kitorles = []
gyokszam = []

for x in range(500):
    szamlista.append(random.randint(0 , 500))
    

for x in szamlista:
    if x % 2 == 0: 
        ketto.append(x)
    if x % 5 == 0:
        ot.append(x)
        
szamlista.sort()            


        




        
print(f"A lista összes eleme {szamlista} \n"
    f"a lista elos eleme {szamlista[0]} \n"
      f"a lista mindenkori utolso eleme {szamlista[-1]} \n"
    f"a kettovel osztahto szamok: {ketto} \n \n"
      f"Az öttel osztahto szamok: {ot}"
      f"")