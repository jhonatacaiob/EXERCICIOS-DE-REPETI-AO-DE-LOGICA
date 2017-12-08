primeira=[]
segundo=[]
terceiro=[]
quarto=[]
quinto=[]
def preguiça(x):
    print("Nessa lista, existem", len(x), "pessoas")
for i in range (1,16,1):
    idades = int(input("QUAL SUA IDADE?: "))
    if idades<=0:
        print("Você não é um recém nascido")
    elif idades <= 15:
        primeira += [idades]
    elif idades >= 16 and idades <= 30:
        segundo += [idades]
    elif idades >= 31 and idades <= 45:
        terceiro += [idades]
    elif idades >= 46 and idades <= 60:
        quarto += [idades]
    elif idades > 60:
        quinto += [idades]
preguiça(primeira)
preguiça(segundo)
preguiça(terceiro)
preguiça(quarto)
preguiça(quinto)