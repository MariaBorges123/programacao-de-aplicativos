import sqlite3

conexao = sqlite3.connect('secretaria_meio_ambiente.db')
cursor = conexao.cursor()

def cadastrar_tabela_secretaria():
    try:
        conexao = sqlite3.connect('secretaria_meio_ambiente.db')
        cursor = conexao.cursor()
        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS secretaria (
                        id INTEGER PRIMARY KEY,
                        gestao_ano INTEGER NOT NULL,
                        orcamento REAL NOT NULL
                        )
                        ''')
    
        id = int(input("Digite o id desejado: "))
        gestao_ano = int(input("Digite a gestão do ano: "))
        orcamento = float(input("Digite o valor do orçamento: "))
        
        comando_inserir = ('''
                           INSERT INTO secretaria (id, gestao_ano, orcamento) 
                           VALUES (?, ?, ?)''')
        
        cursor.execute(comando_inserir, (id, gestao_ano, orcamento)) 
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
                
    except sqlite3.Error:
        print("erro ao listar secretarias!")

    finally:
        conexao.close()

def alterar_tabela_secretaria():
    try:
        listar_secretaria()
        conexao = sqlite3.connect('secretaria_meio_ambiente.db')
        cursor = conexao.cursor()

        id_secretaria = input("digite a secretaria que deseja alterar: ")

        cursor.execute('''SELECT * FROM secretaria WHERE id = ?''', (id_secretaria,))
        secretarias = cursor.fetchone()
        if not secretarias:
            print("não encontrada!")
        else:
            novo_id = int(input("Digite o novo id: "))
            nova_gestao = input("Digite a nova gestão anual: ")
            novo_valor_orcamento = float(input("Digite o novo valor do orçamento: "))

            comando = ('''UPDATE secretaria 
                           SET id = ?, gestao_ano = ?, orcamento = ?
                           WHERE id = ?''')

            cursor.execute(comando, (
                novo_id,
                nova_gestao,
                novo_valor_orcamento,
                id_secretaria
            ))

            conexao.commit()

            print("\ndepois da alteração:")
            cursor.execute('''SELECT * FROM secretaria WHERE id = ?''', (novo_id,))
            print(cursor.fetchone())

    except ValueError:
        print("erro de valor no novo cadastro tente novamente!")

    except sqlite3.IntegrityError:
        print("erro: este id já está cadastrado!")

    finally:
        conexao.close()

def deletar_secretaria():
    try:
        listar_secretaria()
        novo_id = int(input("Qual id deseja deletar: "))

        conexao = sqlite3.connect('secretaria_meio_ambiente.db')
        cursor = conexao.cursor()

        cursor.execute('''DELETE FROM secretaria WHERE id = ?''', (novo_id,))
        conexao.commit()

        print("secretaria deletada")

    except ValueError:
        print("erro de valor no cadstro!")

    finally:
        conexao.close()


def menu_secretaria():
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

            if opcao == '1': 
                cadastrar_tabela_secretaria()
            elif opcao == '2': 
                listar_secretaria() 
            elif opcao == '3': 
                alterar_tabela_secretaria() 
            elif opcao == '4': 
                deletar_secretaria() 
            elif opcao == '5': 
                break
            else: 
                print("Opção inválida!")

    except ValueError:
        print("erro de valor no cadastro tente novamente!")

    finally:
        print("encerrando programa")


conexao = sqlite3.connect('secretaria_meio_ambiente.db')
cursor = conexao.cursor()

def cadastrar_ecopontos():
    try:
        cursor.execute("PRAGMA foreign_keys = ON")
    
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ecopontos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                endereco TEXT NOT NULL,
                id_secretaria INTEGER NOT NULL,
                FOREIGN KEY (id_secretaria) REFERENCES secretaria (id)
            )''')
    
        id_ecoponto = int(input("Digite o id: "))
        endereco = input("Digite o endereço correspondente: ")
        id_secretaria = int(input("Digite o id da secretaria: "))

        comando_inserir = (''' INSERT INTO ecopontos (id, endereco, id_secretaria)
                            VALUES (?, ?, ?)''')

        cursor.execute(
            comando_inserir,
            (id_ecoponto, endereco, id_secretaria)
        )

        conexao.commit()

    except sqlite3.IntegrityError:
        print("Erro: id inexistente!")
        
    except ValueError:
        print("Erro no valor do cadastro!")


def listar_ecopontos():
    try: 
        cursor.execute(''' SELECT * FROM ecopontos''')
        ecopontos = cursor.fetchall()

        if not ecopontos:
            print("nenhum ecoponto cadastrado")
        else:
            for ecoponto in ecopontos:
                print(f"id = {ecoponto[0]}")
                print(f"endereco = {ecoponto[1]}")
                print(f"id_secretaria = {ecoponto[2]}")

    except sqlite3.Error as e:
        print(f"Erro ao listar ecopontos: {e}")

    finally:
        print("encerrando programa")


def alterar_ecopontos():
    try:
        id_ecopontos = int(input("digite o id do ecoponto: "))

        cursor.execute(
            ''' SELECT * FROM ecopontos WHERE id = ?''',
            (id_ecopontos,))

        ecopontos = cursor.fetchone()

        if not ecopontos: 
            print("ecoponto não encontrado!")
            return

        else: 
            novo_id = int(input("Digite o novo id: "))
            endereco_novo = input("Digite o nome do endereço: ")
            novo_id_secretaria = int(input("Digite o novo id da secretaria: "))

            comando = ('''UPDATE ecopontos 
                           SET id = ?, endereco = ?, id_secretaria = ?
                           WHERE id = ?''')

            cursor.execute(
                comando,
                (
                    novo_id,
                    endereco_novo,
                    novo_id_secretaria,
                    id_ecopontos
                )
            )

            conexao.commit()
            print("ecoponto alterado com sucesso!")

    except ValueError:
        print("erro de valor no cadastro tente novamente")

    except sqlite3.IntegrityError:
        print("erro: secretaria não encontrada!")
    finally:
        print("encerrando programa")


def deletar_ecopontos():
    try:
        listar_ecopontos()
        id_novo = int(input("Digite o id"))

        cursor.execute( '''DELETE FROM ecopontos WHERE id = ?''',
            (id_novo,))

        conexao.commit()
        print("ecoponto deletado")

    except ValueError:
        print("erro de valor, tente novamente!")
    finally:
        print("encerrando programa")


def menu_ecopontos():
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

            if opcao == '1': 
                cadastrar_ecopontos()
            elif opcao == '2': 
                listar_ecopontos() 
            elif opcao == '3': 
                alterar_ecopontos() 
            elif opcao == '4': 
                deletar_ecopontos() 
            elif opcao == '5': 
                break
            else: 
                print("Opção inválida!")
    except ValueError:
        print("erro de valor, tente novamente!")

def menu():
    while True:
        print("\n--- SISTEMA SECRETARIA E ECOPONTOS ---")
        print("1. Secretaria")
        print("2. Ecopontos")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_secretaria()
        elif opcao == '2':
            menu_ecopontos()
        elif opcao == '3':
            break
        else:
            print("Opção inválida!")
conexao.commit()



menu()
conexao.close()
