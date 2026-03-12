s1 = input("Digite a primeira string: ")
s2 = input("Digite a segunda string: ")

print("String 1:", s1)
print("Tamanho:", len(s1))

print("String 2:", s2)
print("Tamanho:", len(s2))

if len(s1) == len(s2):
    print("As duas strings têm o mesmo tamanho.")
else:
    print("As duas strings têm tamanhos diferentes.")

if s1 == s2:
    print("As duas strings possuem conteúdo igual.")
else:
    print("As duas strings possuem conteúdo diferente.")
