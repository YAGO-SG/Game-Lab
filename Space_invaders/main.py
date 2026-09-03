import config 
from pplay.sprite import Sprite
from menu import game_dif, game_loop_menu, init_sprites_menu, posições_Sprites, game_rank
from game import game_loop

init_sprites_menu()
posições_Sprites()
 
while True: 
    config.window.set_background_color((0, 0, 0))

    if config.GAME_STATE == 0:
        game_loop_menu()
    elif config.GAME_STATE == 1:
        game_loop()
    elif config.GAME_STATE == 2:
        game_dif()
    elif config.GAME_STATE == 3:
        game_rank()
