usuarios = ["admin" , "convidado" , "suporte" , "teste"]
print(f"lista antiga: {usuarios}")
usuarios.remove("teste")
del usuarios[0]
print(f"A lista atual é: {usuarios}")