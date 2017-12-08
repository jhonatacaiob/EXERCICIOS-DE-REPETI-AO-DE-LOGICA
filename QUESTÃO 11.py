texto = input("Digite um texto(Pode ser palavra ou uma frase): ")
texto_reverso=""
if " " not in texto:
    texto=texto.lower()
    for l in range(len(texto)-1,-1,-1):
        texto_reverso += texto[l]

    if texto_reverso==texto:
        print("ISSO É UM PALÍNDROMO")
    else:
        print("ISSO NÃO É UM PALÍNDROMO")
else:
    textoLista=texto.split()
    texto="".join(textoLista)
    texto=texto.lower()
    for i in range(len(texto)-1,-1,-1):
        texto_reverso += texto[i]
    if texto_reverso == texto:
        print("ISSO É UM PALÍMDROMO")
    else:
        print("ISSO NÃO É UM PALÍNDROMO")
        
