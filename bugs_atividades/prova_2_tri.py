import sqlite3

conexao = sqlite3.connect('sistema_secretaria_ambiente.db')
cursor = conexao.cursor()

def cadastrar_tabela_secretaria():
    try:
        conexao = sqlite3.connect('sistema_secretaria_ambiente.db')
        cursor = conexao.cursor()
        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS sistemas_secretaria_ambiente,
                        id INTEGER PRIMAY KEY,
                        gestao_ano INTEGER NOT NULL,
                        orcamento FLOAT NOT NULL
                        ''')
    
        id = int(input("Digite o id desejado: "))
        gestao_ano = int(input("Digite a gestão do ano: "))
        orcamento = float(input("Digite o valor do orçamento: "))
        
        comando_inserir = (f'''
                           INSERT INTO sistema_secretaria_ambiente (id, gestao ano, ocamento) 
                           VALUES ('{id}', '{gestao_ano}', '{orcamento}')''')
        
        cursor.execute(comando_inserir) 
        conexao.commit()
        
    except sqlite3.IntegrityError: 
        print("Erro: Este id já está cadastrado no sistema!") 

    except sqlite3.Error:
        print("Erro no codigo, tente novamente!")

    finally:
        conexao.close()

def listar_secretaria():
    try: 
        conexao = sqlite3.connect('secretaria_meio_ambiente.db')
        cursor = conexao.cursor()
        cursor.execute(''' SELECT * FROM secretaria''')
        secretarias = cursor.fetchall()
        if not secretarias:
            print("nenhuma secretaria cadastrada!")
        else:
            for secretaria in secretarias:
                print(f"id: {secretaria[0]}")
                print(f"gestão ano: {secretaria[1]}")
                print(f"orçamento: {secretaria[2]}")
                
    except TypeError:
        print("erro de tipo de dados")
    finally:
        conexao.close()

def alterar_tabela_secretaria():
    try:
        listar()
        conexao = sqlite3.connect('secretaria_meio_ambiente')
        cursor = conexao.cursor()

        id_secretaria = input("digite a secretaria que deseja alterar: ")

        cursor.execute(f'''SELECT * FROM WHERE id = {id_secretaria} ''')
        secretarias = cursor.fetchone()
        if not id_secretaria:
            print("não encontrada!")
        else:
            novo_id = int(input("Digite o novo id: "))
            nova_gestao = input("Digite a nova gestão anual: ")
            novo_valor_orcamento = int(input("Digite o novo valor do orçamento: "))

            print("\ndepois da alteração:")
            print(cursor.fetchone())
            comando = (f'''UPDATE secretarias SET id = '{novo_id}', gestao = '{nova_gestao}', orcamento = '{novo_valor_orcamento}''')
        conexao.commit()

    except ValueError:
        print("erro de valor no novo cadastro tente novamente!")

    finally:
        conexao.close()

def deletar_secretaria():
    try:
        listar_secretaria()
        novo_id = int(input("Qual id deseja deletar: "))
        cursor.execute(f'''DELETE FROM secretaria WHERE id = {novo_id}''')
        conexao.commit()
        print("secretaria deletada")
    except ValueError:
        print("erro de valor no cadstro!")
    finally:
        print("encerrando programa...")

def menu():
    try:
        while True:
            print("\n--- TABELA SECRETARIA ---")
            print("\n SISTEMA SECRETARIA ")  
            print("1. Cadastrar secretaria") 
            print("2. Listar secretaria") 
            print("3. Atualizar secretaria") 
            print("4. Excluir secretaria") 
            print("5. Sair")
                
            opcao = input("Escolha uma opção: ")

            if opcao == '1': cadastrar_tabela_secretaria()
            elif opcao == '2'listar_secretaria() 
            elif opcao == '3': alterar_tabela_secretaria() 
            elif opcao == '4': deletar_secretaria() 
            elif opcao == '5': break
            else: 
                print("Opção inválida!")
except ValueError:
        print("erro de valor no cadastro tente novamente!")
finally:
        print("encerrando programa")


conexao = sqlite3.connect('secretaria_meio_ambiente.db')
cursor = conexao.cursor()

def cadastrar_ecopontos():
    cursor.execute("PRAGMA foreign_keys = ON")
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ecopontos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            endereco TEXT NOT NULL
            FOREIGN KEY (id_secretaria) REFERENCES (id)
        )''')
    
    id_ecoponto = int(input("Digite o id: "))
    endereco = input("Digite o endereço correspondente: ")

    comando_inserir = (f''' INSERT INTO ecopontos (id, endereco)
                            VALUES ('{id_ecoponto}', '{endereco}')''')

    cursor.execute(comando_inserir)
    conexao.commit()

    except sqlite3.IntegrityError:
        print("Erro: id inexistente!")
    except ValueError:
        print("Erro no valor do cadastro!")

def listar_ecopontos():
    try: 
        cursor.execute(''' SELECT * FROM ecopontos''')
        professores = cursor.fetchall()
        if not ecopontos:
            print("nenhum professor cadastrado")
        else:
            for ecoponto in ecopontos:
                print(f"id = {ecoponto[0]}")
                print(f"endereco = {ecoponto[1]}")
                print(f"id_secretaria = {ecoponto[2]}")

    except Sqlite3.Error as e:
        print(f"Erro ao listar ecopontos: {e}")
    finally:
        print("encerrando programa")

def alterar_ecopontos():
    try:
        id_ecopontos = int(input("digite o id do professor: "))
        cursor.execute(f''' SELECT * FROM ecopontos WHERE id = {id_secretaria}''')
        ecopontos = cursor.fetchone()
        if not ecopontos: 
            print("ecoponto não encontrado!")
            return
        else: 
            novo_id = int(input("Digite o novo id: "))
            endereco_novo = input("Digite o nome do endereço: ")

            comando = (f'''UPDATE ecopontos '{novo_id}' endereco = '{endereco_novo}''')
    except ValueError:
        print("erro de valor no cadastro tente novamente")
    finally:
        print("encerrando programa")

def deletar_ecopontos():
    try:
        listar_ecopontos()
        id_novo = int(input("Digite o id"))
        cursor.execute(f'''DELETE FROM ecopontos WHERE id = {id_novo}''')
        conexao.commit()
        print("ecoponto deletado")
    except ValueError:
        print("erro de valor no cadastro, tente novamente!")

def menu():
    try:
        while True:
            print("\n--- TABELA ECOPONTO ---")
            print("\n SISTEMA ECOPONTO ")  
            print("1. Cadastrar ecoponto") 
            print("2. Listar ecoponto") 
            print("3. Atualizar ecoponto") 
            print("4. Excluir ecoponto") 
            print("5. Sair")
                
            opcao = input("Escolha uma opção: ")

            if opcao == '1': cadastrar_ecopontos()
            elif opcao == '2'listar_ecopontos() 
            elif opcao == '3': alterar_ecopontos() 
            elif opcao == '4': deletar_ecopontos() 
            elif opcao == '5': break
            else: 
                print("Opção inválida!")

menu()
conexao.close()




       

                


        