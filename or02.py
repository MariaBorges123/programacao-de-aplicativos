media = float(input("digite sua media: "))
renda = int(input(" digite o valor de sua renda: "))
escola = input("digite se você era de escola publica (S/N): ")

if media >= 8.0 and ( renda < 2000.00 or escola == "S"): 
    print("Você ganhou a bolsa!")
else:
    print("Você não ganhou a bolsa!")