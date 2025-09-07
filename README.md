# Installer les dépendances

Installer pip

pip install pygame

pip install pytmx (carte et décors au format tmx)

pip install pyscroll (déplacements sur la carte)

# Day 1

## *Créer  un fichier main.py*

- Importer le module pygame dans le fichier principal et l’initialiser.

- Créer la fenêtre du jeu
    - Créer la fenêtre du jeu depuis le menu pygame (en utilisant display et set mode). Préciser la taille de la fenêtre.
    - Modifier le nom de la fenêtre avec pygame (en utilisant display et set_caption)
    - Maintenir en activité la fenêtre: Créer un booléen initialisé à True et dans une boucle while regarder les évènements dans la liste pygame.event.get(). Si le type de l’event est pygame.QUIT, passer ce booléen à False puis puis fermer la fenêtre en utilisant pygame.quit().
- Créer la carte
    - Installer l’outil tiled (adapté à votre OS)
        - Nouvelle carte
        - 50 tuiles par 50 tuiles de 16pix par 16pix
        - Enregistrer dans le dossier du projet
        - Pack d’asset gratuit: RPG Nature Tilset (morceaux d’environnement naturels)
            
            🖼️Player SpriteSheet :
            
            [https://www.mediafire.com/file/v7qwnr...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbHliV0JTMTFZbkE5c1BEajVYMlMyenNPc1FRd3xBQ3Jtc0trRTJRVUtJblZVYTRmNjJkY2k1S0Jkc3dpcHlraFJ1UDlJUmZQWXRBemQyclJ5cjJvUXhWWmkwTDZweE5SLTI0TDZTSGhMZ2FPaVFVQXM5WUVMRjlFMVVDd2hTQjBpOHZOTDJJZ3U0N0JYRHdjc1dMTQ&q=https%3A%2F%2Fwww.mediafire.com%2Ffile%2Fv7qwnrk2m1c9pxv%2FPygamon.zip%2Ffile&v=ooITOxbYVTo)
            
            🖼️Nature Tileset :
            
            [https://stealthix.itch.io/rpg-nature-...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbXlkbnd5LVFoclE1MG9iVGtrZ210Mm1MWXM4QXxBQ3Jtc0trbGE1WGpIRXhta2xSaVltRHhOWjVjdGdYdnIyLXpVaWdORmtKM2JlQmhRWDBzQzVmNlhBek8wcTM0MEVDN0Z2Qy1PdmFST2tEd1E2QU81SmhWUkdXdXJPalQ1VjM5SlFxNjBibUt1NkNjQXBzUmFhTQ&q=https%3A%2F%2Fstealthix.itch.io%2Frpg-nature-tileset&v=ooITOxbYVTo)
            
            🖼️House Tileset :
            
            [https://bit.ly/3eYfpxl](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjBRZ2ZxYktsUXFKZkxXYU9za2NKdjA1RzZnQXxBQ3Jtc0trT1hDcTZka2k2Nmg2WFZyU2wxZG1qYUVrbmpGMV9kNzN1SFZNTmR3RXlROVF0WHNKY0lnalFaR01OSURvTVlPaWlKU2IyN0RiNFIzbEJWTzlJeE9hVG1RN19hUENHb3hjUklpbU0xd2NJaklZMjV3QQ&q=https%3A%2F%2Fbit.ly%2F3eYfpxl&v=ooITOxbYVTo)
            
        - Cliquer sur nouveau jeu de tuile et cliquer sur le tilset qu’on vient de la télécharger
        - ATTENTION, rendre le jeu de tuile transparent avant d’enregistrer en .tsx
    - Renommer le premier calque “background” (utiliser l’outil de remplissage pour remplir le cadre). Le remplir avec ce qui fera office de sol.
    - Nouveau calque (clique droit) que l’on appelle wall. Le remplir avec ce qui fera office de mur.
    - Nouveau calque que l’on appelle “water”. Le remplir avec ce qui fera office de cours d’eau.
    - Nouveau calque “road”. Le remplir avec ce qui fera office de routes.

- Création de la classe du jeu Game dans le fichier game.py
    - Dans la classe init: Déplacer les lignes de codes responsable de l’initialisation de la fenêtre du jeu.
    - Créer un attribut screen. Stocker la fenêtre du jeu à l’intérieur.
    - Implémenter une méthode “run”. Déplacer les lignes de code responsable de la gestion de la fenêtre du jeu dans cette méthode.
- Dans le fichier main.py, initialiser pygame, instancier la classe Game et appeler la méthode run. ATTENTION, ces lignes de code ne doivent se lancer que si on lance le jeu depuis [main.py](http://main.py) (utiliser if __**name**__ == "__**main__**":)
- Dans le fichier [Game.py](http://Game.py):
    - Importer pytmx et pyscroll
    - Charger les données de tiled dans le jeu: tmx_data = pytmx.util_pygame.load_pygame(’carte.tmx’)
    - Utiliser tmx_data pour récupérer la carte map_data = pyscroll.data.TiledMapDate(tmx_data).
    - Utiliser map_data pour récupérer tous les layers de la carte: map_layer = pyscroll.orthographic.BufferedRenderer(map_data,self.screen.get_size()).
    - Dessiner le groupe de calque (ce qu’on appelle “groupe de calque” correspond au groupe formé par les différents layers de la carte).
        - Stocker ce groupe de calque dans un attribut “group” en utilisant pyscroll.PyscrollGroup()
    - Dans la methode run:
        - recupérer le groupe et dessiner les calques en utilisant la méthode draw et  pygame.display.flip()
- Fin du jour numéro 1: TEST. La fenêtre doit s’ouvrir, afficher la carte, et se fermer lorsque l’on clique sur la croix.

# Day 2

- Implémentation du personage
    - Récupérer le player Sprite sheet: 🖼️Player SpriteSheet : [https://www.mediafire.com/file/v7qwnr...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbHliV0JTMTFZbkE5c1BEajVYMlMyenNPc1FRd3xBQ3Jtc0trRTJRVUtJblZVYTRmNjJkY2k1S0Jkc3dpcHlraFJ1UDlJUmZQWXRBemQyclJ5cjJvUXhWWmkwTDZweE5SLTI0TDZTSGhMZ2FPaVFVQXM5WUVMRjlFMVVDd2hTQjBpOHZOTDJJZ3U0N0JYRHdjc1dMTQ&q=https%3A%2F%2Fwww.mediafire.com%2Ffile%2Fv7qwnrk2m1c9pxv%2FPygamon.zip%2Ffile&v=ooITOxbYVTo)
    - créer la classe pour la gestion du joueur:
        - importer pygame
        - la classe hérite de pygame.sprite.Sprite (Un sprite est un élément du jeu qui peut interagir avec d’autres sprite du jeu et qui n’est pas statique ≠ (de la carte par exemple)
        - récupérer le sprite sheet et le stocker dans un attribut “sprite_sheet” pygame.image.load(<nom_sprite_sheet>)
        - Créer une méthode “get image”. Elle permet de récupérer un bout de la sprite sheet. Elle prend en argument les coordonnées de l’image:  pygame.Surface([largeur,hauteur]), .blit(sprite_sheet,(0,0), (x,y, largeur, hauteur)) et renvoie cette image. Les arguments “largeur” et “hauteur” correspondent aux dimensions de l’image que vous souhaitez récupérer.
        - Dans la méthode init, créer un attribut image. Stocker l’image récupéré par get_image(0,0) à l’intérieur.
        - Utiliser sur cet attribut image la fonction .set_colorkey([0,0,0]) pour enlever le background noir.
        - Utiliser la méthode .get_rect() sur l’image pour récupérer un rectangle correspondant à l’image. Stocker le résultat dans un attribut rectangle. Ce rectangle représentera la position du personage.
- Dans la classe Game:
    - Créer un joueur en utilisant la classe “Joueur”.
    - En utilisant la méthode .add sur le groupe, ajouter le joueur au groupe de calque.
- Test de mi parcours: Vérifier que tout fonctionne correctement. A ce stade, le personnage devrait apparaitre sur la carte.

- Placer le joueur au centre de la carte:
    - Modifier la méthode “init” du joueur. Elle prend maintenant en arguments des coordonnées initiales.
    - Stocker la position du joueur dans un attribut position. Une simple liste avec la coordonnée sur l’axe des abscisses et la coordonnée sur l’axe des ordonnées suffit.
    - Définir une méthode “update” pour mettre à jour la position du joueur. Il s’agit de faire correspondre la coin en haut à gauche du rectangle représentant le joueur, à la position du joueur. (appeler .topleft sur le rectangle représentant le joueur et le faire correspondre à self.position)
    - Update tout le groupe dans la boucle du jeu.
- Nouveau test pour vérifier que tout fonctionne correctement.
- Retour sur tiled:
    - Créer un calque d’objet: Un objet est élément non visible qui permet de placer un point, gérer les collisions, etc…Utiliser l’outil “insérer un point”, donner un nom à ce point (propriété “name”, <nom_du_point>). Ce point sera utilisé pour faire apparaitre le joueur au lancement du jeu.
    - Récupérer ce point dans le code à l’aide de tmx_data.get_object_by_name(”<nom_du_point>”) et utiliser les coordonnées de ce point pour placer le joueur.
    - Centrer la caméra sur le joueur (dans la boucle du jeu self.group.center(self.joueur.rect.center).
- Retour sur le code:
    - Pour voir le joueur sur la carte, il faut le replacer au dessus de tous les layers. Changer le default layer (self.group) à 3.
    - Test de fin de journée

# Day 3

- Déplacement du joueur:
    - Dans la class Game, définir une méthode “handle_input” pour récupérer les input claviers: pygame.key.get_pressed()
    - En utilisant une condition (if, elif) sur les inputs claviers[pygame.K_UP\DOWN\LEFT\RIGHT], afficher un message précisant quelle touche clavier a été pressée. Plus tard, on associera chaque entrée clavier à un déplacement du personnage.
    - Dans la boucle du jeu, appeler handle_input avant d’update les éléments
    - TEST: A ce stade, un message personalisé doit s’afficher quand vous appuyer sur les flèches directionnelles de votre clavier.
    - Implémenter les méthodes pour bouger le personnage (droite gauche haut bas)
    - définir un attribut speed correspondant à la vitesse de déplacement du personnage.
    - TEST: Si votre personnage se déplace à une vitesse beaucoup trop importante, c’est normal. Il manque un petit quelque chose.
    - Changer les FPS du jeu:
        - définir une clock au début de la boucle. clock = pygame.time.Clock()
        - A la fin de chaque boucle, clock.tick(60)
        - TEST: Le personnage devrait maintenant se déplacer sur la carte sans problème.
- Tourner le personnage quand on se déplace. Pour l’instant, peu importe la direction dans laquelle le personnage se déplace, l’image qui le réprésente reste la même. Nous allons changer cela pour rendre le jeu un peu plus réaliste.
    - définir un attribut “images” sur le joueur. Cet attribut est un dictionnaire. Pour chacune des directions (gauche, droite, haut, bas) récupérer le bout de sprite sheet correspondant. (utiliser get_image()).
    - Implémenter une méthode pour changer l’animation du joueur lors d’un déplacement dans une nouvelle direction. Cette fonction prend en argument un nom de direction et modifie self.image pour correspondre à la direction actuelle du personnage.
    - Appeler cette méthode sur le joueur dans “Game”, lorsque l’on applique une pression sur la touche correspondante.
    - Ajouter la petite ligne pour enlever le background noir quand on change l’animation.

# Day 4

- Gestion des collisions
    - Dans tiled, sélectionner le rectangle. Sélectionner les murs et leur donner le type “collision”. Faire de même pour tous les murs et les cours d’eau.
    - Dans la classe “Game”, définir un attribut “walls”.
    - Chercher dans “tmx_data.objects” les objets dont le type est collision et les ajouter à la list “walls”. On n’ajoute pas l’objet lui même mais son rectangle correspondant (donc pygame.Rect(obj.x, obj.y, obj.width, obj.height))
    - Les pieds du joueur doivent déclencher la collision lorsqu’il s’approche d’un objet. (mur ou eau) qui à le type collision. Définir un nouvel attribut “pieds_du_joueur”  correspondant aux pieds du joueur. pygame.Rect(0,0, moitié de la taille du rectangle du jour, 12 pour la hauteur)
    - Créer un nouvel attribut “old position”. Faire une copie de la position du joueur et la stocker dans cet attribut.
    - Créer une méthode “save location” qui copie la position du joueur et la stocke dans “old position”. Cette méthode est à appeler avant de bouger le joueur dans la boucle principale.
    - Dans la méthode update, définir le bas des pieds du joueur comme étant le bas du rectangle correspondant au joueur(midbottom). (On colle les deux rectangles).
    - Définir une méthode “move_back” pour replacer le joueur à sa vielle position en cas de collision. La méthode est similaire à  update sauf que l’on utilise “old_position” au lieu de “position”.
    - Définir dans la classe Game une méthode update:
        - update le groupe.
        - Détection des collisions: regarder si le sprite correspondant aux pieds du joueur entre en collision avec un des éléments de la liste des “walls”.
    - Remplacer le group.update par juste un update
    - Avant tout déplacement, mémoriser la position du joueur.

# Day 5

- Ajout de décoration sur la carte:
    - Créer un nouveau calque de tuile pour les décorations: arbre, champignons, rochers…
    - ajouter les collisions (attention, séléctioner le calque d’objet)
    - Changer le default layer pour replacer le joueur sur le bon calque.
- Ajout de structure et bâtiments:
    - 🖼️House Tileset : [https://bit.ly/3eYfpxl](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjBRZ2ZxYktsUXFKZkxXYU9za2NKdjA1RzZnQXxBQ3Jtc0trT1hDcTZka2k2Nmg2WFZyU2wxZG1qYUVrbmpGMV9kNzN1SFZNTmR3RXlROVF0WHNKY0lnalFaR01OSURvTVlPaWlKU2IyN0RiNFIzbEJWTzlJeE9hVG1RN19hUENHb3hjUklpbU0xd2NJaklZMjV3QQ&q=https%3A%2F%2Fbit.ly%2F3eYfpxl&v=ooITOxbYVTo)
    - Ajouter un nouveau jeu de tuiles au projet
    - Sélectionner une couleur de transparence (blanc ok)
    - Créer un nouveau calque de tuiles (house)
    - Ajouter un rectangle de collision sur la maison. Attention, ne sélectionner que la moitié de la maison.(sinon votre joueur ne pourra pas passer derrière la maison).
    - Changer le default layer pour replacer le joueur sur le bon calque.
- Rentrer dans la maison:
    - Créer une nouvelle carte qui correspondra à l’intérieur de la maison. Changer le nombre de tuiles 25 par 25
    - nom du tmx: house
    - Premier calque de tuile: floor
    - Deuxième calque: mur
    - Troisième calque: éléments à l’intérieur de la maison (meuble)
    - Ajouter les collisions aux objets à l’intérieur de la maison.
    - Définir un rectangle sur la porte d’entrée de la maison que l’on appelle “enter_house”. Définir un point de spawn “enter_house_exit” et le placer à l’exterieur de la maison. Ce point correspondra à la position à laquelle le joueur apparaitra en sortant de la maison.
    - De même, à l’intérieur de la maison, définir un rectangle exit_house et un point spawn_house.
    - Définir une variable enter_house dans le code pour récupérer le rectangle d’entrée de la maison
    - Créer un attribut “enter_house_rect” correspondant au rectangle “enter house”.
    - Dans update vérifier la collision des pieds du joueur avec le rectangle d’entrée de la maison (utiliser la fonction colliderect).
    - Définir une méthode switch_house pour charger la carte de la maison (réutiliser le code de chargement de la map).Il s’agit de switch entre les deux cartes (extérieur et maison) quand une collision avec l’entrée de la maison est détectée.
    - Créer une méthode “switch world” pour retourner dehors. Les deux méthodes sont quasiment identique.
    - Dans update vérifier la sortie de la maison.
- TEST FINAL ET FIN DU JEU!!! CONGRATS
