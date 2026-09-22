estacoes = int(input("Digite o numero de 1 a 12:  "))

match estacoes:
    case 1 | 2 | 12:
        print("Verão")
    case 3 | 4 | 5:
        print("Outono")
    case 6 | 7 | 8:
        print("Inverno")
    case 9 | 10 | 11:
        print("Primavera")
    case _:
        print("estções inválidas")