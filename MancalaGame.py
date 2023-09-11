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
                print(Mancala.verifierGagnantJoueur())

    def ordiDeplacement():
        Mancala.verifierGagnantOrdi()
        return False

    def verifierGagnantJoueur():
        listPuits = list(Mancala.grille.values())
        for x in range(0, 6):
            if listPuits[x] == 0:
                continue
            else:
                return "Non gagnant"

        return "Player has won the game"

    def verifierGagnantOrdi():
        listPuits = list(Mancala.grille.values())
        for x in range(7, 13):
            if listPuits[x] == 0:
                continue
            else:
                return "Non gagnant"

        return "Ordi has won the game"
