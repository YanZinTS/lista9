palavra = input("Digite uma palavra: ")

vogais = "aeiouAEIOU"
newpalavra = ""

for letras in palavra:
    if letras not in vogais:
        newpalavra += letras
        
print("A nova palavra sem vogais é", newpalavra)