#assert: Significa que é uma condição que serve para verificar se é verdadeiro uma informação.
#Se não for veradeiro irá mostrar um erro "AssertionError".

#testes código

#exemplos basicos para entendimentos:

assert 2 + 2 == 4
#verdadeiro
assert 2 + 2 == 5
#erro: AssertionError, pois a informação é verdadeira

#assert com mensagens:

idade = int(input("Digite sua idade: "))

assert idade >= 18
print("Você é maior de idade!")

#exemplo função:

def soma(a, b):
    return a + b

assert soma(2, 3) == 5
assert soma(10, 5) == 15
assert soma(-1, 1) == 0
#o código da certo pois todas as condições de soma da função estão corretas.

#exemplo de testes diferentes:

nome = "João"
idade = 20
lista = [1, 2, 3]

assert nome == "João"
assert idade > 18
assert 2 in lista
assert 4 not in lista
# o código da certo pois as condições são verdadeiras.

#Pytest
# O pytest organiza suas funções, executa e encontra.

def soma(a, b):
    return a + b


def test_soma():
    assert soma(2, 3) == 5
    assert soma(10, 5) == 15
    assert soma(-1, 1) == 0



