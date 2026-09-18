
number = int(input("digite um numero: "))


def conta():
    decimal = []
    global number
    while number > 1:
        resto = number % 2
        decimal.append(resto)
        number = number // 2
    decimal.append(number)

    resultado = "".join(str(x) for x in decimal[::-1])
    return resultado

decimais = conta()

print(decimais)


def evil(a):
    um = a.count("1")
    if um % 2 == 0:

        return "It's Evil!"

    else:
        return "It's Odious!"

verificando = evil(decimais)

print(verificando)

