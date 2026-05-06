def calcular_preco_final(valor_base, imposto_percentual, cupom_desconto):
    valor_imposto  = valor_base + imposto_percentual

    if cupom_desconto > valor_imposto:
        preco_final = 0
        return preco_final
    elif cupom_desconto > 0:
        preco_final = valor_imposto - cupom_desconto
        return preco_final
    
    return valor_imposto

valor_base = int(input("Digite o valor do produto: "))
imposto_percentual = int(input("Digite o valor do imposto: "))
cupom_desconto = int(input("Digite o valor do desconto: "))

chamada = calcular_preco_final(valor_base, imposto_percentual, cupom_desconto)

print(chamada)
    

