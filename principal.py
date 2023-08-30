
from binario import Binario
from octal import Octal
from hexadecimal import Hexadecimal


caso = int(input("\n elija: \n1.binario\n2.octal\n3.hexadecimal\n\n-"))
numero= int(input("\n Digita el número hasta el que quieres contar: "))


if caso == 1:
    c = Binario()
    
    for i in range(numero+1):
        c.numero = i
        print(c.valor_bin())

elif caso == 2:
    c = Octal()
    
    for i in range(numero+1):
        c.numero = i
        print(c.valor_oct())
        
elif caso == 3:
    c = Hexadecimal()
    
    for i in range(numero+1):
        c.numero = i
        print(c.valor_hex())

else :
    print("\nerror")