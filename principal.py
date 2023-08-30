
from binario import Binario
from octal import Octal
from hexadecimal import Hexadecimal


caso = int(input("\n elija: \n1.Binario\n2.Octal\n3.Decimal\n4.Hexadecimal\n\n-"))
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
    for i in range(numero+1):
        print(i)

elif caso == 4:
    c = Hexadecimal()
    
    for i in range(numero+1):
        c.numero = i
        print(c.valor_hex())

else :
    print("\nERROR!")