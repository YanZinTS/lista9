frase = input("Digite uma frase: ")
cot = 0

for char in frase:
    if char == " ":
        cot += 1

print(f"A frase '{frase}' tem {cot} caracteres brancos")