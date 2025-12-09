with open('./forras6.txt' , 'r' , encoding='utf-8') as adatfolyam:
    tartalom = adatfolyam.read()
    
tartalom = list(map(str, tartalom.strip().split(" ")))

tartalom = [szó.strip(" ") for szó in tartalom] 

tartalom = [szó.rstrip(" ") for szó in tartalom]



for szó in tartalom:
    print(szó)
    

