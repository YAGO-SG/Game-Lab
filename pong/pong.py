from pplay.window import *
from pplay.sprite import *
import random
import time

#configurações da janela
janela = Window(width=1200, height=600)
janela.set_title('yago santos gois')
teclado = janela.get_keyboard()
espaço = 0

#configurações da bolinha
bolinha = Sprite('./pong/bolinha.png', frames=1)
bolinha.set_position(janela.width/2 - bolinha.width/2 , janela.height/2 - bolinha.height/2)
velx = 450
vely = -404

#configurações da barra
barra1 = Sprite('./pong/bar.png', frames = 1)
barra2 = Sprite('./pong/bar.png', frames = 1)
barra1.set_position(barra1.width ,janela.height/2 - barra1.height/2)
barra2.set_position(janela.width - 2 * barra2.width, janela.height/2 - barra2.height/2)
BarVelUp = 500
BarVelDown = 500
velocidade_IA = 385

#variáveis do placar
ponto_player = 0
ponto_IA = 0

background = Sprite('./pong/background.jpg', frames=1);
background.set_position(janela.width/2 - background.width/2 , janela.height/2 - background.height/2);


barra_horizontal = Sprite('./pong/bar_horizontal.png', frames = 1) 
barra_horizontal2 = Sprite('./pong/bar_horizontal.png', frames = 1)
barra_horizontal.set_position(janela.width/2 - bolinha.width - 20, janela.height - barra_horizontal.height - 25)
barra_horizontal2.set_position(janela.width/2 - bolinha.width - 20, 25)
velbarh = 600
velbarhia = 600
random.seed(time.time())
numero_normal = random.randint(5, 10)
numero_modificado = random.randint(5, 10)
print(numero_normal)
print(numero_modificado)
tempo1 = 0
tempo2 = 0
modo = 1

while True:
    janela.set_background_color([0, 93, 171])
    

    #funcionalidade de iniciar com a tecla 'espaço'
    if teclado.key_pressed("SPACE") or espaço == 1:
            bolinha.x += janela.delta_time() * velx
            bolinha.y += janela.delta_time() * vely
            espaço = 1
            tempo1 += janela.delta_time()
            tempo2 += janela.delta_time()
            print(tempo1)

    if tempo1 > numero_normal:
        modo = modo * -1
        tempo1 = 0
    
    

    if modo == 1:
        #limite da bolinha nas verticais
        if bolinha.y >= janela.height - bolinha.height:
            bolinha.y = (janela.height - bolinha.height) - 1
            vely = vely * -1
        elif bolinha.y <= 0:
            bolinha.y = 1
            vely = vely * -1

        #movimentação da barra da esquerda
        if teclado.key_pressed("UP") and barra1.y >= 0:
            barra1.y -= BarVelUp * janela.delta_time()
        elif teclado.key_pressed("DOWN") and barra1.y <= janela.height - barra1.height:  # Direcional \/
            barra1.y += BarVelDown * janela.delta_time()
        
        #movimentação da barra da direita(IA)
        if barra2.y + barra2.height / 2 < bolinha.y:
            barra2.y += velocidade_IA * janela.delta_time()
        elif barra2.y + barra2.height / 2 > bolinha.y:
            barra2.y -= velocidade_IA * janela.delta_time()
        barra2.y = max(0, min(barra2.y, janela.height - barra2.height))

        #colisão da barra com a bolinha
        if barra1.collided(bolinha):
            bolinha.x = barra1.x + barra1.width 
            velx = velx * -1
        elif barra2.collided(bolinha):
            bolinha.x = barra2.x - bolinha.width
            velx = velx * -1


        #Placar e reset da partida
        if bolinha.x <= 1:
            ponto_IA += 1
            bolinha.set_position(janela.width/2 - bolinha.width/2 , janela.height/2 - bolinha.height/2)
            espaço = 0
        elif bolinha.x >= janela.width:
            ponto_player += 1
            bolinha.set_position(janela.width/2 - bolinha.width/2 , janela.height/2 - bolinha.height/2)
            espaço = 0
        janela.draw_text(str(ponto_player), (janela.width / 4), 50, size = 70, color = (150, 200, 50), font_name = "placar", bold = False, italic = False )
        janela.draw_text(str(ponto_IA), (2 * janela.width / 3) + bolinha.width, 50, size = 70, color = (150, 200, 50), font_name = "placar", bold = False, italic = False )

        background.draw()
        bolinha.draw()
        barra2.draw()
        barra1.draw()


    elif modo == -1:
        #limite da bolinha nas horizontais
        if bolinha.x >= janela.width - bolinha.width - 1:
            bolinha.x = (janela.width - bolinha.width) - 2
            velx = velx * -1
        elif bolinha.x <= 0:
            bolinha.x = 1
            velx = velx * -1

        #movimentação da barra da esquerda
        if teclado.key_pressed("LEFT") and barra_horizontal.x >= 0:
            barra_horizontal.x -= velbarh * janela.delta_time()
        elif teclado.key_pressed("RIGHT") and barra_horizontal.x <= janela.width - barra_horizontal.width:  # Direcional \/
            barra_horizontal.x += velbarh * janela.delta_time()
        
        #movimentação da barra de cima(IA)
        if barra_horizontal2.x + barra_horizontal2.width / 2 < bolinha.x:
            barra_horizontal2.x += velbarhia * janela.delta_time()
        elif barra_horizontal2.x + barra_horizontal2.width / 2 > bolinha.x:
            barra_horizontal2.x -= velbarhia * janela.delta_time()

        barra_horizontal2.x = max(0, min(barra_horizontal2.x, janela.width - barra_horizontal2.width))

        #colisão da barra com a bolinha
        if barra_horizontal2.collided(bolinha):
            bolinha.y = barra_horizontal2.y + barra_horizontal2.height 
            vely = vely * -1
        elif barra_horizontal.collided(bolinha):
            bolinha.y = barra_horizontal.y - bolinha.height
            vely = vely * -1


        #Placar e reset da partida
        if bolinha.y <= 1:
            ponto_player += 1
            bolinha.set_position(janela.width/2 - bolinha.width/2 , janela.height/2 - bolinha.height/2)
            espaço = 0
        elif bolinha.y >= janela.height:
            ponto_IA += 1
            bolinha.set_position(janela.width/2 - bolinha.width/2 , janela.height/2 - bolinha.height/2)
            espaço = 0
        janela.draw_text(str(ponto_player), (janela.width / 4), 50, size = 70, color = (150, 200, 50), font_name = "placar", bold = False, italic = False )
        janela.draw_text(str(ponto_IA), (2 * janela.width / 3) + bolinha.width, 50, size = 70, color = (150, 200, 50), font_name = "placar", bold = False, italic = False )

        background.draw()
        bolinha.draw()
        barra_horizontal.draw()
        barra_horizontal2.draw()
    
    janela.update()