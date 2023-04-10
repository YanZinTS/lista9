let word = prompt("Digite uma palavra:");
let vowels_count = 0;

for (let letter of word) {
  if ("aeiou".includes(letter.toLowerCase())) {
    vowels_count += 1;
  }
}

let replace_letter = prompt("Digite um caractere para substituir as vogais:");
let new_word = word.replaceAll(/[aeiou]/gi, replace_letter);

console.log(`A palavra '${word}' tem ${vowels_count} vogais.`);
console.log(`A palavra '${new_word}' com as vogais substituídas por '${replace_letter}' é: ${new_word}`);