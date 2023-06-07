import pygame

class Ship:
    
     def __init__ (self,screen):
         self.screen=screen
         
         # load the ship image and get its rect
         self.image=pygame.image.load('./ship.bmp') # load the image
         self.rect = self.image.get_rect()  # get_rect() method to access the surface's rect attribute
         self.screen_rect = screen.get_rect() 
         # start each new ship at the bottom center of the screen

         
     def blitme(self): # bit block transfer (blit) draws the image to the screen
        # draw the ship at its current location  
        self.rect.centerx = self.screen_rect.centerx # center the ship, x axis
        self.rect.bottom = self.screen_rect.bottom   # bottom the ship  
        
        self.screen.blit(self.image,self.rect)