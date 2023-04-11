vetA = list("COMPUTACAO")
vetB = input("Digite uma palavra de 10 letras: ")

for i in range(len(vetB)):
    if vetB[i].upper() == vetA[i]:
        print("O índice", i, "de vetB possui a letra", vetB[i], "que é igual à letra", vetA[i], "de vetA.")