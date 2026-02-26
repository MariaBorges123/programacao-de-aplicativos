media = float(input("digite sua media final: "))
presenca = int(input("digite sua presença: "))

if media>= 70.00 and presenca>= 75:
    
    print("Parabéns! você foi apovado")

elif media<70.00 and presenca< 75:
    print("Reprovado, verifique sua nota ou presença")
    