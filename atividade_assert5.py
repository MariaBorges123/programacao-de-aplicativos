def calcular_frete(valor_compra):
    if valor_compra >= 200:
        return 0
    elif valor_compra >= 100:
        return 10
    return 20


calcular_frete(67)
assert calcular_frete(67) == 20
assert calcular_frete(100) == 10
assert calcular_frete(167) == 10
assert calcular_frete(199.99) == 10
assert calcular_frete(200) == 0
assert calcular_frete(267) == 0