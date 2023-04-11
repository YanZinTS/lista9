palavra = input("Digite uma palavra: ")
vogais = "aeiouAEIOU"
newpalavra = ""
for letra in palavra:
    if letra not in vogais:
        newpalavra += letra
print("A nova palavra sem vogais é", newpalavra)