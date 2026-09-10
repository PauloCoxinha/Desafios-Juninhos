notas = []


print("Caso queira sair digite 'n' ")


while True:
    nota = float(input("Informe a nota do aluno: "))
    notas.append(nota)
    decisao = input("Deseja continuar? s/n: ")

    if decisao == 'n':
        break

def media(a):
    medias = sum(a) / len(a)
    return medias

def ordem(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def passou(a):
    i = 0 
    for n in a:
        if n >= 7.0:
           i = i + 1
    return i

def naopassou(a):
    i = 0
    for n in a:
        
        if n <= 7.0:
            
            i = i + 1
    return i
    
ordem(notas)

print(f" a média da turma foi: {media(notas):.2f}")

print(f"Na nossa turma atual {naopassou(notas)} foram reprovados e apenas {passou(notas)} passaram de ano")

print(f"a menor nota é {notas[0]} e a maior é {notas[-1]}")

print(notas)