dia = input("Digite um dia: ")

match dia:
    case "sábado" | "domingo":
        print("Fim de semana")
    case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
        print("Dia útil")
    case _:
        print("Texto inválido")
