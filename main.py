print("--- Classificador de Idade ---\n")

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

if idade < 18:
    print(f"\nOlá, {nome}! Como você tem {idade} anos, você é menor de idade.")
elif idade >= 18 and idade <= 65:
    print(f"\nOlá, {nome}! Como você tem {idade} anos, você é um adulto.")
else:
    print(f"\nOlá, {nome}! Como você tem {idade} anos, você é uma pessoa que se aposentou.")
