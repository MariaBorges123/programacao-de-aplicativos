def eh_par(numero):
    if numero % 2 == 0:
        return (True)
    else:
        return (False)
    
usuario = int(input("Digite o numero: "))

if eh_par(usuario):
    print("O número é par")

else:
    print("O número é impar")