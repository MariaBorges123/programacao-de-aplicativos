def analizar_vendas(nome, lista_vendas, meta):
    total = 0
    for venda in lista_vendas:
        total += venda 

    media = total/len(lista_vendas)

    if media >= meta :
        resposta_meta = "bateu!"
    else:
        resposta_meta = "não bateu!"

    return f"O vendedor {nome} teve média de {media} e {resposta_meta} a meta"


nome = input("digite seu nome: ")
lista = [1200, 1500, 1100, 1900]
meta = float(input("Digite sua meta: "))

chamada = analizar_vendas(nome , lista , meta)
print(chamada)