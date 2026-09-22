dia = int(input("Digite o dia da semana: "))

match dia:
    case 1:
        print("domingo")
    case 2:
        print("segunda-feira")
    case 3:
        print("terça-feira")
    case 4:
        print("quarta-feira")
    case 5:
        print("quinta-feira")
    case 6:
        print("sexta-feira")
    case 7:
        print("sábado")
    case _:
        print("opção inválida")