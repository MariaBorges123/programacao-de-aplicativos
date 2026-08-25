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

            


        