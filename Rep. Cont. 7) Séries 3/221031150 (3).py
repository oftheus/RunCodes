n = int(input())
ultimo=0
penultimo=1
 
for i in range(n):
    print(ultimo)
    termo     = ultimo + penultimo
    ultimo    = penultimo
    penultimo = termo

