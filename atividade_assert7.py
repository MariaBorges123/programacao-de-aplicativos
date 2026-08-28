def verificar_aprovacao(nota1, nota2):
    media = (nota1 + nota2) / 2

    if media > 6:
        return "Aprovado"
    else:
        return "Reprovado"
#código errado

def teste_aprovado():
    assert verificar_aprovacao(8, 8) == "Aprovado"

def teste_reprovado():
    assert verificar_aprovacao(4, 5) == "Reprovado"

def teste_media_6():
    assert verificar_aprovacao(6, 6) == "Aprovado"
#vai dar erro no teste 3, pois retornaria "reprovado". Pois só seria aceito se a nota fosse > 6.

def verificar_aprovacao(nota1, nota2):
    media = (nota1 + nota2) / 2

    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"
#código corrigido
#corrigimos >= 6, dessa forma se a media for 6 retornaria "aprovado".

