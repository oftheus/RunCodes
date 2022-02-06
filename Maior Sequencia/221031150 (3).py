def sequencia(lista, n):

    sequencia = [0] * n
    m = 0

    for i in range(n):
        sequencia[i] = 1

    for i in range(1, n):
        for j in range(i):
            if (lista[i] < lista[j] and sequencia[i] < sequencia[j] + 1):
                sequencia[i] = sequencia[j] + 1

    for i in range(n):
        if (m < sequencia[i]):
            m = sequencia[i]

    return m

n = int(input())

lista = []

for i in range(n):
    lista.append(int(input()))

print(sequencia(lista, n))
