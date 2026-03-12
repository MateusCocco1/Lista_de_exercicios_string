texto = input("Digite um texto: ")

leet = texto.lower()

leet = leet.replace("a","4")
leet = leet.replace("e","3")
leet = leet.replace("i","1")
leet = leet.replace("o","0")
leet = leet.replace("t","7")
leet = leet.replace("s","5")

print("Leet Speak:", leet)
