quantidade_registro = int(input("Quantos equipamentos vão ser registrados? "))

equipamentos = {
    
    
}

for i in range(quantidade_registro):
    nome_aparelho = input("Digite o nome do seu aparelho: ")
    potencia_aparelho = float(input(f"Informe o tanto da potencia do seu aparelho sem utilizar virgula, use pontos. o quanto do seu {nome_aparelho} gasta em potencia: "))
    horas_gastas = int(input("Agora por favor você poderia me citar quantas horas você gasta nesse aparelho? (em horas por favor): "))

    consumo_minuto = potencia_aparelho * 60
    consumo_hora = consumo_minuto * 60
    consumo_diario = consumo_hora * horas_gastas

    equipamentos[nome_aparelho] = {"potencia": potencia_aparelho, "Horas de uso": horas_gastas, "Consumo diário": consumo_diario}

print(equipamentos)
    


            




