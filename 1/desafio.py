boletim = {}

print("Digite 'sair' caso você tenha finalizado o cadastro das notas ")


while True:

    nome = input('Digite o nome do aluno: ').upper()


    if nome == 'SAIR':
        break

    nota = float(input(f"Digite a nota de {nome}: "))

    if nome not in boletim:
        boletim[nome] = []

    boletim[nome].append(nota)

print("\n NOTA FINAL  -----")
print(boletim)