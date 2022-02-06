pedra   = 0
spock   = 1
papel   = 2
lagarto = 3
tesoura = 4

vitorias1 = 0
vitorias2 = 0
empates   = 0

jogador1_1partida = int(input())
jogador2_1partida = int(input())

if jogador1_1partida == jogador2_1partida:
    empates += 1
    
elif jogador1_1partida == 0:
    if jogador2_1partida == 1:
        vitorias2 += 1
    elif jogador2_1partida == 2:
        vitorias2 += 1
    elif jogador2_1partida == 3:
        vitorias1 += 1
    elif jogador2_1partida == 4:
        vitorias1 += 1
    
elif jogador1_1partida == 1:
    if jogador2_1partida == 0:
        vitorias1 += 1
    elif jogador2_1partida == 2:
        vitorias2 += 1
    elif jogador2_1partida == 3:
        vitorias2 += 1
    elif jogador2_1partida == 4:
        vitorias1 += 1
        
elif jogador1_1partida == 2:
    if jogador2_1partida == 0:
        vitorias1 += 1
    elif jogador2_1partida == 1:
        vitorias1 += 1
    elif jogador2_1partida == 3:
        vitorias2 += 1
    elif jogador2_1partida == 4:
        vitorias2 += 1

elif jogador1_1partida == 3:
    if jogador2_1partida == 0:
        vitorias2 += 1
    elif jogador2_1partida == 1:
        vitorias1 += 1
    elif jogador2_1partida == 2:
        vitorias1 += 1
    elif jogador2_1partida == 4:
        vitorias2 += 1
    
elif jogador1_1partida == 4:
    if jogador2_1partida == 0:
        vitorias2 += 1
    elif jogador2_1partida == 1:
        vitorias2 += 1
    elif jogador2_1partida == 2:
        vitorias1 += 1
    elif jogador2_1partida == 3:
        vitorias1 += 1
        
jogador1_2partida = int(input())
jogador2_2partida = int(input())

if jogador1_2partida == jogador2_2partida:
    empates += 1
    
elif jogador1_2partida == 0:
    if jogador2_2partida == 1:
        vitorias2 += 1
    elif jogador2_2partida == 2:
        vitorias2 += 1
    elif jogador2_2partida == 3:
        vitorias1 += 1
    elif jogador2_2partida == 4:
        vitorias1 += 1
    
elif jogador1_2partida == 1:
    if jogador2_2partida == 0:
        vitorias1 += 1
    elif jogador2_2partida == 2:
        vitorias2 += 1
    elif jogador2_2partida == 3:
        vitorias2 += 1
    elif jogador2_2partida == 4:
        vitorias1 += 1
        
elif jogador1_2partida == 2:
    if jogador2_2partida == 0:
        vitorias1 += 1
    elif jogador2_2partida == 1:
        vitorias1 += 1
    elif jogador2_2partida == 3:
        vitorias2 += 1
    elif jogador2_2partida == 4:
        vitorias2 += 1

elif jogador1_2partida == 3:
    if jogador2_2partida == 0:
        vitorias2 += 1
    elif jogador2_2partida == 1:
        vitorias1 += 1
    elif jogador2_2partida == 2:
        vitorias1 += 1
    elif jogador2_2partida == 4:
        vitorias2 += 1
    
elif jogador1_2partida == 4:
    if jogador2_2partida == 0:
        vitorias2 += 1
    elif jogador2_2partida == 1:
        vitorias2 += 1
    elif jogador2_2partida == 2:
        vitorias1 += 1
    elif jogador2_2partida == 3:
        vitorias1 += 1

jogador1_3partida = int(input())
jogador2_3partida = int(input())

if jogador1_3partida == jogador2_3partida:
    empates += 1
    
elif jogador1_3partida == 0:
    if jogador2_3partida == 1:
        vitorias2 += 1
    elif jogador2_3partida == 2:
        vitorias2 += 1
    elif jogador2_3partida == 3:
        vitorias1 += 1
    elif jogador2_3partida == 4:
        vitorias1 += 1
    
elif jogador1_3partida == 1:
    if jogador2_3partida == 0:
        vitorias1 += 1
    elif jogador2_3partida == 2:
        vitorias2 += 1
    elif jogador2_3partida == 3:
        vitorias2 += 1
    elif jogador2_3partida == 4:
        vitorias1 += 1
        
elif jogador1_3partida == 2:
    if jogador2_3partida == 0:
        vitorias1 += 1
    elif jogador2_3partida == 1:
        vitorias1 += 1
    elif jogador2_3partida == 3:
        vitorias2 += 1
    elif jogador2_3partida == 4:
        vitorias2 += 1

elif jogador1_3partida == 3:
    if jogador2_3partida == 0:
        vitorias2 += 1
    elif jogador2_3partida == 1:
        vitorias1 += 1
    elif jogador2_3partida == 2:
        vitorias1 += 1
    elif jogador2_3partida == 4:
        vitorias2 += 1
    
elif jogador1_3partida == 4:
    if jogador2_3partida == 0:
        vitorias2 += 1
    elif jogador2_3partida == 1:
        vitorias2 += 1
    elif jogador2_3partida == 2:
        vitorias1 += 1
    elif jogador2_3partida == 3:
        vitorias1 += 1

print(vitorias1)
print(vitorias2)
print(empates)



