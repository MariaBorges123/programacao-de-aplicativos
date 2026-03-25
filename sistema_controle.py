autorizados = ["Alice" , "Bob" , "Carlos"]
nome = input ("Digite o nome do pesquisador")
if nome in autorizados:
    indice = autorizados.index(nome)
    print(f"O pesquisador {nome} está na posição {indice}")
    pergunta = input("Deseka remover esse pesquisador da lista? (S/N): ")

    if pergunta == "S":
        autorizados.remove(nome)
        print(f"Agora os membros da lista são: {autorizados}")
    else:
        print("encerrando o programa...")

else:
    print(f"Acesso negado! O pesquisador {nome} não foi encontrado")
    pergunta2 = input("Deseja cadastrar esse novo pesquisador (S/N): ")
    if pergunta == "S":
        autorizados.append(nome)
        print(f"lista autorizada {nome}")
    else:
        print("Encerrando o programa...")