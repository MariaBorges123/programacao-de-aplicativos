vetor = [1, 3, 5, 7, 9]

numero = int(input("Digite o número que deseja inserir: "))

inicio = 0
fim = len(vetor)

while inicio < fim:
    meio = (inicio + fim) // 2

    if vetor[meio] < numero:
        inicio = meio + 1
    else:
        fim = meio

posicao = inicio

vetor.insert(posicao, numero)

print(f"O número deve ser inserido na posição {posicao}")
print(f"Vetor: {vetor}")
