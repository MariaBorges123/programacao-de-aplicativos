import sqlite3 
 
def cadastrar_escola_manual(): 
	# O aluno resolveu gerar o ID por conta própria 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor()
    try:
        id_escola = int(input("Digite o ID para a nova escola: ")) 
        nome = input("Nome da escola: ") 

        # Se rodar duas vezes com o ID 1, o programa fecha abruptamente (Crash). 
        # Aplique a blindagem protetora necessária: 
        cursor.execute("INSERT INTO escolas (id, nome) VALUES (?, ?)", (id_escola, nome)) 
        
        conexao.commit() 
    except sqlite3.IntegrityError as e:
        print("Erro no sistema, ", e)
    
    finally:
        conexao.close()

cadastrar_escola_manual()
