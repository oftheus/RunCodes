n = int(input())
m = int(input())

lista1 = []
lista2 = []

for i in range(n):
    lista1.append(int(input()))

for i in range(m):
    lista2.append(int(input()))
    
lista3 = []

for i in range(max(n,m)):
    if i<n:
        lista3.append(lista1[i])
    if i<m:
        lista3.append(lista2[i])

print(lista3)