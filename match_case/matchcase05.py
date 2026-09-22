numero1 = int(input("Digite o valor do numero 1: "))
numero2 = int(input("Digite o valor do numero 2: "))

opcao = input("Digite qual opção vc quer (+ ou -): ")

match opcao:
    case "+":
       Resultado = numero1 + numero2
       print("Resultado:" , Resultado)
    case "-":
        Resultado = numero1 - numero2
        print("Resultado:" , Resultado)
    case _:
        print("Operação inválida!")
