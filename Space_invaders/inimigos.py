import random
from config import window, mouse, keyboard
from pplay.sprite import Sprite


def matriz_inimigos(linhas, colunas):
    global velx_monstros
    velx_monstros = 450

    matriz_inimigos = []
    for i in range(linhas):
        lista_inimigos = []
        matriz_inimigos.append(lista_inimigos)
        for j in range(colunas):
            inimigos1 = Sprite('./Space_invaders/Sprites/game/inimigo1.png')
            inimigos1.set_position((inimigos1.width + inimigos1.width/2) * j,(inimigos1.height + inimigos1.height/2) * i )
            lista_inimigos.append(inimigos1)
    return matriz_inimigos


def inimigos(matriz_inimigos):
    global velx_monstros

    for k in range(len(matriz_inimigos)):
        for y in range(len(matriz_inimigos[k])):    
                matriz_inimigos[k][y].x += velx_monstros * window.delta_time()
                matriz_inimigos[k][y].draw()
    
    inverter = False
    for linha in matriz_inimigos:
        if linha: 
            if linha[-1].x + linha[-1].width >= window.width or linha[0].x <= 0:
                inverter = True
                break

    if inverter:
        velx_monstros *= -1
        for linha in matriz_inimigos:
            for inimigo in linha:
                inimigo.y += 40
                if velx_monstros > 0 and inimigo.x < 0:
                    inimigo.x = 0
                elif velx_monstros < 0 and inimigo.x + inimigo.width > window.width:
                    inimigo.x = window.width - inimigo.width


tiros_inimigos_lista = []
ultimo_tiro = 0

def tiros_inimigos(matriz_inimigos, tempo_ultimo_tiro, nave, nave_imortal, escudo, escudo_helf):
    global tiros_inimigos_lista

    tempo_ultimo_tiro += window.delta_time()

    if tempo_ultimo_tiro >= 2.5:
        colunas_validas = [linha for linha in matriz_inimigos if linha]
        if colunas_validas:
            linha_aleatoria = random.choice(colunas_validas)
            inimigo_aleatorio = random.choice(linha_aleatoria)
            tiro = Sprite('./Space_invaders/Sprites/game/projetil_inimigo.png')
            tiro.set_position(
                inimigo_aleatorio.x + inimigo_aleatorio.width/2 - tiro.width/2,
                inimigo_aleatorio.y + inimigo_aleatorio.height
            )
            tiros_inimigos_lista.append(tiro)
        tempo_ultimo_tiro = 0

    vel_tiro = 400
    atingiu_nave = False
    for i in range(len(tiros_inimigos_lista)-1, -1, -1):
        tiro = tiros_inimigos_lista[i]
        tiro.y += vel_tiro * window.delta_time()
        tiro.draw()
        # Colisão com a nave (só se não estiver imortal)
        if not nave_imortal and tiro.collided(nave):
            tiros_inimigos_lista.pop(i)
            atingiu_nave = True
        # Colisão com escudo
        elif escudo and tiro.collided(escudo):
            tiros_inimigos_lista.pop(i)
            escudo.x = -1000  # "Remove" o escudo da tela
        # Colisão com escudo_helf
        elif escudo_helf and tiro.collided(escudo_helf):
            tiros_inimigos_lista.pop(i)
            escudo_helf.x = -1000  # "Remove" o escudo_helf da tela
        elif tiro.y > window.height:
            tiros_inimigos_lista.pop(i)

    return tempo_ultimo_tiro, atingiu_nave
    


    

        
    



