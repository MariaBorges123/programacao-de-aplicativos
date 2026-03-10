garrafa = int(input("Digite o valor total das garrafas: "))

if garrafa == 500:
    print("HORA DA LIMPEZA: Parar máquina imediatamente!")
    print("QUALIDADE: Retirar amostra teste.")

elif garrafa % 500 == 0:
    print("HORA DA LIMPEZA: Parar máquina imediatamente!")

elif garrafa % 100 == 0:
    print("QUALIDADE: Retirar amostra teste.")

else:
    print(f"Produção em dia. Garrafa número {garrafa} processada.")

        
