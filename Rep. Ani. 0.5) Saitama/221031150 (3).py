n = int(input())
m = int(input())
soma=0
k=1

for i in range(1,n+1):
    for j in range(1,m+1):
        soma+= (i**2 * j) / ((3**i) * (j*(3**i) + i * (3**j)))
        j+=1

print('%.4f'%soma)
        
        