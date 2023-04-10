let phrase = prompt("Digite uma frase:");
let count = 0;

for (let char of phrase) {
  if (char === " ") {
    count += 1;
  }
}

console.log(`A frase '${phrase}' tem ${count} caracteres brancos.`);