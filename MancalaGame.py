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

    puitsOpp = dict(
        {
            0: 12,
            1: 11,
            2: 10,
            3: 9,
            4: 8,
            5: 7,
            12: 0,
            11: 1,
            10: 2,
            9: 3,
            8: 4,
            7: 5,
        }
    )

    def joueurDeplacement(id):
        listPuits = list(Mancala.grille.keys())
        if Mancala.turn is True:
            if listPuits[id] in "ABCDEF":
                Mancala.deplacer(id, listPuits)
                Mancala.volerGraines(id, 6)
                if Mancala.jouerEncore(id, 6):
                    Mancala.turn = True
                else:
                    Mancala.turn = False
                Mancala.grille[listPuits[id]] = 0
                Mancala.verifierPartieTerminer()

    def ordiDeplacement():
        listPuits = list(Mancala.grille.keys())
        if Mancala.turn is False:
            choix_agent = Agent.maxAgent(Mancala.grille)
            lettrePuit = choix_agent
            id = listPuits.index(lettrePuit)
            Mancala.deplacer(id, listPuits)
            Mancala.volerGraines(id, 13)
            if Mancala.jouerEncore(id, 13):
                Mancala.turn = False
            else:
                Mancala.turn = True
            Mancala.grille[listPuits[id]] = 0
            Mancala.verifierPartieTerminer()

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

    def verifierGagnant():
        listPuits = list(Mancala.grille.values())
        panierOrdi = listPuits[13]
        panierJoueur = listPuits[6]
        print(panierJoueur > panierOrdi)
        return panierJoueur > panierOrdi

    def jouerEncore(id, idPanier):
        listPuits = list(Mancala.grille.keys())
        lettrePuit = listPuits[id]
        nbGrainesPuit = Mancala.grille[lettrePuit] - 1
        if (id + nbGrainesPuit) == idPanier:
            return True
        else:
            return False

    def volerGraines(id, idPanier):
        listPuits = list(Mancala.grille.keys())
        lettrePuit = listPuits[id]
        panier = listPuits[idPanier]
        nbGrainesPuit = Mancala.grille[lettrePuit] - 1

        dernierPuit = id + nbGrainesPuit
        if dernierPuit > 13:
            num = dernierPuit - len(listPuits)
            indexDernierP = num - 1
            if indexDernierP == -1:
                indexDernierP = 0
        else:
            indexDernierP = dernierPuit
            if indexDernierP == 6 or indexDernierP == 13:
                return False

        lettreDernierP = listPuits[indexDernierP]
        nbGrainesDernierP = Mancala.grille[lettreDernierP]

        if nbGrainesDernierP == 1:
            indexPuitOpp = Mancala.puitsOpp[indexDernierP]
            lettrePuitOpp = listPuits[indexPuitOpp]
            nbGPuitOpp = Mancala.grille[lettrePuitOpp]
            Mancala.grille[lettrePuitOpp] = 0
            Mancala.grille[lettreDernierP] = 0
            sommeGr = nbGrainesDernierP + nbGPuitOpp
            Mancala.grille[panier] += sommeGr

    def deplacer(id, list):
        indexPuit = id
        lettrePuit = list[id]
        nbGrainesPuit = Mancala.grille[lettrePuit]

        for p in range(0, nbGrainesPuit + 1):
            lettrePuit = list[indexPuit]
            nbGrainesPuit = Mancala.grille[lettrePuit]
            # Gerer index > 13
            if indexPuit >= 13:
                indexPuit = 0
                nbGrainesPuit += 1
            elif indexPuit in range(0, 13):
                indexPuit += 1
                nbGrainesPuit += 1
            Mancala.grille[lettrePuit] = nbGrainesPuit


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
