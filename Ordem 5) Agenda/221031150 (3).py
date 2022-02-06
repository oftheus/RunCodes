agenda = []
n=int(input())
for c in range(n):
    x=int(input())
    if c==0 or x>agenda[-1]:
        agenda.append(x)
    else:
        pos=0
        while pos<len(agenda):
            if x <= agenda[pos]:
                agenda.insert(pos, x)
                break
            pos+=1
    print(agenda)






