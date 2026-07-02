def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # Este bloco quebra ao rodar pela primeira vez em um banco limpo. Por quê?
    cursor.execute('''import sqlite3

        CREATE TABLE IF NOT EXISTS series (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_serie TEXT,
            id_escola INTEGER,
            FOREIGN KEY (id_escola) REFERENCES escolas(id)
            )
        ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT
            )
        ''')
        
    conexao.commit()
    conexao.close()
    criar_tabelas()

    #O erro acontece porque a tabela "series" foi criada antes de "escolas". Como a chave "id_escola" depende do banco de dados "escola" ela ira ser criada depois, por isso a chave não vai ser criada do jeito certo