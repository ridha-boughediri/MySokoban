import pygame

# définition des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# définition de la taille de la fenêtre
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# définition de la taille d'une case de la carte
TILE_SIZE = 50

# définition de la carte
map_data = [
    [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1],

    [1, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 4, 0, 0, 1, 7, 1, 0, 0, 4, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 11, 0, 0, 0, 1, 1, 1, 1],
    [3, 3, 9, 1, 0, 0, 10, 12, 10, 0, 0, 1, 8, 3, 3],
    [1, 1, 1, 1, 0, 0, 0, 11, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 4, 0, 0, 1, 6, 1, 0, 0, 4, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1]
]

# initialisation de Pygame
pygame.init()

# création de la fenêtre
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# boucle de jeu
running = True
while running:
    # traitement des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # effacement de la fenêtre
    window.fill(WHITE)

    # affichage de la carte
    for row in range(len(map_data)):
        for column in range(len(map_data[row])):
            tile = map_data[row][column]
            tile_color = WHITE
