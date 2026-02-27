nome_do_cliente = str(input("digite o nome do cliente: "))
valor_total = float(input("digite o valor total da compra: "))
distancia = int(input("digite qual é a distancia: "))
cupom_desconto = input("digite S para sim e N para não: ")
frete = 40.00 

if cupom_desconto == "S":
    print("Seu cupom solicitado")

elif cupom_desconto == "N":
    print("Seu cupom não sera solicitado")

else:
    print("ok!")

desconto = valor_total * 10
desconto = valor_total - desconto


if valor_total >= 1.000 and cupom_desconto == ("S"): 
    desconto = valor_total * 0.20
    desconto = valor_total - desconto 
    print("Seu cupom é VIP20")

elif valor_total > 500.00 and valor_total < 1000.00 and cupom_desconto:
    desconto= valor_total * 0.10 
    total = valor_total - desconto 
    print ("Seu cupom é PADRÃO10")

if total <=50 and total > 200.00:
    frete = 0.00 
    total_final = total + frete 
else:
    total_final = total + frete 



