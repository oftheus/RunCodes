def maior(list1):
  
    m = list1[0]
   
    for x in list1:
        if x > m :
             m = x
      
    return m

def granizo(h):
    lista = []
    lista.append(h)
    while True:
        if h != 1:
            k = h % 2
            if k == 0:
                lista.append(h / 2)
                h = lista[-1]
            elif k != 0:
                lista.append((3 * h) + 1)
                h = lista[-1]
        elif h == 1:
            return maior(lista)
        
h = int(input())
     
q = 4
for c in range(q):
    r = granizo(h)
print(int(r))


