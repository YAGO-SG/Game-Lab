from pplay.sprite import Sprite

#Sprites da janela Menu
def Sprites_Menu(): 
    background = Sprite('./horde breaker/Sprites/Menu/background.png')
    play = Sprite('./horde breaker/Sprites/Menu/play_2.png')
    score = Sprite('./horde breaker/Sprites/Menu/scored_2.png')
    mute = Sprite('./horde breaker/Sprites/Menu/mute_2.png')
    close = Sprite('./horde breaker/Sprites/Menu/quit_2.png')
    return background, play, score, mute, close

def Sprite_Score():
    score_background = Sprite("./horde breaker/Sprites/Menu/score_background.png")
    return score_background

#Spites da janela game
def Sprites_game():
    full_heart = [Sprite('./horde breaker/Sprites/Game/HUD/full_heart.png') for _ in range(3)]
    heartless = [Sprite('./horde breaker/Sprites/Game/HUD/heartless.png') for _ in range(3)]
    mapa = Sprite('./horde breaker/Sprites/Game/mapa/mapa.png')
    game_over = Sprite('./horde breaker/Sprites/Game/HUD/game_over.png')
    yes_button = Sprite('./horde breaker/Sprites/Game/HUD/yes_button.png')
    no_button = Sprite('./horde breaker/Sprites/Game/HUD/no_button.png')
    furia = Sprite('./horde breaker/Sprites/Game/HUD/FURIA.png')
    round_2 = Sprite('./horde breaker/Sprites/Game/HUD/round_2.png')
    round_3 = Sprite('./horde breaker/Sprites/Game/HUD/round_3.png')

    return full_heart, heartless, mapa, game_over, yes_button, no_button, furia, round_2, round_3

def Sprites_jogador():
    player = Sprite('./horde breaker/Sprites/Game/player.png')
    shooting = Sprite('./horde breaker/Sprites/Game/small shooting.png')
    
    return player, shooting

def Sprites_enemy():
    enemy = Sprite('./horde breaker/Sprites/Game/inimigos/inimigo_default.png')
    explotion_monster = Sprite('./horde breaker/Sprites/Game/inimigos/explosive_monster.png')
    explotion = Sprite('./horde breaker/Sprites/Game/inimigos/explosion.png')

    return enemy, explotion_monster, explotion