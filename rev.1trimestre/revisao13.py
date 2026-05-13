senha = ""
tentativas = 0

while senha != "123" and tentativas < 3:
    senha = input("Digite a senha: ")
    tentativas += 1

if tentativas == 3:
     print("Acesso negado!")
else:
    print("Acesso liberado!")
