opcao = int(input("Digite a opção: "))

match opcao:
    case 1:
        print("Você escolheu a opção café!")
    case 2:
        print("Você escolheu a opção chá!")
    case 3:
        print("Você escolheu a opção suco!")
    case _:
        print("Opção Inválida...")