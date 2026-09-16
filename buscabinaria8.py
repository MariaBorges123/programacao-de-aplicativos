vetor = [1, 2, 3, 4, 6, 6, 6, 8]

numero = int(input("Digite o valor: "))

inicio = 0
fim = len(vetor) - 1
indice = -1
comparacoes = 0

while inicio <= fim:
    meio = (inicio + fim) // 2

    comparacoes += 1

    if vetor[meio] == numero:
        indice = meio
        break
    elif numero > vetor[meio]:
        inicio = meio + 1
    else:
        fim = meio - 1

print(f"Índice: {indice}")
print(f"Comparações: {comparacoes}")
