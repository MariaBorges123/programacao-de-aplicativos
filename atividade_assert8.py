def pode_votar(idade):
    return idade >= 16


#testando
assert pode_votar(15) is False #correto
assert pode_votar(16) is True #correto
assert pode_votar(17) is True #correto
#todos os testes estão certos