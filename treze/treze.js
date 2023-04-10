let string = prompt("Digite uma string:");
let vogais = "aeiouAEIOU";
let nova_string = "";
for(let letra of string){
    if(!vogais.includes(letra)){
        nova_string += letra;
    }
}
console.log(`A nova string sem vogais é ${nova_string}`);