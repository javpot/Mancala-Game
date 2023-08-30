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
            "G": 4,
            "H": 4,
            "I": 4,
            "J": 4,
            "K": 4,
            "L": 4,
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
                "G": 4,
                "H": 4,
                "I": 4,
                "J": 4,
                "K": 4,
                "L": 4,
                "1": 0,
            }
        )
        Mancala.grille = nvGrille

    def joueurDeplacement(id):
        print(id)
        listPuits = list(Mancala.grille.keys())
        indexPuit = id + 1
        lettrePuit = listPuits[indexPuit]
        nbGrainesPuit = Mancala.grille[lettrePuit]
        if listPuits[id] in "GHIJKL":
            for p in range(0, nbGrainesPuit):
                nbGrainesPuit = Mancala.grille[lettrePuit]
                # Gerer index >= 13
                if indexPuit >= 13:
                    nbGrainesPuit += 1
                    indexPuit = 0
            Mancala.grille[lettrePuit] = nbGrainesPuit
            print(
                "DB label, nbGraines: ",
                lettrePuit,
                ", ",
                nbGrainesPuit,
            )
            print("DB positionCurrent: ", indexPuit)
        Mancala.grille[listPuits[id]] = 0

    def ordiDeplacement():
        return False

    def verifierGagnant():
        if True:
            pass
        return False
