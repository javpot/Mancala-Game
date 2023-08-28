class Mancala:
    grille = dict(
        {
            "1": 0,
            "G": 4,
            "H": 4,
            "I": 4,
            "J": 4,
            "K": 4,
            "L": 4,
            "2": 0,
            "A": 4,
            "B": 4,
            "C": 4,
            "D": 4,
            "E": 4,
            "F": 4,
        }
    )

    def nouvelleGrille():
        nvGrille = dict(
            {
                "1": 0,
                "G": 4,
                "H": 4,
                "I": 4,
                "J": 4,
                "K": 4,
                "L": 4,
                "2": 0,
                "A": 4,
                "B": 4,
                "C": 4,
                "D": 4,
                "E": 4,
                "F": 4,
            }
        )
        Mancala.grille = nvGrille

    def joueurDeplacement(id):
        listPuits = list(Mancala.grille.keys())
        indexPuit = id
        lettrePuit = listPuits[indexPuit]
        nbGrainesPuit = Mancala.grille[lettrePuit]
        if lettrePuit in "ABCDEF":
            for p in range(0, nbGrainesPuit + 1):
                puitPresent = listPuits[indexPuit]
                nbGrainesPuit = Mancala.grille[puitPresent]
                # Gerer le 13
                if indexPuit == 13:
                    nbGrainesPuit += 1
                    indexPuit = 7
                # Gerer le 0
                elif indexPuit == 0:
                    nbGrainesPuit += 1
                    indexPuit = 8

                # Gerer les positions a 1 a 7
                elif indexPuit >= 1 and indexPuit <= 7:
                    nbGrainesPuit += 1
                    indexPuit -= 1

                # Gerer les positions de 8 a 12
                elif indexPuit >= 8 and indexPuit < 13:
                    indexPuit += 1
                    puitPresent = listPuits[indexPuit]
                    nbGrainesPuit += 1

                print(
                    "DB label, nbGraines: ",
                    puitPresent,
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
