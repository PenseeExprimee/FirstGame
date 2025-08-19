import pygame

class Joueur(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y):
        super().__init__()
        #Load la sprite sheet
        self.sprite_sheet = pygame.image.load("Player.png")
        
        #Attribut position
        self.position = [position_x, position_y]

        #Image du perso
        self.image = self.get_image(0,0)

        #Enlever le background noir
        self.image.set_colorkey([0,0,0])

        #Position du joueur (représenté par un rectangle)
        self.rect = self.image.get_rect()
    
    def get_image(self,x,y):
        #Récupérer un bout de la sprite sheet
        personage_image = pygame.Surface([32,32])
        personage_image.blit(self.sprite_sheet,(0,0), (x,y, 32, 32))

        return personage_image
    
   
    def update(self):
        self.rect.topleft = self.position
