palavra = input("Digite uma palavra: ")
vogais = 0

for letra in palavra:
    if letra in 'aeiouAEIOU':
        vogais += 1

print("A palavra", palavra, "possui", vogais, "vogais.")