lista=[]
for i in range(0,10):
    lista.append(int(input())) #digite um nº para posição

n=int(input()) #nº a ser comparado
lista2=[] #lista de posições dos nº repetidos

for c,v in enumerate(lista): #c = posição ; v = número
    if v==n:
        lista2.append(c) #colocar as posições que repetem na lista2
print(lista2)
