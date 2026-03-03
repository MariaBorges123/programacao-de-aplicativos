idade = int(input("digite sua idade: "))
ingresso = input("digite se você tem o ingresso VIP  (S/N): ")
lista = input("digite se você tem o nome na lista (S/N): ")

if idade >= 18 and (ingresso == "S" or lista == "S"):
    print ("seja bem vindo!")
else :
    print("acesso negado!")