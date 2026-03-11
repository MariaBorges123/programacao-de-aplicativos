senha = input("digite a sua senha: ")
tentativa = int(input("digite o numero da tentativa atual: "))
token = input("digite se você possui token (S/N): ")

if (senha == "admin123") and (tentativa % 3 == 0) or token == "S":
    print(f"Acesso número {tentativa}: ACESSO CONCEDIDO!")
else:
    print(f"Acesso número {tentativa}:ACESSO BLOQUEADO POR PROTOCOLO")
