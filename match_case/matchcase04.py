nota = input("Digite a sua nota expressa: ")

match nota:
    case "A":
        print("Excelente desempenho!")
    case "B":
        print("Excelente desempenho!")
    case "C":
        print("Desempenho mediano!")
    case "D":
        print("Desempenho mediano!")
    case "F":
        print("Reprovado!")
    case _:
        print("Conceito inválido...")