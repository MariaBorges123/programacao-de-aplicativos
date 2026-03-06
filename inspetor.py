comprimento_da_peça = input("O comprimento da peça está entre 10 e 12cm? (S/N): ")

if comprimento_da_peça == "S":
    largura = input("A largura está entre 5 e 6cm? (S/N): ")    
    if largura == "S":  
        print("PEÇA APROVADA!")
    else:
        print("REPROVADO: problema na largura!")

else:
    print("REPROVADO: problema no comprimento!")