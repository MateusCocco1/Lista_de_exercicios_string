cpf = input("Digite o CPF (xxx.xxx.xxx-xx): ")

if len(cpf) == 14 and cpf[3] == "." and cpf[7] == "." and cpf[11] == "-":
    print("Formato válido")
else:
    print("Formato inválido")
