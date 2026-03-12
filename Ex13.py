import random

palavras = ["python","computador","teclado","internet"]
palavra = random.choice(palavras)

lista = list(palavra)
random.shuffle(lista)

embaralhada = "".join(lista)

print("Palavra embaralhada:", embaralhada)

tentativa = input("Qual é a palavra? ")

if tentativa == palavra:
    print("Acertou!")
else:
    print("Errou! A palavra era:", palavra)
