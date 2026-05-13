def avaliar_desempenho(nota):
    if nota >= 9:
        return "exelente"
    elif nota >= 7:
        return "bom"
    elif nota > 5:
        return "regular"
    else:
        return "insuficiente"

nota_usuario = int(input("Digite a sua nota: "))
mensagem = avaliar_desempenho(nota_usuario)

print(mensagem)