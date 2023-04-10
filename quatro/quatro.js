let letra_maiuscula = prompt("Digite uma letra maiúscula:");
let letra_minuscula = String.fromCharCode(letra_maiuscula.charCodeAt(0) + 32);
console.log(`A letra minúscula correspondente é ${letra_minuscula}`);