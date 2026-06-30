import sqlite3

def buscar_professor(id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    #O python reclama de "Incorrect number of bindings"
    #Estamos passando a variavel, por que ocorre erro?
    cursor.execute("SELECT nome FROM professores WHERE id = ?" , (id_prof))
    resultado = cursor.fethone()
    print(resultado)
    conexao.close()
    