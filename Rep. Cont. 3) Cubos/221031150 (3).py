for c in range (100,1000):
    d1 = c//100
    d2 = (c%100)//10
    d3 = c%10
    if ((d1**3)+(d2**3)+(d3**3)==c):
        print(c)