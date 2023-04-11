word = input("Digite uma palavra: ")
vowels_count = 0

for letter in word:
    if letter.lower() in "aeiou":
        vowels_count += 1

replace_letter = input("Digite um caractere para substituir as vogais: ")
new_word = word.replace("a", replace_letter).replace("e", replace_letter).replace("i", replace_letter).replace("o", replace_letter).replace("u", replace_letter)

print(f"A palavra '{word}' tem {vowels_count} vogais.")
print(f"A palavra '{new_word}' com as vogais substituídas por '{replace_letter}' é: {new_word}")