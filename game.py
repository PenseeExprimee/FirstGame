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
        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer=5)

        #Les murs
        self.walls = []

        for colllide_objects in tmx_data.objects:
            if colllide_objects.name == "collision":
                #Ajouter le rectangle correspondant à l'objet dans la liste.
                self.walls.append(pygame.Rect(colllide_objects.x,colllide_objects.y, colllide_objects.width, colllide_objects.height))

        #Récupérer le point de pop du joueur
        pop_point = tmx_data.get_object_by_name("joueur_pop")
        #Crée un joueur
        self.joueur = Joueur(pop_point.x, pop_point.y)

        #Vitesse du joueur
        self.speed = 2

        #Ajouter le joueur au groupe de calque
        self.group.add(self.joueur)

        #HORS DE LA MAISON
        #Récupérer le point d'entrée de la maison
        enter_house_rect = tmx_data.get_object_by_name("enter_house")
        self.enter_house_rect = pygame.Rect(enter_house_rect.x, enter_house_rect.y, enter_house_rect.width, enter_house_rect.height)
        print("self enter house rect: ", self.enter_house_rect)

        self.exit_house_rect = pygame.Rect(0,0,0,0)


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
            #Collision avec les rectangles de collision classiques
            if(sprite.pieds_joueur.collidelist(self.walls) > -1):
                sprite.move_back()

            #Collision avec la maison (exterieur vers interieur)
            if(sprite.pieds_joueur.colliderect(self.enter_house_rect)):
                #fonction pour rentrer dans la maison
                print("switch in called")
                self.switch_in_house()
            #Interieur vs extérieur
            if(sprite.pieds_joueur.colliderect(self.exit_house_rect)):
                #fonction pour rentrer dans la maison
                self.switch_out_house()
    
    def switch_in_house(self):
        
        tmx_data = pytmx.util_pygame.load_pygame('house.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        
        #House (getting outside)
        exit_house = tmx_data.get_object_by_name("exit_house")
        self.exit_house_rect = pygame.Rect(exit_house.x, exit_house.y, exit_house.width, exit_house.height) 

        #Dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer = 5)

        #Crée un joueur 
        #Point de pop du joueur sur la carte
        joueur_position = tmx_data.get_object_by_name("house_spawn")
        self.joueur = Joueur(position_x = joueur_position.x, position_y = joueur_position.y)


        #Ajouter le joueur au groupe de calque
        self.group.add(self.joueur)

        #Gestion des collisions
        self.walls = []

        for objects in tmx_data.objects:
            if objects.name == "collision":
                #Ajouter le rectangle à la liste
                self.walls.append(pygame.Rect(objects.x,objects.y,objects.width, objects.height))

    def switch_out_house(self):
        
        tmx_data = pytmx.util_pygame.load_pygame('map.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        
        #House (getting outside)
        exit_house = tmx_data.get_object_by_name("enter_house")
        self.exit_house_rect = pygame.Rect(exit_house.x, exit_house.y, exit_house.width, exit_house.height) 

        #Dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer = 5)

        #Crée un joueur 
        #Point de pop du joueur sur la carte
        joueur_position = tmx_data.get_object_by_name("enter_house_exit")
        self.joueur = Joueur(position_x = joueur_position.x, position_y = joueur_position.y)


        #Ajouter le joueur au groupe de calque
        self.group.add(self.joueur)

        #Gestion des collisions
        self.walls = []

        for objects in tmx_data.objects:
            if objects.name == "collision":
                #Ajouter le rectangle à la liste
                self.walls.append(pygame.Rect(objects.x,objects.y,objects.width, objects.height))

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
        
                
