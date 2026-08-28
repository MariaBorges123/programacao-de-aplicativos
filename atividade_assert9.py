def buscar_nome(lista, nome):
    return nome in lista


def tem_senha_valida(senha):
    return len(senha) >= 8


# Testes para buscar_nome
assert buscar_nome(["Ana", "João", "Carlos"], "Ana") is True # é True pois o nome Ana está na lista
assert buscar_nome(["Ana", "João", "Carlos"], "Maria") is False # é false porque o nome Maria não está dentro da lista
assert buscar_nome([], "Ana") is False # a lista está vazia, logo não tem nenhum nome pra ser encontrado 


# Testes para tem_senha_valida
assert tem_senha_valida("12345678") is True # passa, pois a senha tem exatos 8 caracteres, que é o limite pra senha ser considerada valida
assert tem_senha_valida("1234567") is False # uma senha com 7 caracteres não é valida
assert tem_senha_valida("") is False # a função da errado pois essa senha não possui nenhum caracter, e o minimo é 8
