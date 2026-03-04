saldo_inicial = 1000.00
print("1- deposito, 2- saque , 3-extrato")
menu = input("digite sua opção: ")

if menu == "1":
    valor = float(input("digite o valor do deposito: "))
    if valor > 0:
        saldo_inicial = saldo_inicial + valor
        print("deposito realizado com sucesso!")

elif menu == "2":
    valor = float(input("digite o valor do seu saque: "))
    if valor > 0 and (valor <= saldo_inicial or valor == 100 ):
        saldo_inicial = saldo_inicial - valor
        print("saque realizado com sucesso!")

elif menu == "3":
    print("seu saldo: ", saldo_inicial)

