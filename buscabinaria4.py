def buscar_nome(alunos, nome):
    indice = 0

    for aluno in alunos:
        if nome == aluno:
            print("O aluno foi encontrado na posição:", indice)
            return
        indice += 1

        print("O aluno não foi encontrado.")

alunos = ["Ana", "Carlos", "João", "Maria", "Pedro"]
nome = input("Digite o nome que você deseja procurar: ")

   


buscar_nome(alunos, nome)

