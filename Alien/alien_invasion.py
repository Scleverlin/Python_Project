import sys
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
def run_game():
    pygame.init()
    ai_settings = Settings() 
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    
    pygame.display.set_caption("Alien Invasion")# title for the windows
    ship=Ship(ai_settings,screen) # make an instance of ship，and pass screen 
    
    while True :
        gf.check_events(ship)
        ship.update()
        # redraw the screen color during each pass through the loop
        gf.update_screen(ai_settings,screen,ship)

run_game()