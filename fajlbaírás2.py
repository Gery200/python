# r = olvasás
# w = irás hoz féjlt létre ha már van olyan nevű akkor felulirja
# x = írás hoz létre fájlt ha már van olyan fájl akko huibát ad
# a = a létező fájlhoz hozzáfű ha még nem létezik létrehoz
# a+ = hozzáfűz és olvasást is lehetővé teszi



with open('kimenet.txt' , 'w' , encoding='utf-8') as adatfolyam:
    print('Lorem ipsum' , file=adatfolyam) # tényleges fájlba írás
    print(f' \n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eleifend vestibulum euismod. Nunc pulvinar molestie turpis, ac fermentum libero rutrum sed. Aenean varius pulvinar efficitur. Fusce lacus tellus, tristique in sagittis vitae, egestas nec sem. Sed sed pharetra sem, id vehicula orci. Maecenas ac tincidunt libero, a lacinia massa. Mauris sit amet eros ultrices nisi efficitur volutpat. Aliquam commodo ex efficitur tortor cursus accumsan. Aenean vitae augue sed ante blandit convallis. Sed tortor massa, vehicula nec facilisis in, pulvinar quis dolor. Ut sit amet ex at massa condimentum luctus vitae sed diam. Donec ut molestie nulla. Sed vitae nisl eget massa condimentum fringilla. Pellentesque pulvinar malesuada scelerisque. Phasellus placerat elementum tellus, eu facilisis orci lacinia eu.' , file=adatfolyam)
    print(f' \n Ut sit amet lacinia nisl, vitae dignissim libero. Mauris ac dignissim justo, non tempor sem. Duis dictum finibus dignissim. Sed bibendum massa ac mi vestibulum, vel porttitor mi ullamcorper. In hac habitasse platea dictumst. Duis in dui tellus. Ut rhoncus tincidunt tincidunt. Suspendisse vehicula metus id risus convallis euismod. Morbi sit amet arcu nec eros feugiat vulputate. Integer nunc mi, placerat vitae pulvinar in, interdum nec mauris. Pellentesque velit mauris, bibendum eget purus in, dictum malesuada neque. Vivamus ornare velit non dolor consequat interdum. Nam auctor dui at ante porttitor, sed auctor quam malesuada.' , file=adatfolyam)
    print(f" \n a fájlba írás sikeresen megtörtént")
import random
