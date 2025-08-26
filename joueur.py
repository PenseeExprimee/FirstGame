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

        #Différentes directions du personnage
        self.images = {
            "UP": self.get_image(0,96),
            "DOWN": self.get_image(0,0),
            "LEFT": self.get_image(0,32),
            "RIGHT": self.get_image(0,64),
        }

        #Enlever le background noir
        self.image.set_colorkey([0,0,0])

        #Position du joueur (représenté par un rectangle)
        self.rect = self.image.get_rect()

        #Pieds du joueur
        self.pieds_joueur = pygame.Rect(0,0, self.rect.width*0.5, 12)

        #Sauvegarde de la position du joueur
        self.old_position = self.rect.copy()
    
    def get_image(self,x,y):
        #Récupérer un bout de la sprite sheet
        personage_image = pygame.Surface([32,32])
        personage_image.blit(self.sprite_sheet,(0,0), (x,y, 32, 32))

        return personage_image
    
    def save_old_position(self):
        self.old_position = self.position.copy()

    def move_back(self):

        #Update la position de joueur, retour à la position précédente
        self.position = self.old_position
        #Retour du rectangle du joueur à la position précéddente
        self.rect.topleft = self.position
        #Re aligner les pieds du joueur avec le bas du rectangle
        self.pieds_joueur.midbottom = self.rect.midbottom
   
    def update(self):
        #Bouger le rectangle du joueur
        self.rect.topleft = self.position

        #Aligner le bas du rectangle représentant le joueur avec le rectangle représentant les pieds du joueur
        self.pieds_joueur.midbottom = self.rect.midbottom

    def tourner_perso(self, direction):
        self.image = self.images[direction]

        #Enlever le background noir
        self.image.set_colorkey([0,0,0])