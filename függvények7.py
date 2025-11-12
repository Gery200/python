def összeg (lista) -> int:
    összeg = 0 
    for x in lista:
        összeg += x
    return összeg

def egyenlet(a: int, b: int, c: int, d= int(100) ) -> float:
    return a/b*c*d+(d+c)-(a-d)


raktar = [5, 12, 65, 3, 7]
raktar2 = [4, 5, 67, 75, 345]

print(f"A lista elemeinek az összege: {összeg(raktar)}")
print(f"A raktar 2 lista elemeinek az összege: {összeg(raktar2)}")
print(f"Az egyenlet eredménye: {egyenlet(45, 12, 6)}")