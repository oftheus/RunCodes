n=5
v=[0]*n
z=int(input())
for i in range(z):
    for i in range(n):
        v[i]=int(input())
    move=0    
    for i in range(n):
        for j in range(n-1):
            if (v[j]>v[j+1]):
                move+=1
                t=v[j]
                v[j]=v[j+1]
                v[j+1]=t
    print(move)
