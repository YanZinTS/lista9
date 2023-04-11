word = input("Digite uma palavra: ")
result = ""

for char in word:
    ascii_value = ord(char)
    if 65 <= ascii_value <= 90:
        ascii_value -= 32
    result += chr(ascii_value)

print(f"A palavra '{word}' com as letras maiúsculas convertidas para minúsculas é: {result}")