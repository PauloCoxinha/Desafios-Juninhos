from datetime import datetime as dt

hoje = dt.today()

nascimento = input("Digite sua data de nascimento no formao ano/mes/dia: ")

nascimento_dt = dt.strptime(nascimento, "%Y/%m/%d")

idade =   hoje.year - nascimento_dt.year

if (hoje.month, hoje.day) < (nascimento_dt.month, nascimento_dt.day):
    idade = idade - 1

print(f"Você tem {idade} anos")