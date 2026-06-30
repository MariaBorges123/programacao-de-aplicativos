import sqlite3

import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    #este bloco quebra ao rodar pela primeira vez em um banco limpo. Por quê?
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS series (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT )''')

    conexao.commit()
    conexao.close()