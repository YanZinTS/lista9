let palavra = prompt("Digite uma palavra:");
let vogais = 0;

for(let i = 0; i < palavra.length; i++){
    if('aeiouAEIOU'.includes(palavra[i])){
        vogais++;
    }
}

console.log(`A palavra ${palavra} possui ${vogais} vogais.`);