palavra = input("Digite uma palavra: ")
cot = 0

for letter in palavra:
    if letter.lower() in "aeiou":
        cot += 1

caracter = input("Digite um caractere para substituir as vogais: ")
newpalavra = palavra.replace("a", caracter).replace("e", caracter).replace("i", caracter).replace("o", caracter).replace("u", caracter)

print(f"A palavra '{palavra}' tem {cot} vogais")
print(f"A palavra '{newpalavra}' com as vogais substituídas por '{caracter}' agora é: {newpalavra}")