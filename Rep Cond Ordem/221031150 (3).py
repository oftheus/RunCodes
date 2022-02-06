x = int(input())
y = int(input())
w = int(input())
z = int(input())
if x<y<w<z:
    print("sim")
elif (x==y) or (y==w) or (w==z):
    h = int(input())
    if (x<=y<=w<=z<=h):
        print('sim')
else:
    print('não')
    

