palavra = input("Digite uma palavra: ")
result = ""

for char in palavra:
    val = ord(char) + 1
    result += chr(val)

print(f"A palavra '{palavra}' com cada caractere incrementado é: {result}")