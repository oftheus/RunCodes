lista=[]
for i in range(5):
    lista.append(float(input()))
media = (lista[0] + lista[1] + lista[2] + lista[3] + lista[4])/5
menor_dist=-1
n_menor_dist=-1
for i in range(5):
    dife=0
    if lista[i]>=media:
        dife=lista[i]-media
    else:
        dife=media-lista[i]
    if menor_dist == -1 or dife<menor_dist:
        menor_dist = dife
        n_menor_dist = i
print(f"{lista[n_menor_dist]:1.2f}")