print("Menu de operações")
print("+ para somar")
print("– para subtrair")
print("* para multiplicar")
print("/ para dividir")
print("s para sair")
while 1==1:
    operação = input("Escolha a operação: ").lower()
    if operação == "s":
        print("Programa encerrado.")
        break
    else:
        primeiro_numero = int(input("Digite o primeiro numero: "))
        segundo_numero = int(input("Digite o segundo numero: "))
        if operação == "+":
            resultado = primeiro_numero+segundo_numero
            print(primeiro_numero, operação, segundo_numero,"=",resultado)
        elif operação == "-":
            resultado = primeiro_numero - segundo_numero
            print(primeiro_numero, operação, segundo_numero, "=", resultado)
        elif operação == "*":
            resultado = primeiro_numero * segundo_numero
            print(primeiro_numero, operação, segundo_numero, "=", resultado)
        elif operação == "/":
            resultado = primeiro_numero / segundo_numero
            print(primeiro_numero, operação, segundo_numero, "=", resultado)