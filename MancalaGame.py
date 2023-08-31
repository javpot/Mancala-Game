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
        if listPuits[id] in "ABCDEF":
            for p in range(0, nbGrainesPuit):
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

    def ordiDeplacement():
        return False

    def verifierGagnant():
        if True:
            pass
        return False
