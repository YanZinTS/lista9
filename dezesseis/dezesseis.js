let word = prompt("Digite uma palavra:");
let result = "";

for (let char of word) {
  let asciiValue = char.charCodeAt(0) + 1;
  result += String.fromCharCode(asciiValue);
}

console.log(`A palavra '${word}' com cada caractere incrementado em 1 no valor ASCII é: ${result}`);