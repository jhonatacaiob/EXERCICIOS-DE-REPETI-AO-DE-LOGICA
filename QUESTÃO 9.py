operação = int(input("Digite o código do produto: "))
compras = []
while operação != 0:
    if operação == 1:
        preços1 = float(input("Quantos produtos?: "))
        valor1 = preços1/2
        compras += [valor1]
        operação = int(input("Digite o código do produto: "))
    elif operação == 2:
        preços2 = float(input("Quantos produtos?: "))
        valor2 = preços2
        compras += [valor2]
        operação = int(input("Digite o código do produto: "))
    elif operação == 3:
        preços3 = float(input("Quantos produtos?: "))
        valor3 = preços3*4
        compras += [valor3]
        operação = int(input("Digite o código do produto: "))
    elif operação == 5:
        preços5 = float(input("Quantos produtos?: "))
        valor5 = preços5*7
        compras += [valor5]
        operação = int(input("Digite o código do produto: "))
    elif operação == 9:
        preços9 = float(input("Quantos produtos?: "))
        valor9 = preços9*8
        compras += [valor9]
        operação = int(input("Digite o código do produto: "))
    else:
        print("Código inválido")
        operação = int(input("Digite o código do produto: "))
print("Deu R$",sum(compras),"de compras no total")
