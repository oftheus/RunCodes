resp=1
while(resp==1):
    x = int(input())
    termo1=1
    termo2=2
    if (x==1):
        print(1)
    elif(x==2):
        print(1)
        print(2)
    else:
        print(termo1)
        print(termo2)
    for c in range(0,x-2):
        termo3=(termo1*termo2)+1
        termo1=termo2
        termo2=termo3
        print(termo3)
    resp=int(input())
    