let word = prompt("Digite uma palavra:");
let result = "";

for (let char of word) {
  let asciiValue = char.charCodeAt(0);
  if (asciiValue >= 65 && asciiValue <= 90) {
    asciiValue -= 32;
  }
  result += String.fromCharCode(asciiValue);
}

console.log(`A palavra '${word}' com as letras maiúsculas convertidas para minúsculas é: ${result}`);