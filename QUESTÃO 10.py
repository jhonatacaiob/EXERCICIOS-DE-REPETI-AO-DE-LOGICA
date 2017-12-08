primos = [2]
contador = 0
testador = 3
numero = int(input("digite o numero de primos que você quer:"))
while len(primos) < numero:
    for i in primos[:]:
        if testador%i >0:
            contador += 1
    if contador == len(primos):
        primos += [testador]
    contador = 0
    testador += 1
primos=str(primos)
print("os primeiros %i numeros primos são: %s" %(numero,primos))
