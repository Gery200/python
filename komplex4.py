import random
szamlista = []

ujszam = True

while ujszam:
    sorsolt_szam = random.randint(1,9999)
    szamlista.append(sorsolt_szam)
    print(f"Sorsolt szám: {sorsolt_szam}\n"
          f"A lista hossza: {len(szamlista)}")
    kérdés =str(input("Sorsoljak még? (i/n) "))
    if kérdés == 'n':
        ujszam = False
        
print(f"Lista elemei: {szamlista}")


# Bejárás nélkül elvégezhető parancsok / fuggvenyek
print(f"A legkisebb elem: {min(szamlista)}\n"
      f"A legnagyobb elem: {max(szamlista)}\n"
      f"Az elemek összege: {sum(szamlista)} \n"
      f"az elso elem: {szamlista[0]} \n"
      f"Az utolso {len(szamlista)-1}\n")