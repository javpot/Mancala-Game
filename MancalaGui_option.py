import pygame
import sys
from MancalaGame import Mancala


def switch_to_game():
    pygame.quit()  # Fermez la fenêtre actuelle
    from MancalaGui_game import (
        run_game_interface,
    )  # Importez la fonction run_game_interface

    run_game_interface()  # Exécutez la fonction pour afficher la fenêtre de mancalaGui_game


# Function to wrap text within a given width
def wrap_text(text, font, max_width):
    words = text.split()
    lines = []
    current_line = []
    current_width = 0

    for word in words:
        word_surface = font.render(word, True, (255, 255, 255))
        word_width, _ = word_surface.get_size()

        if current_width + word_width <= max_width:
            current_line.append(word)
            current_width += word_width + font.size(" ")[0]
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_width = word_width + font.size(" ")[0]

    lines.append(" ".join(current_line))
    return lines


# Initialisation de Pygame
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
font_instructions = pygame.font.Font(None, 24)

# texte instructions
game_instructions = "L'objectif global de Mancala est de déplacer plus de pierres dans votre magasin que votre adversaire ne peut le faire. Les joueurs vont et viennent en déplaçant leurs pierres d'une fosse à l'autre en les déplaçant dans le sens inverse des aiguilles d'une montre. Le nombre de tuiles que les joueurs peuvent déplacer leurs pierres est basé sur le nombre de pierres dans la pile qu'ils sélectionnent. Le jeu se termine lorsqu'un côté du plateau n'a plus de pierres. À ce stade, celui qui a le plus de pierres dans son magasin est déclaré vainqueur."
wrapped_text = wrap_text(game_instructions, font_instructions, width - 20)

# Position the text on the screen
text_rect = pygame.Rect(10, 10, width - 20, height - 20)
text_rect.center = (width // 2, height // 2)

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
                        Mancala.textDifficulty = text
                        switch_to_game()  # Appel de la fonction pour changer de fenêtre
                        running = False  # Quittez la boucle de mancalaGui_option

    screen.fill(BLACK)  # Fond Noir

    for i, line in enumerate(wrapped_text):
        line_surface = font_instructions.render(line, True, (255, 255, 255))
        screen.blit(
            line_surface, (text_rect.left, text_rect.top + i * font.get_linesize())
        )

    # Affichage des boutons
    for button, text in buttons:
        pygame.draw.rect(screen, RED, button)
        button_surface = font.render(text, True, BLACK)
        button_rect = button_surface.get_rect(center=button.center)
        screen.blit(button_surface, button_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
