import random

palavras = ["python","computador","programacao","teclado"]
palavra = random.choice(palavras)

letras_descobertas = ["_"] * len(palavra)
tentativas = 6

while tentativas > 0 and "_" in letras_descobertas:
    
    print(" ".join(letras_descobertas))
    letra = input("Digite uma letra: ")

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras_descobertas[i] = letra
    else:
        tentativas -= 1
        print("Errou! Tentativas:", tentativas)

if "_" not in letras_descobertas:
    print("Você venceu! Palavra:", palavra)
else:
    print("Você perdeu! Palavra:", palavra)
