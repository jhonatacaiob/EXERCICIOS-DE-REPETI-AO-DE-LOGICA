n=1
quantidade=0
soma=0
while n!=0:
    n=int(input("Digite o numero (0 para sair) "))
    soma+=n
    quantidade+=1
print("quantidade:",quantidade-1)
print("soma:",soma)
print("media", soma/quantidade)
