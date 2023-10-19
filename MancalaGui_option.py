import pygame
import sys

# Initialisation de Pygame
def run_option_interface():
    pygame.init()

    # Couleurs
    YELLOW = (255, 255, 0)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)

    # Paramètres de la fenêtre
    width, height = 900, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Interface de difficulté")

    # Polices de texte
    font = pygame.font.Font(None, 36)

    # Liste des textes des boutons
    button_texts = ["Facile", "Moyen", "Difficile"]

    # Position de départ pour les boutons
    button_x = width // 2
    button_y = (height - (len(button_texts) * 70)) // 2  # Centre les boutons verticalement

    # Création des boutons interactifs
    buttons = []
    for text in button_texts:
        button = pygame.Rect(0, 0, 200, 50)  # Rectangle pour le bouton
        button.center = (button_x, button_y)
        buttons.append((button, text))
        button_y += 70  # Espacement vertical

    # Boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic gauche de la souris
                    for button, text in buttons:
                        if button.collidepoint(event.pos):
                            print(f"Vous avez cliqué sur {text}.")

        screen.fill(BLACK)  # Fond jaune

        # Affichage des boutons
        for button, text in buttons:
            pygame.draw.rect(screen, RED, button)
            button_surface = font.render(text, True, BLACK)
            button_rect = button_surface.get_rect(center=button.center)
            screen.blit(button_surface, button_rect)

        pygame.display.flip()

    pygame.quit()
    sys.exit()
