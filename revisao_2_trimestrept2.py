import sqlite3

conexao = sqlite3.connect('academias.db')
cursor = conexao.cursor()

def cadastrar_tabela_academia():
     cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS academias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_academia TEXT NOT NULL,
            bairro_academia TEXT NOT NULL)''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_aluno TEXT NOT NULL,
            mensalidade_aluno INTEGER NOT NULL,
            id_academia INTEGER NOT NULL,
            FOREIGN KEY (id_academia) REFERENCES academias (id)
            )''')

    conexao.commit()

    def cadastrar_academia():
        try:
            print("\n ----ACADEMIA----")
            nome_academia = input("Digite o nome da academia: ")
            bairro_academia = input("Digite o nome do bairro: ")

            cursor.execute("INSERT INTO alunos (nome_aluno, mensalidade_aluno, id_academia), VALUES (?, ?, ?)",
             (nome_aluno, mensalidade_aluno, id_academia))
             conexao.commit()
        except sqlite3.IntegrityError:
            print("Erro: Aluno(a) não encontrado!")

    def cadastrar_aluno_academia():
        try:
            print("\n ----ALUNOS----")
            nome_aluno = input("Digite o nome do aluno: ")
            mensalidade_aluno = int(input("Digite o valor da mensalidade: "))
            id_academia = int(input("Digite o ID da acdemia: "))

            cursor.execute("INSERT INTO academia (nome_academia, bairro_academia) VALUES (?, ?)"
             (nome_academia, bairro_academia))
             conexao.commit()
        except sqlite3.IntegrityError:
            print("Erro: Academia não cadastrada!")

cadastrar_tabela_academia()
cadastrar_academia()
cadastrar_aluno_academia()

conexao.close()



