produto = input("digite o nome do produto: ")
preco_unitario = float(input("digite o preço do produto unitario: "))
quantidade = int(input("digite a quantidade que o cliente está comprando: "))

valor_da_compra = quantidade*preco_unitario

print("o nome do produto é: " , produto)
print("preço unitario: " , preco_unitario)
print("a quantidade é: " , quantidade)
print("o preço a ser pago é: " , valor_da_compra)