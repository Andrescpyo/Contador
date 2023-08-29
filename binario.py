class Binario():
    def valor_bin(self):
        for i in range(10):
            binario = bin(i)[2:]
            print(binario)