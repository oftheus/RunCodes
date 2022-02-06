A = int(input())
B = int(input())
C = int(input())

print("%.1f"%((A+B+C)/3))
print(A+B+C)
print(A*B*C)

if (A<=B<=C):
    print(A)
elif (B<=A<=C):
    print(B)
else:
    print(C)

if (A>=B>=C):
    print(A)
elif (B>=A>=C):
    print(B)
else:
    print(C)