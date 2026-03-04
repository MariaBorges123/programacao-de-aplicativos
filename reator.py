cargo = input("digite o seu cargo: ")
codigo = input("digite o seu código de acesso: ")
botao = input("o botão de emergencia está pressionado? (S/N): ")
equipamento = input("o equipamento está completo? (S/N): ")

if (cargo == "engenheiro" or cargo == "tecnico") and (codigo == "1234" or botao == "S") and equipamento == "S":
    print("ACESSO LIBERADO!") 
else:
    print("ACESSO NEGADO!")