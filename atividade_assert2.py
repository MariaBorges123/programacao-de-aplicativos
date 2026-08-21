def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    return "Reprovado"

situacao_aluno(0)
assert situacao_aluno(7) == "Aprovado"
assert situacao_aluno(6) == "Aprovado"
assert situacao_aluno(5.9) == "Recuperação"
assert situacao_aluno(4) == "Recuperação"
assert situacao_aluno(3) == "Reprovado"