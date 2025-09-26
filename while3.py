import random

kilepesi_pont = 0

while kilepesi_pont != 4987:
    kilepesi_pont = random.randint(1,4987) #bug
    print(f"Sorsolt szam: {kilepesi_pont}")
    
print(f">> Program vége <<")