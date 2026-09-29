quantidade_registro = int(input("Quantos equipamentos vão ser registrados? "))

equipamentos = {
    
    
}

for i in range(quantidade_registro):
    nome_aparelho = input("Digite o nome do seu aparelho: ")
    potencia_aparelho = float(input(f"Informe o tanto da potencia do seu aparelho sem utilizar virgula, use pontos. o quanto do seu {nome_aparelho} gasta em potencia: "))
    horas_gastas = int(input("Agora por favor você poderia me citar quantas horas você gasta nesse aparelho? (em horas por favor): "))

    consumo_diario = potencia_aparelho * horas_gastas

    equipamentos[nome_aparelho] = {"potencia": potencia_aparelho, "Horas de uso": horas_gastas, "consumo diário WH": consumo_diario}


consumo_total = sum(dados["consumo_diario WH"] for dados in equipamentos.values())

consumo_total_kwh = consumo_total / 1000

aparelho_mais_caro = max(equipamentos, key=lambda k: equipamentos[k]["consumo diário WH"])

print(f"O consumo total dos aparelhos por dia é de {consumo_total_kwh}")
print(f"O aparelho mais caro foi: {aparelho_mais_caro}")
print(equipamentos)
    


            




