def pode_entrar(idade, acompanhado):
    if idade >= 18 or acompanhado:
        return True
    return False

assert pode_entrar(24, False)
assert pode_entrar(10, False) == False
assert pode_entrar(10, True) == True
assert pode_entrar(18, False) == True
assert pode_entrar(17, False) == False
assert pode_entrar(17, True) == True