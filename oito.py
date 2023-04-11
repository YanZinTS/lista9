nome = input("Digite o nome: ")
sexo = input("Digite o sexo (m/f): ")
idade = int(input("Digite a idade: "))

if sexo == "f" and idade < 25:
    print(nome, "ACEITA")
else:
    print("NÃO ACEITA")