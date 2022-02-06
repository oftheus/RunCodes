n = int(input())

x = 0 
y = 1 #x+1=1
z = 2 #x+2=2

c = 0 #contador
    
while c<n:
    x=x+1
    y=y+1
    z=z+1
    c=x*y*z
if c==n:
    print(x)
    print(y)
    print(z)
else:
    print('não')