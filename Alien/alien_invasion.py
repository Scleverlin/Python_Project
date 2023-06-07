import sys
import pygame

from settings import Settings
from ship import Ship
def run_game():
    pygame.init()
    ai_settings = Settings() 
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    
    pygame.display.set_caption("Alien Invasion")# title for the windows
    ship=Ship(screen) # make an instance of ship，and pass screen 
    
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # redraw the screen color during each pass through the loop
        screen.fill(ai_settings.bg_color) # only takes one argument, a color
        ship.blitme() # 
        # redraw the screen during each pass through the loop
        pygame.display.flip()
        
run_game()