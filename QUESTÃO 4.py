numero=int(input("DIGITE UM NUMÉRO INTEIRO: "))
while numero<0:
    print("DIGITE NOVAMENTE: ")
    numero = int(input("DIGITE UM NUMÉRO INTEIRO: "))
algo=1
for n in range(numero,0,-1):
    algo*=n
print(algo)
