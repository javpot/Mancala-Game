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

    turn = None

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
        Mancala.turn = None

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
                Mancala.deplacer(id, listPuits, 6)
                if Mancala.jouerEncore(id, 6):
                    Mancala.turn = True
                else:
                    Mancala.turn = False
                Mancala.grille[listPuits[id]] = 0
                Mancala.verifierPartieTerminer()

    def ordiDeplacement():
        Agent.make_best_move()
        Mancala.verifierPartieTerminer()

    def verifierPartieTerminer():
        listPuits = list(Mancala.grille.values())
        sumOrdi = sum(listPuits[7:13])
        sumJoueur = sum(listPuits[0:6])
        if sumOrdi == 0 or sumJoueur == 0:
            return True
        else:
            return False

    def verifierGagnant():
        listPuits = list(Mancala.grille.values())
        if Mancala.verifierPartieTerminer():
            sumOrdi = sum(listPuits[7:13])
            sumJoueur = sum(listPuits[0:6])
            panierOrdi = listPuits[13] + sumOrdi
            panierJoueur = listPuits[6] + sumJoueur
            print(panierJoueur > panierOrdi)
            print("panierOrdi:", panierOrdi, "\npanierJoueur:", panierJoueur)
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
        elif dernierPuit == 13 or dernierPuit == 6:
            return False
        else:
            indexDernierP = dernierPuit

        lettreDernierP = listPuits[indexDernierP]
        nbGrainesDernierP = Mancala.grille[lettreDernierP]

        if nbGrainesDernierP == 1:
            indexPuitOpp = Mancala.puitsOpp[indexDernierP]
            lettrePuitOpp = listPuits[indexPuitOpp]
            nbGPuitOpp = Mancala.grille[lettrePuitOpp]
            if nbGPuitOpp > 0:
                Mancala.grille[lettrePuitOpp] = 0
                Mancala.grille[lettreDernierP] = 0
                sommeGr = nbGrainesDernierP + nbGPuitOpp
                Mancala.grille[panier] += sommeGr
        return False

    def deplacer(id, list, idPanier):
        indexPuit = id
        lettrePuit = list[indexPuit]
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
        Mancala.volerGraines(id, idPanier)


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

    def make_best_move():
        listpuits = list(Mancala.grille.keys())
        best_score = float("-inf")
        best_move = None
        for move in Agent.puits_valides:
            # Cloner l'état actuel pour simuler le mouvement
            cloned_grille = Mancala.grille.copy()
            cloned_turn = Mancala.turn
            Agent.minimax(move, 0)
            score = Agent.minimax(move, 0)

            # Restaurer l'état original
            Mancala.grille = cloned_grille
            Mancala.turn = cloned_turn

            if score > best_score:
                best_score = score
                best_move = move

        if best_move is not None:
            Mancala.deplacer(listpuits.index(best_move), listpuits, 13)
            if Mancala.jouerEncore(listpuits.index(best_move), 13):
                Mancala.turn = False
            else:
                Mancala.turn = True
            Mancala.grille[best_move] = 0

    def minimax(move, depth):
        if depth == 3:  # Ajustez la profondeur de recherche ici
            return Agent.evaluate_board()

        # Cloner l'état actuel pour simuler le mouvement
        cloned_grille = Mancala.grille.copy()
        clone_list = list(cloned_grille.keys())
        cloned_turn = Mancala.turn
        Mancala.deplacer(Agent.puits_valides.index(move), clone_list, 13)

        if Mancala.turn:  # Si c'est le tour du joueur humain
            best_score = float("-inf")
            for next_move in list(Mancala.grille.keys()):
                score = Agent.minimax(next_move, depth + 1)
                best_score = max(score, best_score)
        elif Mancala.turn is False:  # Si c'est le tour de l'ordinateur
            best_score = float("inf")
            for next_move in Agent.puits_valides:
                score = Agent.minimax(next_move, depth + 1)
                best_score = min(score, best_score)

        # Restaurer l'état original
        Mancala.grille = cloned_grille
        Mancala.turn = cloned_turn

        return best_score

    def evaluate_board():
        # Vous pouvez définir votre fonction d'évaluation ici
        # Elle doit retourner une valeur numérique qui indique la qualité de la position actuelle.
        # Par exemple, vous pouvez considérer la différence entre le nombre de graines dans les puits des deux joueurs.
        player_puits = sum(Mancala.grille[letter] for letter in "ABCDEF")
        opponent_puits = sum(Mancala.grille[letter] for letter in "GHIJKL")
        return player_puits - opponent_puits
