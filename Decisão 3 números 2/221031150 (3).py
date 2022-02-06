a = int(input())
b = int(input())
c = int(input())

if (a+b==c):
    print("soma")

elif (a+c==b):
    print("soma")

elif (b+c==a):
    print("soma")
        
else:
    if(a*b==c):
        print("multi")
    elif(b*c==a):
        print("multi")
    elif(a*c==b):
        print("multi")
    elif(a+b+c)%2==0:
        print("par")
    elif(a+b+c)%2!=0:
        print("ímpar")


    
