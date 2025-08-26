import pygame, pyscroll, pytmx
from joueur import Joueur


class Game:
    def __init__(self):
        #Gestion de la fenêtre du jeu
        #Initialiser pygame
        pygame.init()

        #Créer la fenêtre
        self.screen = pygame.display.set_mode(size=(800, 600), flags=0, depth=0, display=0, vsync=0)
        pygame.display.set_caption("Pensée's first game")

        #Charger la carte
        tmx_data =  pytmx.util_pygame.load_pygame("map.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data) 

        #Dessiner la carte (dessiner sur mon screen les données de la carte)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data,self.screen.get_size())

        #Display la carte
        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer=3)

        #Les murs
        self.walls = []

        for colllide_objects in tmx_data.objects:
            if colllide_objects.name == "collision":
                #Ajouter le rectangle correspondant à l'objet dans la liste.
                self.walls.append(pygame.Rect(colllide_objects.x,colllide_objects.y, colllide_objects.width, colllide_objects.height))
        print("This is the collide list: ", self.walls)

        #Récupérer le point de pop du joueur
        pop_point = tmx_data.get_object_by_name("joueur_pop")
        #Crée un joueur
        self.joueur = Joueur(pop_point.x, pop_point.y)

        #Vitesse du joueur
        self.speed = 2

        #Ajouter le joueur au groupe de calque
        self.group.add(self.joueur)

    def run(self):
        #Maintenir la fenêtre ouverte
        running = True

        #Définir une clock
        clock = pygame.time.Clock() 

        while(running):
            
            #Centrer la caméra sur le joueur (le centre du rectangle représentant le joueur)
            self.group.center(self.joueur.rect.center)
            
            #Sauvegarder la position du joueur
            self.joueur.save_old_position()

            #Bouger le perso
            self.handle_input()

            #Update le group (appelle update sur chaque élément du sprite)
            self.update()

            #Desisner le carte 
            self.group.draw(self.screen)
            pygame.display.flip()


            #FPS
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
    
    #Méthode pour update le groupe et gérer les collisions
    def update(self):
        #Update du group
        self.group.update()

        #Gestion des collisions
        for sprite in self.group.sprites():
            if(sprite.pieds_joueur.collidelist(self.walls) > -1):
                sprite.move_back()

    def handle_input(self):
        pressed_key_list = pygame.key.get_pressed()
    
        if pressed_key_list[pygame.K_UP]:
            self.move_up()
        elif pressed_key_list[pygame.K_DOWN]:
            self.move_down()
        elif pressed_key_list[pygame.K_LEFT]:
            self.move_left()
        elif pressed_key_list[pygame.K_RIGHT]:
            self.move_right()
    
    def move_left(self):
        self.joueur.tourner_perso("LEFT")
        self.joueur.position[0] -= self.speed
    def move_right(self):
        self.joueur.tourner_perso("RIGHT")
        self.joueur.position[0] += self.speed
    def move_up(self):
        self.joueur.tourner_perso("UP")
        self.joueur.position[1] -= self.speed
    def move_down(self):
        self.joueur.tourner_perso("DOWN")
        self.joueur.position[1] += self.speed
        
                
