def criar_arquivo():

    open('viagens.txt' , 'w').close()

def criar():
    adicionar = input("Digite o destino desejado: ")
    with open('viagens.txt' , 'a') as viagem:
        viagem.write(adicionar + '\n')
    print("Destino da viagem adicionado!")

def ler():
    with open('viagens.txt', 'r') as viagem:
        destinos = viagem.readlines()

        i=0
        for destino in destinos:
            print(f"{i} - {destino.strip()}")
            i+=1

def atualizar():
    ler()
    idx = int(input("Digite o id do destino que deseja alterar: "))
    novo_destino = input("Novo destino: ")

    with open('viagens.txt' , 'r') as viagem:
        linhas = viagem.readlines()

        linhas[idx] = novo_destino + '\n'

        with open('viagens.txt' , 'w') as viagem:
            viagem.writelines(linhas)
        print("Destino atualizado!")

def deletar():
    ler()
    deletar = int(input("Digite o destino que deseja deletar")) 
    
    with open('viagem.txt' , 'r') as viagem:
        linhas = viagem.writelines()
        
    del linhas[deletar]
    
    with open('viagem.txt' , 'w') as viagem:
        viagem.writelines(linhas)
    print("Destino removido!")

while True:
    print("\n1-Cadastrar  \n2-Listar  \n3-Editar  \n4-Excluir  \n5-sair")
    opcao = input("Escolha: ")

    if opcao == '1': criar()
    elif opcao == '2': ler()
    elif opcao == '3': atualizar()
    elif opcao == '4': deletar()
    elif opcao == '5': break