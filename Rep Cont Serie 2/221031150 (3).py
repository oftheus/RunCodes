x   =  int(input())
s   = 0
a   = 3
b   = 7

for i in range (0,99):
    if (i%2==0):
        s = s + ((a*x)/b)
    else:
        s = s - ((a*x)/b)
    
    a += 5
    b += 2
soma = s + x

print('%.3f'%soma)