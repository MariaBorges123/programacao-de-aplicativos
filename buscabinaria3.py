vetor = [5, 9, 8, 6, 2, 1, 7, 3, 4, 10]
indice = 0
maior = vetor[0]
posicao = 0

for numero in vetor:
    if numero > maior:
        maior = numero
        posicao = indice
    indice += 1

print("O maior número é:", maior)
print("A posição do maior número é:", posicao)