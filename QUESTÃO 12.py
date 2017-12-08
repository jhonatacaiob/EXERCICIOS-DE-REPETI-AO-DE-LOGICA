altura = int(input("Digite um valor para a altura: "))
largura = int(input("Digite um valor para a largura: "))
print(largura*"*")
for i in range (0,altura-2):
    print("*"," "*(largura-4),'*')
print(largura*"*")