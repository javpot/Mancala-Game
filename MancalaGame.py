import random
import tkinter as tk


class Mancala:
    grille = dict(
        {
            "A": 4,
            "B": 4,
            "C": 4,
            "D": 4,
            "E": 4,
            "F": 4,
            "2": 0,
            "L": 4,
            "K": 4,
            "J": 4,
            "I": 4,
            "H": 4,
            "G": 4,
            "1": 0,
        }
    )

    turn = True

    def nouvelleGrille():
        nvGrille = dict(
            {
                "A": 4,
                "B": 4,
                "C": 4,
                "D": 4,
                "E": 4,
                "F": 4,
                "2": 0,
                "L": 4,
                "K": 4,
                "J": 4,
                "I": 4,
                "H": 4,
                "G": 4,
                "1": 0,
            }
        )
        Mancala.grille = nvGrille
        Mancala.turn = True

    def joueurDeplacement(id):
        listPuits = list(Mancala.grille.keys())
        indexPuit = id
        lettrePuit = listPuits[id]
        nbGrainesPuit = Mancala.grille[lettrePuit]
        if Mancala.turn is True:
            if listPuits[id] in "ABCDEF":
                for p in range(0, nbGrainesPuit + 1):
                    lettrePuit = listPuits[indexPuit]
                    nbGrainesPuit = Mancala.grille[lettrePuit]
                    # Gerer index > 13
                    if indexPuit >= 13:
                        indexPuit = 0
                        nbGrainesPuit += 1
                    elif indexPuit in range(0, 13):
                        indexPuit += 1
                        nbGrainesPuit += 1
                        print(
                            "DB label, nbGraines: ",
                            lettrePuit,
                            ", ",
                            nbGrainesPuit,
                        )
                        print("DB positionCurrent: ", indexPuit)
                    Mancala.grille[lettrePuit] = nbGrainesPuit
                Mancala.grille[listPuits[id]] = 0
                Mancala.turn = False

    def ordiDeplacement():
        Mancala.verifierPartieTerminer()
        #        choix_agent = Agent.randomAgent(Mancala.grille)
        choix_agent = Agent.maxAgent(Mancala.grille)
        if choix_agent:
            lettrePuit = choix_agent
            indexPuit = list(Mancala.grille.keys()).index(lettrePuit)
            id = indexPuit
            listPuits = list(Mancala.grille.keys())
            nbGrainesPuit = Mancala.grille[lettrePuit]
            if Mancala.turn is False:
                for p in range(0, nbGrainesPuit + 1):
                    lettrePuit = listPuits[indexPuit]
                    nbGrainesPuit = Mancala.grille[lettrePuit]

                    # Gerer index > 13
                    if indexPuit >= 13:
                        indexPuit = 0
                        nbGrainesPuit += 1
                    elif indexPuit in range(0, 13):
                        indexPuit += 1
                        nbGrainesPuit += 1
                        print(
                            "DB label, nbGraines: ",
                            lettrePuit,
                            ", ",
                            nbGrainesPuit,
                        )
                        print("DB positionCurrent: ", indexPuit)
                    Mancala.grille[lettrePuit] = nbGrainesPuit
                Mancala.grille[listPuits[id]] = 0
                Mancala.turn = True
        else:
            print("L'ordinateur ne peut pas effectuer de mouvement valide.")
            Mancala.turn = True

    def verifierPartieTerminer():
        listPuits = list(Mancala.grille.values())
        for x in range(0, 6):
            if listPuits[x] == 0:
                continue
            return Mancala.verifierGagnant()
        for y in range(7, 13):
            if listPuits[y] == 0:
                continue
            return Mancala.verifierGagnant()
        return False

    def verifierGagnant():
        listPuits = list(Mancala.grille.values())
        panierOrdi = listPuits[13]
        panierJoueur = listPuits[6]
        return panierJoueur > panierOrdi

    def jouerEncore(id):
        listPuits = list(Mancala.grille.keys())
        lettrePuit = listPuits[id]
        nbGrainesPuit = Mancala.grille[lettrePuit]

        return False


class Agent:
    puits_valides = [
        lettre
        for lettre, graines in Mancala.grille.items()
        if graines > 0 and lettre in "GHIJKL"
    ]

    def randomAgent(grille):
        if Agent.puits_valides:
            choix_puit = random.choice(Agent.puits_valides)
            return choix_puit
        else:
            return None

    def maxAgent(grille):
        index = Agent.puits_valides[0]
        max = Mancala.grille[index]

        choix_max = [
            lettre
            for lettre, graines in Mancala.grille.items()
            if graines > max and lettre in "GHIJKL"
        ]
        if choix_max:
            choix_puit = random.choice(choix_max)
            return choix_puit
        return Agent.randomAgent(Mancala.grille)
