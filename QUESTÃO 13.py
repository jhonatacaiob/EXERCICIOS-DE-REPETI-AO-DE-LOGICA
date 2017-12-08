n=int(input("digite um numero: "))
def repetição_1():
    valor1="*"
    for i in range(0,n+1,1):
        print(i*valor1)
def repetição_2():
    valor2="*"
    for i in range(n,-1,-1):
        print(i*valor2)
repetição_1()
repetição_2()
for j in range(0,n):
    k = n-j
    print(" "*j,"*"*(k))
for j in range(n-1,-1,-1):
    k = n-j
    print(" "*j,"*"*(k))