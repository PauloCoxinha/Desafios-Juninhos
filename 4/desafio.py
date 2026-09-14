temperaturas = []

decisao = int(input("Quantos dias voce quer adicionar as temperaturas? ")) 
indice = 1

while indice <= decisao:
    temperatura = float(input(f"Digite a temperatura do dia {indice} (lembre-se de usar o ponto ao invés da virgula e não coloque o simbolo de graus): "))
    temperaturas.append(temperatura)
    indice = indice + 1

def media(a):
    mediaReal = sum(a) / len(a) 
    return mediaReal

maior_temperatura = max(temperaturas)

dia_da_maior = temperaturas.index(maior_temperatura) + 1

def ordem(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

ordem(temperaturas)
temperatura_media = media(temperaturas)

def abaixomedia(temperaturas, temperatura_media):
    dias = 0
    for t in temperaturas:
        if t < temperatura_media:
            dias = dias + 1
        return dias 

dias_abaixo = abaixomedia(temperaturas, temperatura_media)



        


print(f"A maior  temperatura é {temperaturas[-1]} e a menor é {temperaturas[0]}")
print(f"A temperatura média foi de {temperatura_media} Graus")
print(f"Os dias que ficaram abaixo da média foram: {dias_abaixo:.2f}")
print(f"A maior temperatura do dia foi no dia {dia_da_maior}")
print(f"{temperaturas}")

