vetor = [5, 9, 8, 6, 2, 1, 7, 3, 4, 10]
indice = 0
valor = int(input("Digite o valor que você deseja: "))

for numero in vetor:
    if valor == numero:
        print("Você encontrou o numero desejado!" , indice)
        break
    indice += 1
