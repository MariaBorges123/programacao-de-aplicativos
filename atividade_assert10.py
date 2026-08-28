def classificar_temperatura(temperatura):

    if temperatura < 15:
        return "Frio"
    elif temperatura <= 25:
        return "Agradável"
    else:
        return "Quente"

assert classificar_temperatura(10) == "Frio"
assert classificar_temperatura(14) == "Frio"
assert classificar_temperatura(15) == "Agradável" #teste limite 
assert classificar_temperatura(25) == "Agradável" #teste limite 
assert classificar_temperatura(26) == "Quente"

# abaixo de 15: "Frio"
# de 15 até 25: "Agradável"
# acima de 25: "Quente"

#o teste assert classificar_temperatura(15) == "Agradável". Esse teste verifica o limite de 15 graus. O código diz que de 15 até 25 graus é agradável, o resultado esperado é ‘Agradável’