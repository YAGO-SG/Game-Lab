from config import window, mouse, keyboard, click
import config
from pplay.sprite import Sprite
from Sprites import Sprite_game
from inimigos import matriz_inimigos, inimigos, tiros_inimigos
import json
import os

nave = Game_Over = escudo = escudo_helf = None
nivel = 1
def init_game_loop():
    global nave, Game_Over, disparos, tempo_disparos, recarga_disparos, heart, escudo, escudo_helf
    global nave_imortal, tempo_imortal
    global nivel, pontuação
    nivel = 1
    pontuação = 0
    nave, Game_Over, heart, escudo, escudo_helf= Sprite_game()
    nave.set_position((window.width - nave.width)/2, window.height - 70)
    Game_Over.set_position((window.width - Game_Over.width)/2, (window.height - Game_Over.height)/2)
    escudo.set_position((window.width - escudo.width)/2, (window.height - escudo.height)/2 + 200)
    escudo_helf.set_position((window.width - escudo_helf.width)/2, (window.height - escudo_helf.height)/2 + 200)
    disparos = []
    recarga_disparos = 0
    tempo_disparos = 0
    nave_imortal = False
    tempo_imortal = 0

def opções_nave():
    global disparos, tempo_disparos

    tempo_disparos += window.delta_time()
    vel_nave = 650

    if keyboard.key_pressed("RIGHT") and nave.x <= window.width - nave.width:
        nave.x += vel_nave * window.delta_time()
    elif keyboard.key_pressed("LEFT") and nave.x >= 0:
        nave.x -= vel_nave * window.delta_time()

    veldisparos = -800

    # Corrigido: só dispara se tempo_disparos >= 0.259, e zera após disparar
    if keyboard.key_pressed("SPACE") and tempo_disparos >= 0.259:
        disparo = Sprite('./Space_invaders/Sprites/game/projetil.png')
        disparo.set_position(nave.x + nave.width/2 - disparo.width/2, nave.y - disparo.height)  
        disparos.append(disparo)
        tempo_disparos = 0  # Zera o cronômetro após disparar

    for i in range(len(disparos)-1, -1, -1):
        disparos[i].draw()
        disparos[i].y += veldisparos * window.delta_time()
        if disparos[i].y < 0:
            disparos.pop(i)

    nave.draw()

def colisão_inimigos(matriz_inimigos):
    global disparos, pontuação, escudo, escudo_helf

    if not any(matriz_inimigos):
        return

    min_x = float('inf')
    max_x = float('-inf')
    max_y = float('-inf')
    for linha in matriz_inimigos:
        for inimigo in linha:
            if inimigo.x < min_x:
                min_x = inimigo.x
            if inimigo.x + inimigo.width > max_x:
                max_x = inimigo.x + inimigo.width
            if inimigo.y + inimigo.height > max_y:
                max_y = inimigo.y + inimigo.height

    for i in range(len(disparos)-1, -1, -1):
        disparo = disparos[i]
        # Colisão com escudo
        if escudo and disparo.collided(escudo):
            disparos.pop(i)
            continue
        # Colisão com escudo_helf
        if escudo_helf and disparo.collided(escudo_helf):
            disparos.pop(i)
            continue
        # Só verifica colisão se o disparo está dentro da área lateral e inferior da matriz
        if (disparo.x + disparo.width < min_x or disparo.x > max_x or
            disparo.y > max_y):
            continue

        colisao = False
        for linha in matriz_inimigos:
            for j in range(len(linha)-1, -1, -1):
                inimigo = linha[j]
                if disparo.collided(inimigo):
                    linha.pop(j)
                    disparos.pop(i)
                    pontuação += 1
                    colisao = True
                    break
            if colisao:
                break

def salvar_score(nome, pontuacao, arquivo="ranking.json"):
    # Carrega o ranking existente ou cria um novo
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            ranking = json.load(f)
    else:
        ranking = []

    # Adiciona o novo score
    ranking.append({"nome": nome, "pontuacao": pontuacao})

    # Salva de volta
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(ranking, f, ensure_ascii=False, indent=4)

def game_loop():
    global nave_imortal, tempo_imortal
    global nave_imortal, tempo_imortal, nivel
    init_game_loop()
    monstros = matriz_inimigos(4, 8)
    tempo_ultimo_tiro_inimigo = 0

    while True:
        window.set_background_color((0, 0, 0))
        if keyboard.key_pressed("ESC"):
            config.GAME_STATE = 0
            break

        # Verifica se algum inimigo chegou na altura da nave
        game_over = False
        for linha in monstros:
            for inimigo in linha:
                if inimigo.y + inimigo.height >= nave.y:
                    game_over = True
                    break
            if game_over:
                break

        if game_over:
            Game_Over.draw()
            window.update()
            nome = input("digite seu nome: ")
            salvar_score(nome, pontuação)
            config.GAME_STATE = 0
            return

        tempo_ultimo_tiro_inimigo, atingiu_nave = tiros_inimigos(
    monstros, tempo_ultimo_tiro_inimigo, nave, nave_imortal, escudo, escudo_helf
)
        if atingiu_nave and not nave_imortal:
            nave.x = (window.width - nave.width) / 2
            nave.y = window.height - 70
            nave_imortal = True
            tempo_imortal = 0

        if nave_imortal:
            tempo_imortal += window.delta_time()
            # Pisca: desenha a nave só em certos frames
            if int(tempo_imortal * 10) % 2 == 0:
                nave.draw()
            # Após 2 segundos, volta ao normal
            if tempo_imortal >= 2:
                nave_imortal = False
        else:
            opções_nave()
        inimigos(monstros)
        colisão_inimigos(monstros)
        
        if all(len(linha) == 0 for linha in monstros):
            nivel += 1
            linhas = min(4 + nivel, 10)
            colunas = min(8 + nivel, 16)
            monstros = matriz_inimigos(linhas, colunas)
            from inimigos import velx_monstros
            velx_monstros += 50 * nivel

            # Reposiciona os escudos para o centro (voltam a aparecer)
            escudo.set_position((window.width - escudo.width)/2, (window.height - escudo.height)/2 + 200)
            escudo_helf.set_position((window.width - escudo_helf.width)/2, (window.height - escudo_helf.height)/2 + 200)

        escudo_helf.draw()
        escudo.draw()
        window.draw_text(str(pontuação), 50, window.height - 50, size=20, color=(255,255,255), font_name="Arial" , bold=False, italic=False)
        window.update()