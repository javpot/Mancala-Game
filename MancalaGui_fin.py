import pygame
import sys
from MancalaGame import Mancala


def switch_to_options():
    pygame.quit()  # Fermez la fenêtre actuelle
    import MancalaGui_option


# Initialisation de Pygame
pygame.init()

# Couleurs
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Paramètres de la fenêtre
width, height = 900, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ecran fin de partie")

# Polices de texte
font = pygame.font.Font(None, 24)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic gauche de la souris
                switch_to_options()  # Appel de la fonction pour changer de fenêtre

    screen.fill(BLACK)  # Fond Noir

    # Affichage des boutons

    pygame.display.flip()

pygame.quit()
sys.exit()
