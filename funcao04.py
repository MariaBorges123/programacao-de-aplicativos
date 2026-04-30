def esta_na_lista(lista, nome_busca):
    for item in lista:
        if item == nome_busca:
            return "Encontrado!"
    return "Não disponível"

frutas = ["maçã", "banana", "laranja", "uva", "abacaxi"]

print(esta_na_lista(frutas, "banana"))
print(esta_na_lista(frutas, "manga")) 