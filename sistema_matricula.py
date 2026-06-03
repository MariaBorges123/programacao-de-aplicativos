import json
import os

dados = "alunos.json"

def cadastrar():
    if os.path.exists(dados):
        with open(dados, 'r' , encoding= 'utf-8') as estudantes:
            alunos = json.load(estudantes)

    else:
        alunos = []

    novo_aluno = {
        "id": int(input("ID: ")),
        "nome": input("nome: "),
        "telefone": input("Telefone: "),
        "turma": input("turma: "),
        "idade": int(input("idade: ")),
        "cpf": input("CPF: ")
                 }
    
    alunos.append(novo_aluno)

    with open(dados, 'w', encoding= 'utf-8') as estudantes:
        json.dump(alunos, estudantes, indent=4, ensure_ascii=False)
    print("aluno cadastrdado com sucesso!")


def listar(): 
    print("\n--- Atualizar Aluno ---") 
    
    if not os.path.exists(dados):
     with open(dados, 'r', encoding='utf-8') as f: 
        alunos = json.load(f)      
    else:
        alunos = []

    if not alunos:
        print("Nenhum aluno cadastrado!")

        return
    
    for aluno in alunos:
        print(f"Nome: {aluno['nome']} | ID: {aluno['id']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']} CPF: {aluno['cpf']}")

    def atualizar():
        print("\n")