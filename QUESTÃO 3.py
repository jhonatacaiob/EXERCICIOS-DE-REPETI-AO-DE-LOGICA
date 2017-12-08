a=int(input("Digite o número que você quer fazer a tabuada: "))
b=int(input("Digite até ontem você quer: "))
for i in range(a,b+1,1):
    soma=a+i
    mult=a*i
    print(a,"+",i,"=",soma,"e",a,"x",i,"=",mult)