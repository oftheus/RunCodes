lista1=[] #quantidade de jogos retirados por cada cliente

for i in range(0,10):
    lista1.append(int(input()))

lista2=[] #quantidade de locações gratuitas por cada cliente
for i in range(0,10):
    lista2.append(int(lista1[i]/5))
    
print(lista2)
