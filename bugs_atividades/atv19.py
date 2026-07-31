import sqlite3

def buscar_dados_dinamicos(nome_tabela, id_registro):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # O SQLite joga um erro de sintaxe operacional indicando que não aceita o
    # caractere '?'.
    # Não podemos parametrizar nomes de tabelas? Como resolver mantendo a segurança?
    cursor.execute(f"SELECT * FROM {nome_tabela} WHERE id = ?" , (id_registro,))

    print(cursor.fetchone())

    conexao.close()

nome_tabela = input("digite o nome da tabela:" )
id_registro = int(input("digite o id_registro:  "))

buscar_dados_dinamicos(nome_tabela, id_registro)


