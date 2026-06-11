import sqlite3

conexao = sqlite3.connect('escola_demostracao.db')
cursor = conexao.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS alunos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                turma TEXT,
                idade INTEGER,
                cpf TEXT UNIQUE NOT NULL
               )''')

nome_aluno = input("Digite a idade do aluno: ")
telefone_aluno = input("Digite o telefone do aluno: ")
turma_aluno = input("Digite a turma: ")
idade_aluno = int(input("Digite a idade do novo aluno: "))
cpf_aluno = input("Digite o cpf do aluno: ")

comando_inserir = (f'''INSERT INTO alunos(nome, telefone, turma, idade, cpf)
                     VALUES('{nome_aluno}', '{telefone_aluno}', '{turma_aluno}', {idade_aluno} , '{cpf_aluno}')''')

cursor.execute(comando_inserir)
conexao.commit()

print("Cadastro realizado com sucesso!")

conexao.close()

