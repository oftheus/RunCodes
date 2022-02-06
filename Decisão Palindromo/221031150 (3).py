x = int(input())

d0 = x//1%10
d1 = x//10%10
d2 = x//100%10
d3 = x//1000%10
d4 = x//10000%10

if (d0==d4) and (d1==d3):
    print("sim")
else:
    print("não")