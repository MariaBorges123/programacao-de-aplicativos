import sqlite3

def vincular_aluno_turma():
    nome = input("Nome do aluno: ")
    # Se o usuario digitar "Turma B" em vez do numero do ID, o sistema quebra
    # O try/except abaixo falhou em capturar esse erro. Qual o problema
    try:
        id_turma = int(input("Digite o ID numerico da turma: "))

        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", (nome, id_turma))
        conexao.commit()
    except sqlite3.Error:
        print("Erro no banco de dados!")
    except sqlite3.Error:
        print("Erro de digitação!")
    finally:
        conexao.close()
        
# Não estava dando certo pois faltava um except para indentificação do erro de digitação