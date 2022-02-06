a=int(input())
b=int(input())
for x in range(a,b+1):
    cont=0    
    for y in range(1,x+1):
        if x%y==0: #nº de divisores
            cont+=1
    unidade = x%10
    dezena  = x//10%10
    centena = x//100%10
    soma=unidade+dezena+centena
    
    if cont<=2 and (soma%2==0): #se tiver no max 2 divs é primo
        print(x)
