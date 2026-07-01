import sqlite3

def criar_tabela _turma():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # O sqlite acusa erro de sintaxe próximo ao FOREIGN KEY. Cade o erro?
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_turma TEXT,
                id_serie,
                FOREIGN KEY (id_serie) REFERENCES series (id)
                )
                ''')

    conexao.commit()
    conexao.close()