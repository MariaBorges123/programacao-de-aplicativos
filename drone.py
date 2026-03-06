codigo = int(input("digite o código: "))
autorizacao = input("o drone possui autorização? (S/N): ")

if codigo == 999 or autorizacao == "S":

    print("certo! vamos avançar para analise de voo")
    bateria = int(input("digite o nível de bateria de 0 a 100"))
    clima = input("digite se o clima está chuvoso/ensolorado")
    velocidade = float(input("digite a velocidade do vento"))

    if bateria < 10:
        print("AUTORIZADO IMEDIATAMENTE")
        
    elif bateria >= 10: 
        if clima == "ensolorado" and velocidade < 30 or clima == "chuvoso" and velocidade < 10:
            print( "POUSO AUTORIZADO: Iniciando descida.")
        else:
            print("POUSO NEGADO: Condições meteorológicas perigosas. Aguardando em órbita.")


else:
    print("ERRO01: Drone não indentificado. Retornamos a base!")

    
    