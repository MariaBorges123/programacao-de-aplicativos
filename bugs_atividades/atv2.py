import sqlite3

def cadastrar_serie(nome_serie, id_escola):
    conexao = sqlite3.connect('sistema_escola.db')
        conexao.execute("PRAGMA foreign_keys = ON") # isso faz com que haja a verificação das chaves estrangeiras
    cursor = conexao.cursor()

# o aluno tenta cadastrar uma serie com id_escola = 999 (que não existe)
# o sqlite aceita o cadastro mesmo assim. O que está faltando ativar?

    try: 
        cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)",
        (nome_serie, id_escola))
        conexao.commit()
    except sqlite3.IntegrityError:
        print("Erro: Escola inexistente!")
    finally:
        conexao.close()


        

