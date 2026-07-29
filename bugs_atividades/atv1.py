import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
    '    CREATE TABLE IF NOT EXISTS escolas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
        )
    ''')'
# o banco não está salvando as alterações. Por quê?
    conexao.commit() #faltava o conexao.commit para armazenar os dados
    conexao.close()