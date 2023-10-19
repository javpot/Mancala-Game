import pygame
import sys
from Puit import Puit

# Initialisation de Pygame
pygame.init()

# Couleurs
BROWN = (139, 69, 19)  # Couleur brun

# Paramètres de la fenêtre
width, height = 900, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mancala Game")

# Image à afficher
board = pygame.image.load("board.jpg")
board_rect = board.get_rect()
board_rect.center = (width // 2, height // 2)

# Créez des instances de la classe Puit avec les coordonnées appropriées
puits = []
puits.append(Puit("A", 256, 305, 100, 100, 4, "4.jpg"))
puits.append(Puit("B", 314, 305, 100, 100, 4, "4.jpg"))
puits.append(Puit("C", 372, 305, 100, 100, 4, "4.jpg"))
puits.append(Puit("D", 476, 305, 100, 100, 4, "4.jpg"))
puits.append(Puit("E", 534, 305, 100, 100, 4, "4.jpg"))
puits.append(Puit("F", 592, 305, 100, 100, 4, "4.jpg"))
puits.append(Puit("1", 0, 0, 100, 300, 0, "se.jpg"))
puits.append(Puit("G", 256, 240, 100, 100, 4, "4.jpg"))
puits.append(Puit("H", 314, 240, 100, 100, 4, "4.jpg"))
puits.append(Puit("I", 372, 240, 100, 100, 4, "4.jpg"))
puits.append(Puit("J", 476, 240, 100, 100, 4, "4.jpg"))
puits.append(Puit("K", 534, 240, 100, 100, 4, "4.jpg"))
puits.append(Puit("L", 592, 240, 100, 100, 4, "4.jpg"))
puits.append(Puit("2", 700, 240, 100, 300, 0, "se.jpg"))

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BROWN)  # Fond brun
    screen.blit(board, board_rect)  # Affichage de l'image "board.jpg"

    # Affichez les images "4.jpg" pour chaque puit
    for puit in puits:
        puit_rect = pygame.Rect(puit.x, puit.y, puit.width, puit.height)
        puit_image = pygame.image.load(puit.image)
        screen.blit(puit_image, puit_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
