from Puit import Puit

grille = {
    "1": 0,
    "A": 4,
    "B": 4,
    "C": 4,
    "D": 4,
    "E": 4,
    "F": 4,
    "G": 4,
    "H": 4,
    "I": 4,
    "J": 4,
    "K": 4,
    "L": 4,
    "2": 0,
}


def nouvelleGrille():
    return


def joueurDeplacement(etiquette):
    if etiquette in "ABCDEF":
        return True
    return False


def ordiDeplacement():
    return False


def verifierGagnant():
    return False
