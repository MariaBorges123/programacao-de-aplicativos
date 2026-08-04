import sqlite3

conexao = sqlite3.connect('hospital.db')
cursor = conexao.cursor()

def criar_tabela_medicos():
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS hospitais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_hospital TEXT NOT NULL,
            cidade_hospital TEXT NOT NULL
        )''')
    
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS medicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_medico TEXT NOT NULL,
            crm INTEGER NOT NULL,
            id_hospital INTEGER NOT NULL,
            FOREIGN KEY (id_hospital) REFERENCES hospitais(id)
        )''')
    conexao.commit()

def cadastrar_hospitais():

    try:
        print("\n ---HOSPITAL--- ")
        nome_hospital = input("informe o nome do hospital: ")
        cidade_hospital = input("INFORME A CIDADE: ")

        cursor.execute("INSERT INTO hospitais (nome_hospital, cidade_hospital) VALUES (?, ?)", 
        (nome_hospital, cidade_hospital))
        conexao.commit()
    except sqlite3.IntegrityError:
        print("Erro: hospital inexistente!")


def cadastrar_medicos():

    try:
        print("\n ---MEDICO--- ")
        nome_medico = input("nome completo: ")
        crm = int(input("informe o crm: "))
        id_hospital = int(input("informe o id do hospital cadastrado: "))

        cursor.execute("INSERT INTO medicos (nome_medico, crm, id_hospital) VALUES (?, ?, ?)",
        (nome_medico, crm, id_hospital))
        conexao.commit()
    except sqlite3.IntegrityError:
        print("Erro: medico inexistente!")
    
criar_tabela_medicos()
cadastrar_hospitais()
cadastrar_medicos()

conexao.close()