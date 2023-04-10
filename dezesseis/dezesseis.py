word = input("Digite uma palavra: ")
result = ""

for char in word:
    ascii_value = ord(char) + 1
    result += chr(ascii_value)

print(f"A palavra '{word}' com cada caractere incrementado em 1 no valor ASCII é: {result}")