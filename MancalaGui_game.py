import pygame
import sys
from Puit import Puit
from MancalaGame import Mancala


def switch_to_finPartie():
    import MancalaGui_fin


def event_puit(id):
    print("DB puit Joueur : ", id)
    if id >= 0 and id <= 5:
        Mancala.joueurDeplacement(id)
        isGameDone()
        for p in puits:
            puitGraines = Mancala.grille[p.label]
            p.image = Mancala.dessinerPuit(puitGraines)
            if puits.index(p) == 6 or puits.index(p) == 13:
                p.image = Mancala.dessinerPanier(puitGraines)
        pygame.display.flip()
        print(Mancala.grille)
        if Mancala.turn is False:
            event_ordi()


def event_ordi():
    while Mancala.turn is False:
        afficherPlayerTurn()
        Mancala.ordiDeplacement()
        isGameDone()
    afficherPlayerTurn()
    for p in puits:
        puitGraines = Mancala.grille[p.label]
        p.image = Mancala.dessinerPuit(puitGraines)
        if puits.index(p) == 6 or puits.index(p) == 13:
            p.image = Mancala.dessinerPanier(puitGraines)
    pygame.display.flip()


def isGameDone():
    if Mancala.verifierPartieTerminer() is True:
        switch_to_finPartie()
    else:
        return


def getPlayerTurnStr():
    if Mancala.turn is True:
        return "Votre Turn"
    elif Mancala.turn is False:
        return "Turn a Ordi"
    else:
        return "Tour a personne"


def afficherPlayerTurn():
    # texte player turn
    player_turn_label = font.render(getPlayerTurnStr(), True, BLACK)
    player_turn_label_rect = player_turn_label.get_rect()
    player_turn_label_rect.center = (width // 2, 200)
    screen.blit(player_turn_label, player_turn_label_rect)


# Initialisation de Pygame
# def run_game_interface():
pygame.init()

# Couleurs
BROWN = (139, 69, 19)  # Couleur brun
WHITE = (255, 255, 255)  # Couleur blanche
BLACK = (0, 0, 0)  # Couleur noir

# Paramètres de la fenêtre
width, height = 900, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mancala Game")

# Image à afficher
board = pygame.image.load("./images/board.jpg")
board_rect = board.get_rect()
board_rect.center = (width // 2, height // 2)

# Liste des textes des boutons
button_texts = ["Ordi", "Joueur"]

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

ordi_button_info = buttons[0]
joueur_button_info = buttons[1]

ordi_button_rect, ordi_label = ordi_button_info
joueur_button_rect, joueur_label = joueur_button_info

obj_ordi_button_rect = pygame.Rect(
    ordi_button_rect.left,
    ordi_button_rect.top,
    ordi_button_rect.width,
    ordi_button_rect.height,
)
obj_joueur_button_rect = pygame.Rect(
    joueur_button_rect.left,
    joueur_button_rect.top,
    joueur_button_rect.width,
    joueur_button_rect.height,
)

# Créez des instances de la classe Puit avec les coordonnées appropriées

puits = []
puits.append(Puit("A", 256, 305, 57, 57, 4, "./images/4.jpg"))
puits.append(Puit("B", 314, 305, 57, 57, 4, "./images/4.jpg"))
puits.append(Puit("C", 372, 305, 57, 57, 4, "./images/4.jpg"))
puits.append(Puit("D", 476, 305, 57, 57, 4, "./images/4.jpg"))
puits.append(Puit("E", 534, 305, 57, 57, 4, "./images/4.jpg"))
puits.append(Puit("F", 592, 305, 57, 57, 4, "./images/4.jpg"))
puits.append(Puit("1", 654, 240, 55, 122, 0, "./images/se.jpg"))
puits.append(Puit("G", 592, 240, 57, 57, 4, "./images/4.jpg"))
puits.append(Puit("H", 534, 240, 57, 57, 4, "./images/4.jpg"))
puits.append(Puit("I", 476, 240, 57, 57, 4, "./images/4.jpg"))
puits.append(Puit("J", 372, 240, 57, 57, 4, "./images/4.jpg"))
puits.append(Puit("K", 314, 240, 57, 57, 4, "./images/4.jpg"))
puits.append(Puit("L", 256, 240, 57, 57, 4, "./images/4.jpg"))
puits.append(Puit("2", 195, 240, 55, 122, 0, "./images/se.jpg"))

font = pygame.font.Font(None, 44)
font_label = pygame.font.Font(None, 36)
font_titre = pygame.font.Font(None, 66)

# Label for "Qui commence?"
qui_commence_label = font.render("Qui commence?", True, WHITE)
qui_commence_rect = qui_commence_label.get_rect()
qui_commence_rect.center = (width // 2, height - 150)

# texte titre jeu
titre = font_titre.render("Mancala", True, BLACK)
titre_rect = titre.get_rect()
titre_rect.center = (width // 2, 25)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (
                event.button == 1
            ):  # Vérifiez s'il s'agit d'un clic de souris (clic gauche)
                # Vérifiez si le clic est dans un puit
                for index, puit in enumerate(puits):
                    if puit.rect.collidepoint(event.pos):
                        # Appelez la fonction event_puit avec l'index du puit ca c'est lorsque le joueur clique
                        event_puit(index)
                        break
                if obj_ordi_button_rect.collidepoint(event.pos):
                    # "Ordi" button clicked
                    print("Ordi button clicked")
                    Mancala.turn = False
                    obj_ordi_button_rect.center = (-100, -100)
                    qui_commence_rect.center = (-100, -100)
                    event_ordi()

                if obj_joueur_button_rect.collidepoint(event.pos):
                    # "Joueur" button clicked
                    Mancala.turn = True
                    obj_joueur_button_rect.center = (-100, -100)
                    qui_commence_rect.center = (-100, -100)

    screen.fill(BROWN)  # Fond brun
    screen.blit(board, board_rect)  # Affichage de l'image "board.jpg"

    # Affichez les images "4.jpg" pour chaque puit
    for puit in puits:
        puit_rect = pygame.Rect(puit.x, puit.y, puit.width, puit.height)
        puit_image = pygame.image.load(puit.image)
        screen.blit(puit_image, puit_rect)

        # Create labels for each puit
        puitGraines = Mancala.grille[puit.label]
        labels_joueur = [
            font_label.render(f"{puitGraines}", True, WHITE) for i in range(6)
        ]
        labels_joueur_rect = pygame.Rect(
            puit.x + 15, puit.y, puit.width // 2, puit.height // 2
        )
        for label in labels_joueur:
            screen.blit(label, labels_joueur_rect)

    # Affichage des boutons
    for button, text in buttons:
        pygame.draw.rect(screen, WHITE, button)
        button_surface = font.render(text, True, BLACK)
        button_rect = button_surface.get_rect(center=button.center)
        screen.blit(button_surface, button_rect)

    # Affichez le texte "A.I" et la variable
    screen.blit(titre, titre_rect)
    screen.blit(qui_commence_label, qui_commence_rect)
    afficherPlayerTurn()

    pygame.display.flip()

pygame.quit()
sys.exit()
