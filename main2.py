import pygame

# Définition des constantes
RED = (100, 3, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Définition de la taille de la fenêtre
WIDTH = 1000
HEIGHT = 1000

# Définition de la taille d'une case de la carte
TILE_SIZE = 40

# Définition de la carte du jeu sous forme de tableau
game_map = [
    [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 1],
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

# # Initialisation de Pygame
# pygame.init()

# # Création de la fenêtre
# screen = pygame.display.set_mode((WIDTH, HEIGHT))

# # Boucle principale du jeu
# running = True
# while running:

#     # Gestion des événements
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Dessiner la carte
#     for y, row in enumerate(game_map):
#         for x, tile in enumerate(row):
#             rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE,
#                                TILE_SIZE, TILE_SIZE)
#             if tile == 1:
#                 pygame.draw.rect(screen, BLUE, rect)
#             else:
#                 pygame.draw.rect(screen, GREEN, rect)

#     # Mettre à jour l'affichage
#     pygame.display.flip()

# # Quitter Pygame
# pygame.quit()


# Chargement des images
wall_image = pygame.image.load("fond.png")
empty_image = pygame.image.load("mer.png")
player_image = pygame.image.load("joueur.png")
mur_image = pygame.image.load("mur.png")
fond_image = pygame.image.load("fond.png")
champignon_image = pygame.image.load("champignon.png")

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Boucle principale du jeu
running = True
while running:

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dessiner la carte
    for y, row in enumerate(game_map):
        for x, tile in enumerate(row):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE,
                               TILE_SIZE, TILE_SIZE)
            if tile == 1:
                screen.blit(mur_image, rect)

            elif tile == 0:
                screen.blit(fond_image, rect)
            elif tile == 2:
                screen.blit(player_image, rect)

            elif tile == 4:
                screen.blit(champignon_image, rect)

            else:
                screen.blit(empty_image, rect)

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
