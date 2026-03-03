valor_compra = float (input("digite o valor da sua compra: "))
prime = input("digite se você é prime (S/N): ")

frete = 50.00 

if valor_compra > 500.00 or (prime == "S" and valor_compra > 100.00):
    