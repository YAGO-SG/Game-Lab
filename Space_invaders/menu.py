from config import window, mouse, click, keyboard
import config
from Sprites import Sprite_menu
import json
import os

#inicializando as variáveis
GameLogo = PlayMenu = DiffMenu = RankMenu = ExitMenu = EasyBttn = MediumBttn = HardBttn = None

def init_sprites_menu():
    global GameLogo, PlayMenu, DiffMenu, RankMenu, ExitMenu, EasyBttn, MediumBttn, HardBttn
    GameLogo, PlayMenu, DiffMenu, RankMenu, ExitMenu, EasyBttn, MediumBttn, HardBttn = Sprite_menu()

def posições_Sprites():
    GameLogo.set_position((window.width - GameLogo.width)/2, GameLogo.height/4)
    PlayMenu.set_position((window.width - PlayMenu.width)/2, (window.height- PlayMenu.height)/2 - 75)
    DiffMenu.set_position((window.width - DiffMenu.width)/2, (window.height - DiffMenu.height)/2)
    RankMenu.set_position((window.width - RankMenu.width)/2, (window.height - RankMenu.height)/2 + 75)
    ExitMenu.set_position((window.width - ExitMenu.width)/2, (window.height - ExitMenu.height)/2 + 150)

def game_loop_menu():

    while config.GAME_STATE == 0:
        window.set_background_color((0, 0, 0))

        if click(PlayMenu):
            config.GAME_STATE = 1
        elif click(DiffMenu):
            config.GAME_STATE = 2
        elif click(RankMenu):
            config.GAME_STATE = 3
        elif click(ExitMenu):
            window.close()

        GameLogo.draw()
        PlayMenu.draw()
        DiffMenu.draw()
        RankMenu.draw()
        ExitMenu.draw()
        window.update()

def game_dif():
    GameLogo, PlayMenu, DiffMenu, RankMenu, ExitMenu, EasyBttn, MediumBttn, HardBttn = Sprite_menu()
    while True: 

        bttn_spaces = 30
        start_y = window.height / 2 - EasyBttn.height - bttn_spaces
        GameLogo.set_position((window.width - GameLogo.width)/2, 50)
        EasyBttn.set_position((window.width - EasyBttn.width) / 2, GameLogo.y + GameLogo.height + bttn_spaces)
        MediumBttn.set_position((window.width - MediumBttn.width) / 2, EasyBttn.y + EasyBttn.height + bttn_spaces)
        HardBttn.set_position((window.width - HardBttn.width)/2, start_y + 2 * (EasyBttn.height + bttn_spaces))
        GameLogo.draw()
        EasyBttn.draw()
        MediumBttn.draw()
        HardBttn.draw()
        window.update()

def game_rank():
    while True:
        window.set_background_color((0, 0, 0))
        if keyboard.key_pressed("esc"):
            config.GAME_STATE = 0
            break
        ranking_file = "ranking.json"
        if os.path.exists(ranking_file):
            with open(ranking_file, "r", encoding="utf-8") as f:
                ranking = json.load(f)
            # Ordena do maior para o menor
            ranking = sorted(ranking, key=lambda x: x["pontuacao"], reverse=True)[:5]
        else:
            ranking = []

        def draw_ranking():
            window.draw_text("RANKING", window.width // 2 - 80, 50, size=40, color=(255,255,0), font_name="Arial", bold=True)
            for idx, entry in enumerate(ranking):
                text = f"{idx+1}. {entry['nome']} - {entry['pontuacao']}"
                window.draw_text(text, window.width // 2 - 120, 120 + idx * 40, size=30, color=(255,255,255), font_name="Arial")
        
        draw_ranking()  # <-- Adicione esta linha!
        window.update()

def modes_draw():
    GameLogo.draw()
    EasyBttn.draw()
    MediumBttn.draw()
    HardBttn.draw()