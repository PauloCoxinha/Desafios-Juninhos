
number = int(input("digite um numero: "))

decimal = []

resultado = "".join(decimal)

dois = 2
def conta(number, decimal):
    while number > 1:
        operacao = number / 2
        number = number // 2
        sequencial = operacao
        if sequencial != number:
            decimal.append(1)
            
        elif sequencial == number:
            decimal.append(0)

print(resultado)

def evil(number):
    
    return "It's Evil!"