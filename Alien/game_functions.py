import sys 
import pygame
from bullet import Bullet
def check_events(ai_settings,screen,ship,bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get(): # event loop
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events (event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        
def update_screen(ai_settings,screen,ship,bullets):
    screen.fill(ai_settings.bg_color) # only takes one argument, a color
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme() # draw the ship
    # redraw the screen during each pass through the loop
    pygame.display.flip()

def check_keydown_events (event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT: 
        ship.moving_right = True
    elif event.key == pygame.K_LEFT: 
        ship.moving_left = True 
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
        
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT: 
        ship.moving_left = False
             