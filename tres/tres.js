let vetA = "COMPUTACAO".split("");
let vetB = prompt("Digite uma palavra de 10 letras:");
vetB = vetB.split("");

for(let i = 0; i < vetB.length; i++){
    if(vetB[i].toUpperCase() === vetA[i]){
        console.log(`O índice ${i} de vetB possui a letra ${vetB[i]} que é igual à letra ${vetA[i]} de vetA.`);
    }
}