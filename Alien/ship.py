import pygame

class Ship:
    
     def __init__ (self,ai_settings,screen):
         self.screen=screen
         self.ai_settings = ai_settings 
         # load the ship image and get its rect
         self.image=pygame.image.load('./ship.bmp') # load the image
         self.rect = self.image.get_rect()  # get_rect() method to access the surface's rect attribute
         self.screen_rect = screen.get_rect() 
         self.center = float(self.rect.centerx)
         # start each new ship at the bottom center of the screen
         self.rect.centerx = self.screen_rect.centerx # center the ship, x axis
         self.rect.bottom = self.screen_rect.bottom   # bottom the ship  
         self.moving_right = False
         self.moving_left  = False 
         
         self.ship_speed_factor_right = 1.1
         self.ship_speed_factor_left = 0.1 # in my keaboard, the left key speed is faster than that of right key
     def update(self):
         if self.moving_right and self.rect.right < self.screen_rect.right :
             self.rect.centerx += self.ship_speed_factor_right
         if self.moving_left and self.rect.left > 0:  
             self.rect.centerx -= self.ship_speed_factor_left
     def blitme(self): # bit block transfer (blit) draws the image to the screen
        # draw the ship at its current location  
        self.screen.blit(self.image,self.rect)