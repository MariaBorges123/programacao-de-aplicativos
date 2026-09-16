vetor = []

while numero <= 100:
    vetor.append(numero)
    numero += 1
valores = [10, 50, 100]


for numero in valores:

    comparacoes_sequencial = 0
    encontrado = False

    for valor in vetor:
        comparacoes_sequencial += 1

        if valor == numero:
            encontrado = True
            break

    inicio = 0
    fim = len(vetor) - 1
    comparacoes_binaria = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2

        comparacoes_binaria += 1

        if vetor[meio] == numero:
            break
        elif numero > vetor[meio]:
            inicio = meio + 1
        else:
            fim = meio - 1


    print(f"\nValor procurado: {numero}")
    print(f"Comparações - Sequencial: {comparacoes_sequencial}")
    print(f"Comparações - Binária: {comparacoes_binaria}")
