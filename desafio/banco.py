import sqlite3

def criar_tabela_escola():
    conexao = sqlite3.connect('desafio/gestao_escolar.db') 
    cursor = conexao.cursor()  
    cursor.execute("PRAGMA foreing_keys = ON")

    cursor.execute('''CREATE TABLE IF NOT EXISTS escolas(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_escola TEXT NOT NULL,
                        cidade TEXT NOT NULL)''')

conexao.commit()
conexao.close()

def criar_tabela_turmas():
    conexao = sqlite3.connect('desafio/gestao_escolar.db') 
    cursor = conexao.cursor()  
    cursor.execute("PRAGMA foreing_keys = ON")

    cursor.execute('''CREATE TABLE IF NOT EXISTS turmas(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_turma TEXT NOT NULL,
                        foreing keys (id_escola) REFERENCE escolas (id))''')

conexao.commit()
conexao.close()

def criar_tabela_alunos():
    conexao = sqlite3.connect('desafio/gestao_escolar.db') 
    cursor = conexao.cursor()  
    cursor.execute("PRAGMA foreing_keys = ON")

    cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_aluno TEXT NOT NULL,
                        idade INTEGER NOT NULL,
                        foreing keys (nome_turma) REFERENCE turmas (nome_turma))''')

conexao.commit()
conexao.close()



