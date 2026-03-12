num = int(input("Digite um número de 0 a 99: "))

unidades = ["zero","um","dois","três","quatro","cinco","seis","sete","oito","nove"]
dezenas = ["dez","vinte","trinta","quarenta","cinquenta","sessenta","setenta","oitenta","noventa"]

if num < 10:
    print(unidades[num])

elif num % 10 == 0:
    print(dezenas[num//10 -1])

else:
    print(dezenas[num//10 -1], "e", unidades[num%10])
