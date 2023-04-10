let string = prompt("Digite uma string contendo apenas 0's e 1's:");
let numero_uns = (string.match(/1/g) || []).length;
console.log(`O número de 1's na string é ${numero_uns}`);