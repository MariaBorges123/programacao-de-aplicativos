aluno = input("pergunte se o aluno completou o curso de segurança: ")
if aluno == "S":
    instrutor = input("O instrutor está presente na sala? (S/N): ")
    if instrutor == "S":
        print("Acesso liberado: operação iniciada!")
    else:
        print("acesso negado: aguarde o instrutor para ligar a maquina!")
    
else:
    print("Acesso negado: faça o treinamento primeiro")


