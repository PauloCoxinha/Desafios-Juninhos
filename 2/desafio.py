sequencia = []
i = 0
contagem = 0

decisao = int(input("Quantos números voce quer que apareça?  "))

while decisao > len(sequencia):
    i = i + 2
    contagem = contagem + i
    sequencia.append(contagem)


print(sequencia)
    

    

