A = int(input())
B = int(input())
anos = 0

while A<B:
    A = A + int(0.5 * A)
    B = B + int(0.3 * B)
    anos = anos + 1
print(anos) 



    