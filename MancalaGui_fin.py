import pygame
import sys
from MancalaGame import Mancala


def switch_to_options():
    import MancalaGui_option


# Initialisation de Pygame
pygame.init()

# Couleurs
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paramètres de la fenêtre
width, height = 900, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ecran fin de partie")

# Polices de texte
font_resultat = pygame.font.Font(None, 36)
font = pygame.font.Font(None, 28)

# texte Gagnant
titre = font_resultat.render(Mancala.verifierGagnant(), True, WHITE)
titre_rect = titre.get_rect()
titre_rect.center = (width // 2, 25)

# Label for "Voulez-vous jouer à nouveau?"
rejouer_label = font.render("Voulez-vous jouer à nouveau?", True, WHITE)
rejouer_label_rect = rejouer_label.get_rect()
rejouer_label_rect.center = (width // 2, height - 150)

# Liste des textes des boutons
button_texts = ["Oui", "Non"]

# Position de départ pour les boutons
button_x = width // 2 - 112.5
button_y = height - 100  # Centre les boutons verticalement

# Création des boutons interactifs
buttons = []
for text in button_texts:
    button = pygame.Rect(0, 0, 200, 50)  # Rectangle pour le bouton
    button.center = (button_x, button_y)
    buttons.append((button, text))
    button_x += 225  # Espacement vertical
oui_button_info = buttons[0]
non_button_info = buttons[1]

oui_button_rect, ordi_label = oui_button_info
non_button_rect, joueur_label = non_button_info

obj_oui_button_rect = pygame.Rect(
    oui_button_rect.left,
    oui_button_rect.top,
    oui_button_rect.width,
    oui_button_rect.height,
)
obj_non_button_rect = pygame.Rect(
    non_button_rect.left,
    non_button_rect.top,
    non_button_rect.width,
    non_button_rect.height,
)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic gauche de la souris
                if non_button_rect.collidepoint(event.pos):
                    exit()  # quitter
                elif oui_button_rect.collidepoint(event.pos):
                    Mancala.nouvelleGrille()
                    switch_to_options()  # Appel de la fonction pour changer de fenêtre
                    running = False

    screen.fill(BLACK)  # Fond Noir

    screen.blit(titre, titre_rect)
    screen.blit(rejouer_label, rejouer_label_rect)

    # Affichage des boutons
    for button, text in buttons:
        pygame.draw.rect(screen, WHITE, button)
        button_surface = font.render(text, True, BLACK)
        button_rect = button_surface.get_rect(center=button.center)
        screen.blit(button_surface, button_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
