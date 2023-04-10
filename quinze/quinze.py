phrase = input("Digite uma frase: ")
count = 0

for char in phrase:
    if char == " ":
        count += 1

print(f"A frase '{phrase}' tem {count} caracteres brancos.")