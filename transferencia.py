pendentes = ["Relatorio.pdf" , "Foto.png" , "Planilha.xlsx"]
concluidos = []
print(f"Arquivo antigo pendente {pendentes} concluido {concluidos}")
pendentes.pop(0)
concluidos.append("Relatorio.pdf")
print(f"Arquivo novo pendente {pendentes} concluido {concluidos}")