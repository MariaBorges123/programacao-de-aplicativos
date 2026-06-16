import sqlite3

def cadastrar_professor():

    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute('''
                    CREAT TABLE IF NOT EXISTS professores(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT,
                    materia TEXT,
                    idade INTEGER,
                    cpf TEXT UNIQUE NOT NULL,
                    salario REAL NOT NULL,
                    escola TEXT NOT NULL,
                   )''')
    
    nome_professor = input("Digite o nome do professor: ")
    telefone_professor = input("Digite o telefone do professor: ")
    materia_professor = input("Digite qual materia ele aplica: ")
    idade_professor = int(input("Digite a idade do novo professor: "))
    cpf_professor = input("Digite o cpf do professor: ")
    salario_professor = float(input("Digite o salario: "))
    nome_escola = input("Digite o nome da escola: ")

    comando_inserir = (f''' INSERT INTO professores (nome , telefone , materia , idade , cpf , salario , escola)
                       VALUES ('{nome_professor}' , '{telefone_professor}' , '{materia_professor}' , {idade_professor} , 
                       '{cpf_professor}' , {salario_professor} , '{nome_escola}')''')
    
    cursor.execute(comando_inserir)
    conexao.commit()

    print("Cadastro realizado com sucesso!")

    conexao.close()


def listar_professor():

    conexao = sqlite3.connect('escola_demostracao.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM professor")
    professor = cursor.fetchall() 