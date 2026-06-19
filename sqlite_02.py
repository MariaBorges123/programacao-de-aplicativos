import sqlite3

def cadastrar_professor():

    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS professores(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT,
                    materia TEXT,
                    idade INTEGER,
                    cpf TEXT UNIQUE NOT NULL,
                    salario REAL NOT NULL,
                    escola TEXT NOT NULL
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

    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    cursor.execute('''SELECT * FROM professores''')
    professores = cursor.fetchall() 

    print("===lista de professores===")

    for professor in professores:
        print(f"ID: {professor[0]}")
        print(f"Nome: {professor[1]}")
        print(f"Telefone: {professor[2]}")
        print(f"Turma: {professor[3]}")
        print(f"Idade: {professor[4]}")
        print(f"CPF: {professor[5]}")
        print("-" * 30)

def alterar_nome_cpf():

    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor() 

    cpf_atual = input("Digite o CPF do professor que deseja alterar: ")

    cursor.execute(f'''SELECT nome, cpf FROM professores WHERE cpf = '{cpf_atual}' ''')
    professor = cursor.fetchone()

    if professor is None: 
        print("Professor não encontrado!")
    else:
        print(f"Nome atual: {professor[0]}")
        print(f"CPF atual: {professor[1]}")

        novo_nome = input("Digite o novo nome: ")
        novo_cpf = input("Digite o novo CPF: ")

        cursor.execute(f'''
                UPDATE professores 
                SET nome = '{novo_nome}', cpf = '{novo_cpf}' 
                WHERE cpf = {cpf_atual} 
            ''')
        conexao.commit()

        print("Dados alterados com sucesso!")

        conexao.close()

def excluir_professor():

    conexao = sqlite3.connect('escola_demonstracao.db')
    cursor = conexao.cursor()

    id_professor = int(input("Digite o ID do professor que deseja excluir: ")) 

    cursor.execute(f'''SELECT nome FROM professores WHERE id = '{id_professor}' ''')
    professor = cursor.fetchone()

    if professor is None: 
        print("Professor não encontrado!")
    else:
        print(f"Professor encontrado: {professor[0]}") 

        confirmacao = input("Deseja realmente excluir? (s/n): ") 

        if confirmacao == "s":
            cursor.execute(f'''"DELETE FROM professores WHERE id = {id_professor}''') 
            conexao.commit() 
            print("Professor excluído com sucesso!")
        else:
            print("Exclusão cancelada.")

    conexao.close() 

def menu():

    while True:
        print("\n --- TABELA DE PROFESSORES ---")
        print("\n === SISTEMA ESCOLAR ===")
        print("1. Cadastrar professor ")
        print("2. Listar professor ")
        print("3. Atualizar professor ")
        print("4. Deletar professor ")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1': cadastrar_professor()
        elif opcao == '2': listar_professor()
        elif opcao == '3': alterar_nome_cpf()
        elif opcao == '4': excluir_professor()

        else:
            print("Opção invalida")
menu()




