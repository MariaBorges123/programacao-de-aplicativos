import json #importa para a biblioteca Json, que geralmente é usada para salvar um dado em formato de Json
import os #ele verifica se o arquivo é existente

BANCO_DADOS = 'alunos.json' #Cria uma variavel para armazenar os nomes dos alunos, e "alunos.json" evita que o código fique se repetindo

def cadastrar(): #Cria uma função que tem como objetivo organizar o código
    print("\n--- Novo Cadastro ---") #O print mostra uma mensagem que vai rodar no terminal. O \n serve para pular uma linha

    
    if os.path.exists(BANCO_DADOS): #ele verifica se o arquivo ja existe
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #open: Abre o arquivo
            #r significa read, que ativa o modo de leitura do código
            #encoding serve para salvar caracteres especiais
            #as f: O arquivo chamará f
            alunos = json.load(f) #serve para ler o json e transformar em lista python
    else:
        alunos = []#Cria uma lista sem nada, ou seja, vazia

    novo_aluno = { #Cria um novo objeto com os dados dos alunos
        "nome": input("Nome: "), #pede para digitar o nome do aluno
        "telefone": input("Telefone: "), #pede o telefone
        "turma": input("Turma: "), #pede para digitar a turma
        "idade": int(input("Idade: ")), #pede para digitar a idade
        "cpf": input("CPF: ") #pede para digitar o cpf
    }
    
    alunos.append(novo_aluno) #adiciona o objeto na lista de alunos

    with open(BANCO_DADOS, 'w', encoding='utf-8') as f: # salva no arquivo, w = write substitui o conteudo que esta dentro do arquivo
        json.dump(alunos, f, indent=4, ensure_ascii=False) #json.dump salva os dados no arquivo json
        #indent=4 formata o arquivo
        #ensure_ascii=false é responsavel pela acentuação
        
    print("Aluno cadastrado com sucesso!") #mensagem

def listar(): #função que mostra os alunos
    print("\n--- Lista de Alunos ---") #
    
    if os.path.exists(BANCO_DADOS): #ve se o arquivo existe
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f: #carrega os alunos
            alunos = json.load(f) 
    else:
        alunos = [] #se não existir nenhuma das opções anteriores

    if not alunos: #se não tiver alunos
        print("Nenhum aluno cadastrado.") #exibe a mensagem no terminal
        return #encerra a função

    for aluno in alunos: #laço de repetição
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}") #exibição de dados, string com formatação

def atualizar(): #atualização de dados do aluno
    print("\n--- Atualizar Aluno ---")
    if not os.path.exists(BANCO_DADOS): #verifica o arquivo, se não existir
        print("Nenhum aluno cadastrado no sistema.") #mostrar a mensagem
        return #encerrar o código

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f: 
        alunos = json.load(f)
        
    cpf_busca = input("Digite o CPF do aluno que deseja editar: ")
    
    for aluno in alunos:
        if aluno['cpf'] == cpf_busca:
            print(f"Editando dados de: {aluno['nome']}")
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome']
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
                json.dump(alunos, f, indent=4, ensure_ascii=False)
            print("Dados atualizados com sucesso!")
            return
            
    print("Aluno não encontrado.")

def excluir():
    print("\n--- Excluir Aluno ---")
    if not os.path.exists(BANCO_DADOS):
        print("Nenhum aluno cadastrado no sistema.")
        return

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
        alunos = json.load(f)
        
    cpf_busca = input("Digite o cpf do aluno que deseja remover: ")
    
    nova_lista = [a for a in alunos if a['cpf'] != cpf_busca]
    
    if len(nova_lista) < len(alunos):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado.")

def menu():
    if not os.path.exists(BANCO_DADOS):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump([], f)

    while True:
        print("\n=== SISTEMA ESCOLAR ===")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Excluir Aluno")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1': cadastrar()
        elif opcao == '2': listar()
        elif opcao == '3': atualizar()
        elif opcao == '4': excluir()
        elif opcao == '5': break
        else: print("Opção inválida!")

menu()