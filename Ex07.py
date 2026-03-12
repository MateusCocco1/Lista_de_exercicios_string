frase = input("Digite uma frase: ")

espacos = frase.count(" ")
vogais = 0

for letra in frase.lower():
    if letra in "aeiou":
        vogais += 1

print("Espaços:", espacos)
print("Vogais:", vogais)
