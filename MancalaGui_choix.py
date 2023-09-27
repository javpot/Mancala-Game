import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
BLEU = (0, 0, 255)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)

# Configuration de la fenêtre
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Sélection du niveau de difficulté")

# Charger l'image du fond d'écran
fond = pygame.image.load("background.jpeg")  # Assurez-vous de placer votre propre image de fond ici
fond = pygame.transform.scale(fond, (largeur, hauteur))  # Redimensionner l'image du fond

# Font pour le texte des boutons
font = pygame.font.Font(None, 36)

# Création des boutons
def creer_boutons():
    bouton_facile_surf = pygame.Surface((200, 50))
    bouton_moyen_surf = pygame.Surface((200, 50))
    bouton_difficile_surf = pygame.Surface((200, 50))

    bouton_facile_rect = bouton_facile_surf.get_rect()
    bouton_moyen_rect = bouton_moyen_surf.get_rect()
    bouton_difficile_rect = bouton_difficile_surf.get_rect()

    bouton_facile_rect.center = (largeur // 2, 200)
    bouton_moyen_rect.center = (largeur // 2, 300)
    bouton_difficile_rect.center = (largeur // 2, 400)

    return [
        {"surface": bouton_facile_surf, "rect": bouton_facile_rect, "texte": "Partie Facile"},
        {"surface": bouton_moyen_surf, "rect": bouton_moyen_rect, "texte": "Partie Moyen"},
        {"surface": bouton_difficile_surf, "rect": bouton_difficile_rect, "texte": "Partie Difficile"},
    ]

boutons = creer_boutons()

# Boucle principale
while True:
    fenetre.fill(BLANC)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            for bouton in boutons:
                if bouton["rect"].collidepoint(pygame.mouse.get_pos()):
                    bouton["surface"].fill(VERT)
                else:
                    bouton["surface"].fill(BLEU)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for bouton in boutons:
                if bouton["rect"].collidepoint(pygame.mouse.get_pos()):
                    print(bouton["texte"])

    fenetre.blit(fond, (0, 0))  # Afficher le fond d'écran
    for bouton in boutons:
        fenetre.blit(bouton["surface"], bouton["rect"])
        texte_surf = font.render(bouton["texte"], True, BLANC)
        texte_rect = texte_surf.get_rect()
        texte_rect.center = bouton["rect"].center
        fenetre.blit(texte_surf, texte_rect)

    pygame.display.update()
