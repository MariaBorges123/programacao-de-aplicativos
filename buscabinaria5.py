vetor = [5, 2, 8, 5, 3, 9, 5, 4, 2, 7]
indice = 0
primeira = -1
ultima = -1

valor = int(input("Digite o valor que você deseja procurar: "))

for numero in vetor:
    if valor == numero:
        if primeira == -1:
            primeira = indice

        ultima = indice

    indice += 1

if primeira != -1:
    print("A primeira posição é:", primeira)
    print("A última posição é:", ultima)
else:
    print("O valor não foi encontrado.")
