palavras = ["banana", "casa", "gato", "livro", "maçã", "rato"]

palavra = input("Digite uma palavra: ")

inicio = 0
fim = len(palavras) - 1
encontrou = False

while inicio <= fim:
    meio = (inicio + fim) // 2

    if palavras[meio] == palavra:
        encontrou = True
        break
    elif palavra > palavras[meio]:
        inicio = meio + 1
    else:
        fim = meio - 1

if encontrou:
    print("A palavra está na lista!")
else:
    print("A palavra não está na lista!")
