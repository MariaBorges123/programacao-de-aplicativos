import sqlite3

def verificar_registros():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER,
            turma TEXT
        )
        """)

    cursor.execute("SELECT * FROM alunos") 


# Por que o segundo print não mostra absolutamente nada no controle?

    registros = cursor.fetchall()

    print("Primeiro print:", registros)
    print("Segundo print;", registros)

    conexao.close()

verificar_registros()
