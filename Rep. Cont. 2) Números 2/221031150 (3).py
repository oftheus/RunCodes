n=int(input()) #nº de inteiros as serem lidos

c=i=maior=menor=0
p       =  1

while c<n:
    a      = int(input())
    soma   = a+i
    i      = soma
    media  = soma/n
    p      = p*a 
    c+=1
    if c == 1:
        maior = menor = a
    else:
        if a>maior:
            maior=a
        if a<menor:
            menor=a

print('%.2f' %media)
print(i)
print(p)
print(menor)
print(maior)
