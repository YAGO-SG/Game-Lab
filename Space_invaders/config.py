import pygame
from pplay.window import *
from pplay.sprite import *
from pplay.animation import *
from pplay.collision import *
from pplay.gameimage import *
pygame.init()

window = Window(1200,800)
title = "Space-Invaders"
window.set_title("Space Invaders")
keyboard = window.get_keyboard()
mouse = window.get_mouse()

GAME_STATE = 0

def click(Sprite):
    if mouse.is_button_pressed(1) and mouse.is_over_object(Sprite):
        return True
    
    return False
