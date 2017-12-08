lista_de_v=[]
lista_de_p=[]
for i in range(0,15):
    VoP = input("Qual o tipo de transação?(V para a vista ou P para a prazo): ")
    if VoP == "V" or VoP == "v":
        Valor_de_v = float(input("Qual o valor da transação?: "))
        lista_de_v += [Valor_de_v]
    elif VoP == "P" or VoP == "p":
        Valor_de_p = float(input("Qual o valor da transação?: "))
        lista_de_p += [Valor_de_p]
    else:
        print("Comando Inválido")
somatoria_de_v = sum(lista_de_p)
somatoria_de_p = sum(lista_de_v)
valor_total = somatoria_de_p + somatoria_de_v
listavep = lista_de_p+lista_de_v
menor_valor = int(min(listavep))
maior_valor = int(max(listavep))
print("O total a vista foi R$ %i, a prazo foi R$ %i e o total foi R$ %i" %(somatoria_de_v, somatoria_de_p, valor_total))
print("O menor valor foi R$ %i e o maior valor foi R$ %i" %(menor_valor, maior_valor))
