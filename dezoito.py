palavra = input("Digite uma palavra: ")
resultado = ""

for char in palavra:
    val = ord(char)
    if 65 <= val <= 90:
        val -= 32
    resultado += chr(val)

print(f"A palavra '{palavra}' com as letras maiúsculas convertidas para minúsculas é: {resultado}")