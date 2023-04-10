let string = prompt("Digite uma string:");
let caractere_antigo = "0";
let caractere_novo = "1";
let nova_string = string.replaceAll(caractere_antigo, caractere_novo);
console.log(`A nova string é ${nova_string}`);