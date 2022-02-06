def tribonacci(s, n):
    saida=[]
    if n==0:
        return[]
    for c in range(1,n-2):
        soma=0
        for i in s[-3:]:
            soma+=i
        s.append(soma)
    for qtd_element in s[:n]:
        saida.append(qtd_element)
    return saida

n=int(input())
print(tribonacci([1,1,2],n))
