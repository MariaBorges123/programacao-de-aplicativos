import sqlite3

# O aluno criou a conexão fora das funções para "facilitar"
# Por que isso quebra o sistema quando usamos multiplos arquivos (módulos)?


def inserir_escola(nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO escolas (nome) VALUES (?)", (nome,))
    conexao.commit()

# A conexão e o cursor foram criados fora do def, oq faz com que de erro no código