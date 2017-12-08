numero=int(input("DIGITE UM NUMERO INTEIRO: "))
while numero<0:
        print("Número Inválido")
        numero = int(input("DIGITE UM NUMERO INTEIRO: "))
algo=0
for n in range(1,numero+1,1):
    algo+=n
print(algo)