let nome = prompt("Digite o nome:");
let sexo = prompt("Digite o sexo (M ou F):");
let idade = parseInt(prompt("Digite a idade:"));

if(sexo === "F" && idade < 25){
    console.log(`${nome} ACEITA`);
} else {
    console.log("NÃO ACEITA");
}