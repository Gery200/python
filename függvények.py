#A megoldás (nincs visszatérési érték- "alapprogram")
#FÜGGVÉNYDEFINÍCIÓ
def kiír(): #függvény neve , zárójelbe az attribútumuk
    print("TESZT") # a függvény hívása során történik


# függvény (meg)hívása
kiír()



#B megoldás(szabványos függvény)
def kiír2(a):
    return a # ez egy függvényérték (visszatérési érték)

print(kiír2("Alma"))


def össz(a ,b) -> int:
    osszeg = a + b 
    return osszeg # mindig valaminke az értéke vátozónévvel lehivatkozva 



def össz2 (a=int(10) , b=int(12)) -> int:
    return a + b 

print(össz2())


def egyenlet (a , b , c , d ) -> float: # alapértelmezés nélküli függvény
    eredmeny = a*b*c*+(d/c)+(a*d)+b-(d*a)
    return eredmeny

print(f"az egyenlet eredmenye: {egyenlet(43,45,65,78):.2f}")
   
    
def egyenlet2 (a ,b ,c ,d = int(100) ) -> float: # a (d) alapértelmezett érték
    eredmeny = a*b*c*+(d/c)+(a*d)+b-(d*a)
    return eredmeny



a = int(input("add meg az (a) szamot:"))
b = int(input("add meg az (b) szamot:"))
c = int(input("add meg az (c) szamot:"))
d = int(input("add meg az (d) szamot:"))



    
print(f"az egyenlet eredmenye {egyenlet2(a,b,c):}")
  
    
    

    
    
    
