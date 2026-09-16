distancia = int(input("Quantos metros você percorreu? "))

tempo = int(input("Isso em quanto tempo (escreva em segundos, sem pontos ou virgulas)? "))

velocidade_media = distancia / tempo

print(f"A velocidade é de {velocidade_media} m/s")

velocidade_por_km = velocidade_media * 3.6

print(f"A velocidade atingida por km é de {velocidade_por_km} km/h")