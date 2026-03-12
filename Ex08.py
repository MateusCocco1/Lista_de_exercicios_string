texto = input("Digite uma palavra: ")

if texto == texto[::-1]:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
