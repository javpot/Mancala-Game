import random


class Mancala:
    grille = dict(
        {
            "A": 4,
            "B": 4,
            "C": 4,
            "D": 4,
            "E": 4,
            "F": 4,
            "1": 0,
            "G": 4,
            "H": 4,
            "I": 4,
            "J": 4,
            "K": 4,
            "L": 4,
            "2": 0,
        }
    )

    textDifficulty = "None"
    turn = None
    list_puits = list(grille.keys())

    list_images_Puit = [
        "./images/e.jpg",
        "./images/1.jpg",
        "./images/2.jpg",
        "./images/3.jpg",
        "./images/4.jpg",
        "./images/5.jpg",
    ]
    list_images_Panier = [
        "./images/se.jpg",
        "./images/s1.jpg",
        "./images/s2.jpg",
        "./images/s3.jpg",
        "./images/s4.jpg",
        "./images/s5.jpg",
    ]
    images_Puit = {
        0: list_images_Puit[0],
        1: list_images_Puit[1],
        2: list_images_Puit[2],
        3: list_images_Puit[3],
        4: list_images_Puit[4],
        5: list_images_Puit[5],
    }
    images_Panier = {
        0: list_images_Panier[0],
        1: list_images_Panier[1],
        2: list_images_Panier[2],
        3: list_images_Panier[3],
        4: list_images_Panier[4],
        5: list_images_Panier[5],
    }

    def dessinerPuit(nbgraines: int):
        return Mancala.images_Puit.get(nbgraines, "./images/m.jpg")

    def dessinerPanier(nbgraines):
        return Mancala.images_Panier.get(nbgraines, "./images/sm.jpg")

    def nouvelleGrille():
        nvGrille = dict(
            {
                "A": 4,
                "B": 4,
                "C": 4,
                "D": 4,
                "E": 4,
                "F": 4,
                "1": 0,
                "G": 4,
                "H": 4,
                "I": 4,
                "J": 4,
                "K": 4,
                "L": 4,
                "2": 0,
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

    def difficulty(text):
        if text == "Facile":
            Agent.randomAgent(Mancala.grille)
        elif text == "Moyen":
            Agent.maxAgent(Mancala.grille)
        elif text == "Difficile":
            Agent.make_best_move()
        else:
            Agent.make_best_move()

    def joueurDeplacement(id):
        if Mancala.turn is True:
            if Mancala.list_puits[id] in "ABCDEF":
                Mancala.deplacer(id, Mancala.list_puits, 6)
                if Mancala.jouerEncore(id, 6):
                    Mancala.turn = True
                else:
                    Mancala.turn = False
                Mancala.grille[Mancala.list_puits[id]] = 0
                Mancala.verifierGagnant()

    def ordiDeplacement():
        if Mancala.turn is False:
            Mancala.difficulty(Mancala.textDifficulty)
            Mancala.verifierGagnant()

    def verifierPartieTerminer():
        list_puits = list(Mancala.grille.values())
        sumOrdi = sum(list_puits[7:13])
        sumJoueur = sum(list_puits[0:6])
        if sumOrdi == 0 or sumJoueur == 0:
            return True
        else:
            return False

    def verifierGagnant():
        list_puits = list(Mancala.grille.values())
        if Mancala.verifierPartieTerminer():
            sumOrdi = sum(list_puits[7:13])
            sumJoueur = sum(list_puits[0:6])
            panierOrdi = list_puits[13] + sumOrdi
            panierJoueur = list_puits[6] + sumJoueur
            if panierJoueur > panierOrdi:
                return f"Joueur Gagner avec {panierJoueur} points"
            else:
                return f"Ordi Gagner avec {panierOrdi} points"
        else:
            return "Partie pas encore termine"

    def jouerEncore(id, idPanier):
        lettrePuit = Mancala.list_puits[id]
        nbGrainesPuit = Mancala.grille[lettrePuit] - 1
        if (id + nbGrainesPuit) == idPanier:
            return True
        else:
            return False

    def volerGraines(id, idPanier):
        lettrePuit = Mancala.list_puits[id]
        panier = Mancala.list_puits[idPanier]
        nbGrainesPuit = Mancala.grille[lettrePuit] - 1

        dernierPuit = id + nbGrainesPuit
        if dernierPuit > 13:
            num = dernierPuit - len(Mancala.list_puits)
            indexDernierP = num - 1
            if indexDernierP == -1:
                indexDernierP = 0
        elif dernierPuit == 13 or dernierPuit == 6:
            return False
        else:
            indexDernierP = dernierPuit

        lettreDernierP = Mancala.list_puits[indexDernierP]
        nbGrainesDernierP = Mancala.grille[lettreDernierP]

        if nbGrainesDernierP == 1:
            indexPuitOpp = Mancala.puitsOpp[indexDernierP]
            lettrePuitOpp = Mancala.list_puits[indexPuitOpp]
            nbGPuitOpp = Mancala.grille[lettrePuitOpp]
            if nbGPuitOpp > 0:
                Mancala.grille[lettrePuitOpp] = 0
                Mancala.grille[lettreDernierP] = 0
                sommeGr = nbGrainesDernierP + nbGPuitOpp
                Mancala.grille[panier] += sommeGr
        Mancala.turn = False

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
        Mancala.verifierGagnant()


class Agent:
    puits_valides = [
        lettre
        for lettre, graines in Mancala.grille.items()
        if graines > 0 and lettre in "GHIJKL"
    ]

    def randomAgent(grille):
        if Agent.puits_valides:
            choix_puit = random.choice(Agent.puits_valides)
            Mancala.deplacer(
                Mancala.list_puits.index(choix_puit), Mancala.list_puits, 13
            )
            if Mancala.jouerEncore(Mancala.list_puits.index(choix_puit), 13):
                Mancala.turn = False
            else:
                Mancala.turn = True
            Mancala.grille[choix_puit] = 0
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
        else:
            choix_puit = Agent.randomAgent(Mancala.grille)
        Mancala.deplacer(Mancala.list_puits.index(choix_puit), Mancala.list_puits, 13)
        if Mancala.jouerEncore(Mancala.list_puits.index(choix_puit), 13):
            Mancala.turn = False
        else:
            Mancala.turn = True
            Mancala.grille[choix_puit] = 0

    def make_best_move():
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
            Mancala.deplacer(
                Mancala.list_puits.index(best_move), Mancala.list_puits, 13
            )
            if Mancala.jouerEncore(Mancala.list_puits.index(best_move), 13):
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
