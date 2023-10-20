import pygame
class Puit:
    def __init__(self, label, x, y, width, height, nbGraines,image):
        self.label = label
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.nbGraines = nbGraines
        self.bouton = 0
        self.image = image
        self.rect = pygame.Rect(x, y, width, height)
