vA = list("COMPUTAÇÃO")
vB = input("Digite uma palavra de 10 letras: ")

for i in range(len(vB)):
    if vB[i].upper() == vA[i]:
        print("O índice", i, "de vetB possui a letra", vB[i], "que é igual à letra", vA[i], "de vetA.")