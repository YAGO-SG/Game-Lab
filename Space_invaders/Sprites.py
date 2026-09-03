from pplay.sprite import Sprite


def Sprite_menu():
    GameLogo = Sprite("./Space_invaders/Sprites/Menu/si.png")
    PlayMenu = Sprite("./Space_invaders/Sprites/Menu/Play_menu.png")
    DiffMenu = Sprite("./Space_invaders/Sprites/Menu/Diff_menu.png")
    RankMenu = Sprite("./Space_invaders/Sprites/Menu/Rank_menu.png")
    ExitMenu = Sprite("./Space_invaders/Sprites/Menu/Exit_menu.png")
    EasyBttn = Sprite("./Space_invaders/Sprites/Menu/Easy_Bttn.png")
    MediumBttn = Sprite("./Space_invaders/Sprites/Menu/Medium_Bttn.png")
    HardBttn = Sprite("./Space_invaders/Sprites/Menu/Hard_Bttn.png")

    return GameLogo, PlayMenu, DiffMenu, RankMenu, ExitMenu, EasyBttn, MediumBttn, HardBttn

def Sprite_game():
    nave = Sprite('./Space_invaders/Sprites/game/nave.png')
    Game_over = Sprite('./Space_invaders/Sprites/game/Game_Over.png')
    hearth = Sprite('./Space_invaders/Sprites/game/full_heart.png')
    escudo = Sprite('./Space_invaders/Sprites/game/escudo.png')
    escudo_helf = Sprite('./Space_invaders/Sprites/game/escudo_helf.png')
    return nave, Game_over, hearth, escudo, escudo_helf
