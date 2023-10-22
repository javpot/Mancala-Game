import pygame
import sys
from Puit import Puit
from MancalaGame import Mancala


def switch_to_finPartie():
    pygame.quit()  # Fermez la fenêtre actuelle
    import MancalaGui_fin


def event_puit(id):
    print("DB puit Joueur : ", id)
    if id >= 0 and id <= 5:
        Mancala.joueurDeplacement(id)
        for p in puits:
            puitGraines = Mancala.grille[p.label]
            p.image = Mancala.dessinerPuit(puitGraines)
            if puits.index(p) == 6 or puits.index(p) == 13:
                p.image = Mancala.dessinerPanier(puitGraines)
        pygame.display.flip()
        print(Mancala.grille)
        if Mancala.turn is False:
            # pygame.time.delay(2000)
            event_ordi()


def event_ordi():
    while Mancala.turn is False:
        Mancala.ordiDeplacement()
    for p in puits:
        puitGraines = Mancala.grille[p.label]
        p.image = Mancala.dessinerPuit(puitGraines)
        if puits.index(p) == 6 or puits.index(p) == 13:
            p.image = Mancala.dessinerPanier(puitGraines)
    pygame.display.flip()


def send_text_to_game(text):
    Mancala.textDifficulty = text


# Initialisation de Pygame
# def run_game_interface():
pygame.init()

# Couleurs
BROWN = (139, 69, 19)  # Couleur brun
WHITE = (255, 255, 255)  # Couleur blanche

# Paramètres de la fenêtre
width, height = 900, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mancala Game")

# Image à afficher
board = pygame.image.load("./images/board.jpg")
board_rect = board.get_rect()
board_rect.center = (width // 2, height // 2)

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

font = pygame.font.Font(None, 48)

# Texte "A.I"
text_ai = font.render("Ordi", True, WHITE)
text_ai_rect = text_ai.get_rect()
text_ai_rect.topleft = (100, 10)

# Variable AI
variable_value_AI = 0
variable_textAI = font.render(str(variable_value_AI), True, WHITE)
variable_text_rectAI = variable_textAI.get_rect()
variable_text_rectAI.topleft = (100, text_ai_rect.bottom + 10)

# Texte "Joueur"
text_joueur = font.render("Joueur", True, WHITE)
text_joueur_rect = text_joueur.get_rect()
text_joueur_rect.topright = (width - 100, 10)  # Aligné à droite

# Variable Joueur
variable_value_Joueur = 0
variable_textJoueur = font.render(str(variable_value_Joueur), True, WHITE)
variable_text_rectJoueur = variable_textJoueur.get_rect()
variable_text_rectJoueur.topright = (
    width - 100,
    text_joueur_rect.bottom + 10,
)  # Aligné à droite
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

    screen.fill(BROWN)  # Fond brun
    screen.blit(board, board_rect)  # Affichage de l'image "board.jpg"

    # Affichez les images "4.jpg" pour chaque puit
    for puit in puits:
        puit_rect = pygame.Rect(puit.x, puit.y, puit.width, puit.height)
        puit_image = pygame.image.load(puit.image)
        screen.blit(puit_image, puit_rect)

    # Affichez le texte "A.I" et la variable
    screen.blit(text_ai, text_ai_rect)
    screen.blit(variable_textAI, variable_text_rectAI)
    screen.blit(text_joueur, text_joueur_rect)
    screen.blit(variable_textJoueur, variable_text_rectJoueur)

    pygame.display.flip()

pygame.quit()
sys.exit()
