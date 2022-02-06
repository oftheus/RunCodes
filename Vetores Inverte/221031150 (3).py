lista1 = []

N = int(input()) #quantidade de nºs da lista

for i in range(N):
    lista1.append(int(input())) #números da lista1

lista2=lista1[:]

#inverter ordem
for i in range(int (N/2)):
    aux = lista2[i]            #auxiliar = valor da posição i da lista 2
    lista2[i]=lista2[N-1-i]    #valor da posição i da lista 2 = tamanho+1-1ªposição ; colocar o 1ºnº na ultima posição
    lista2[N-1-i]= aux         #tamanho+1-1ªposição = auxiliar

#calcular fatorial
lista3=[]
for i in range(N):
    if lista2[i]>=0:
        fatorial=1
        valor=1
        fatorial=lista2[i]
        while fatorial>1:
            valor = valor*fatorial
            fatorial = fatorial-1
        lista3.append(valor)
    else:
        lista3.append(lista2[i])

#print(lista1)
#print(lista2)
print(lista3)
