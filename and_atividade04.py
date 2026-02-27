usuario = input("digite o nome de usuario: ")
codigo = int(input("digite o codigo: "))

if usuario == "admin" and codigo == 999:
    print("Acesso ao servidor liberado. Sistema online") 
     
else:
    print("Falha na autenticação. Alerta de segurança negado")