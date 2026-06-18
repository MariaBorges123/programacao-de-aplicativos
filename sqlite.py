import sqlite3

def cadastrar_aluno():
    
    conexao = sqlite3.connect('escola_demostracao.db')
    cursor = conexao.cursor()

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS alunos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT,
                    turma TEXT,
                    idade INTEGER,
                    cpf TEXT UNIQUE NOT NULL
                )''')

    nome_aluno = input("Digite o nome do aluno: ")
    telefone_aluno = input("Digite o telefone do aluno: ")
    turma_aluno = input("Digite a turma: ")
    idade_aluno = int(input("Digite a idade do novo aluno: "))
    cpf_aluno = input("Digite o cpf do aluno: ")

    comando_inserir = (f'''INSERT INTO alunos(nome, telefone, turma, idade, cpf)
                        VALUES('{nome_aluno}', '{telefone_aluno}', '{turma_aluno}', {idade_aluno} , '{cpf_aluno}')''')

    cursor.execute(comando_inserir)
    conexao.commit()

    print("Cadastro realizado com sucesso!")

    conexao.close()

def listar_aluno():

    conexao = sqlite3.connect('escola_demostracao.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos") #SELECT: BUSCA OS DADOS ; * SIGINIFICA TRAZER TUDO ; FROM: SIGNIFICA QUE OS DADOS BUSCADOS SERAM DA TABELA ALUNOS
    alunos = cursor.fetchall() #SIGNIFICA QUE VAI PEGAR TODOS OS REGISTROS DA CONSULTA

    print("=== Lista de Aluno ===")

    for aluno in alunos: #O PROGRAMA PERCORRE CADA REGISTRO NA LISTA ALUNOS
        print(f"ID: {aluno[0]}")
        print(f"Nome: {aluno[1]}")
        print(f"Telefone: {aluno[2]}")
        print(f"Turma: {aluno[3]}")
        print(f"Idade: {aluno[4]}")
        print(f"CPF: {aluno[5]}")
        print("-" * 30)#SIGNIFICA QUE O - IRÁ SE REPETIR 30x PARA SEPARAR A LISTA DE ALUNOS


def alterar():

    conexao = sqlite3.connect('escola_demostracao.db') #ABRE UMA CONEXÃO DE DADOS DO BANCO
    cursor = conexao.cursor()

    cpf_atual = input("Digite o CPF do aluno que deseja alterar: ") #SOLICITA QUE O USUARIO DIGITE O NOVO CPF 

    cursor.execute(f'''SELECT nome, cpf FROM alunos WHERE cpf = '{cpf_atual}' ''') #SELECIONA O NOME, CPF DE ALUNOS ONDE CPF = CPF ATUAL
    aluno = cursor.fetchone() #FECHA UM

    if aluno is None: #SE O ALUNO FOR "VAZIO" VAI MOSTRAR O PRINT "NÃO ENCONTRADO"
        print("Aluno não encontrado!")
    else:
        print(f"Nome atual: {aluno[0]}")
        print(f"CPF atual: {aluno[1]}")

        novo_nome = input("Digite o novo nome: ") #DIGITE O NOME DO NOVO ALUNO
        novo_cpf = input("Digite o novo CPF: ") #DIGITE O CPF PRO NOVO CADASTRO

        cursor.execute(f'''
                UPDATE alunos #ATUALIZE OS REGISTROS DA TABELA ALUNOS
                SET nome = '{novo_nome}', cpf = '{novo_cpf}' #DEFINE OS VALORES 
                WHERE cpf = {cpf_atual} #INDICA QUAL REGISTRO QUE VAI SER ALTERADO
            ''')
        conexao.commit() #SERVE PARA SALVAR AS ALTERAÇÕES FEITAS 

        print("Dados alterados com sucesso!")

        conexao.close() #FECHA A CONEXÃO COM O BANCO DE DADOS

def excluir_aluno(): #FUNÇÃO CRIADA PRA EXCLUIR ALUNO

    conexao = sqlite3.connect('escola_demostracao.db') #ABRE O BANCO DE DADOS
    cursor = conexao.cursor()

    id_aluno = int(input("Digite o ID do aluno que deseja excluir: ")) #PEDE PRO USUARIO DIGITAR O ID DO ALUNO QUE DESEJA EXCLUIR

    cursor.execute(f'''SELECT nome FROM alunos WHERE id = '{id_aluno}' ''')
    aluno = cursor.fetchone()

    if aluno is None: #VERIFICA SE NENHUM ALUNO FOI ENCONTRADO
        print("Aluno não encontrado!")
    else:
        print(f"Aluno encontrado: {aluno[0]}") #MOSTRA O NOME DO ALUNO ENCONTRADO

        confirmacao = input("Deseja realmente excluir? (s/n): ") #PERGUNTA SE O USUARIO QUER EXCLUIR O ALUNO

        if confirmacao == "s": # SE RESPOSTA FOR IGAUL A "sim" EXECUTE O CURSOR
            cursor.execute(f'''"DELETE FROM alunos WHERE id = {id_aluno}''') #AQUI ATUALIZAMOS OS DADOS
            conexao.commit() #SALVA O ARQUIVO NO BANCO DE DADOS
            print("Aluno excluído com sucesso!")
        else:
            print("Exclusão cancelada.")

    conexao.close() 

excluir_aluno() #CHAMA A FUNÇÃO