from datetime import datetime as dt

hoje = dt.today()


quantide_compromisso = int(input("Quantos compromissos voce vai querer adicionar? "))

compromissos_marcados = []

for i in range(quantide_compromisso):
    

    titulo = input("Digite o titulo do seu compromisso: ")
    data_do_compromisso = input("Digite o a data no formato ano/mes/dia: ")
    hora_do_compromisso = input("Agora digite o horario do seu compromisso no formado HH:MM:SS")

    data = dt.strptime(data_do_compromisso, "%Y/%m/%d")
    horario = dt.strptime(hora_do_compromisso, "%H:%M:%S")

    compromissos_marcados.append({"Titulo": titulo, "Data": data, "Horario": horario})


print(compromissos_marcados)


