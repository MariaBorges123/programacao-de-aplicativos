id = int(input(" digite o seu id: "))
temperatura = int(input(" digite a temperatura: "))
tempo = int(input("digite o tempo de uso: "))

if (id % 3 == 0) and (temperatura > 40 or tempo > 8):
    print(f"Funcionario {id} você foi escalado para manutenção hoje")
else: 
    print(f"Funcionario {id} sua maquina opera dentro dos padrões")
