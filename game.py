import pygame, pyscroll, pytmx


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
        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer=1)

    def run(self):
        #Maintenir la fenêtre ouverte
        running = True
        while(running):

            #Desisner le carte 
            self.group.draw(self.screen)
            pygame.display.flip()



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
    