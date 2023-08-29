from decimal import Decimal
from binario import Binario
from octal import Octal
from hexadecimal import Hexadecimal

caso = int(input("\n elija: \n1.decimal\n2.binario\n3.octal\n4.hexadecimal\n\n"))
if caso == 1 :
    print("\n")
    if __name__ == '__main__':
        instanceDecimal = Decimal()
        instanceDecimal.Valor_decimal()
elif caso == 2 :
    print("\n")
    if __name__ == '__main__':
        instanceBin = Binario()
        instanceBin.valor_bin()
elif caso == 3:
    print("\n")
    if __name__ == '__main__':
        instanceOct = Octal()
        instanceOct.valor_oct()
elif caso == 4:
    print("\n")
    if __name__ == '__main__':
        instanceHex = Hexadecimal()
        instanceHex.valor_hex()
else :
    print("\nerror")