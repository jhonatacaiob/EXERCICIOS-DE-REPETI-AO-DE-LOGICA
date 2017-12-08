list=[0,1]
n=int(input("digite um numero"))
marcador = len(list)
while marcador < n:
    y = len(list)
    soma = list[y-1] + list[y-2]
    list += [soma]
    marcador+=1
print(list)