def senha_valida(senha_aprovada):
    while len (senha_aprovada):
        print("senha valida!")
        senha_aprovada = input("Digite a senha: ")
    if len (senha_aprovada) >= 6:
        return True
    else:
        print("Senha invalida, minimo de 6 caracteres")
        return False

senha_usuario = int(input("Digite sua senha: "))
msg = senha_valida(senha_usuario)