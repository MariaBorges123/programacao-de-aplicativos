id = int(input("digite o seu id: "))
valor_da_compra = int(input("digite o valor da sua compra: "))

if id % 2 == 0 and valor_da_compra >= 500:
    print(f"Parabéns, usuario {id} você ganhou um cupom de desconto em sua compra de R$ {valor_da_compra}")
else:
    print(f"Obrigado pela compra usuario {id} continue acompanhando nossas promoções")
