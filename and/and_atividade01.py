idade = int(input("digite sua idade: "))
saldo = float(input("digite o valor do seu saldo: "))

if idade >= 18 and saldo >= 50.00:

    print("Acesso autorizado! Bem vindo ao evento")

elif idade < 18 and saldo < 50.00:

    print("Infelizmente você não cumpre os requisitos da entrada")
    

