string = input("Digite uma string: ")
vogais = "aeiouAEIOU"
nova_string = ""
for letra in string:
    if letra not in vogais:
        nova_string += letra
print("A nova string sem vogais é", nova_string)