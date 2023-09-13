import tkinter as tk
from Puit import Puit
from MancalaGame import Mancala


def event_puit(id):
    print(id)
    Mancala.joueurDeplacement(id)
    # faire une methode jeu pour le deroulement automatique du jeu
    for p in puits:
        puitGraines = Mancala.grille[p.label]
        p.bouton.configure(text=puitGraines)
    print(Mancala.grille)


def event_reset():
    Mancala.nouvelleGrille()
    for x in puits:
        nvPuitGraines = Mancala.grille[x.label]
        x.nbGraines = nvPuitGraines
        x.bouton.configure(text=nvPuitGraines)


if __name__ == "__main__":
    puits = []

    puits.append(Puit("A", 100, 200, 100, 100, 4))
    puits.append(Puit("B", 200, 200, 100, 100, 4))
    puits.append(Puit("C", 300, 200, 100, 100, 4))
    puits.append(Puit("D", 400, 200, 100, 100, 4))
    puits.append(Puit("E", 500, 200, 100, 100, 4))
    puits.append(Puit("F", 600, 200, 100, 100, 4))
    puits.append(Puit("1", 0, 0, 100, 300, 0))
    puits.append(Puit("G", 100, 0, 100, 100, 4))
    puits.append(Puit("H", 200, 0, 100, 100, 4))
    puits.append(Puit("I", 300, 0, 100, 100, 4))
    puits.append(Puit("J", 400, 0, 100, 100, 4))
    puits.append(Puit("K", 500, 0, 100, 100, 4))
    puits.append(Puit("L", 600, 0, 100, 100, 4))
    puits.append(Puit("2", 700, 0, 100, 300, 0))

    root = tk.Tk()
    root.resizable(False, False)
    root.title("Projet 1 - Zafer/Javen")
    tk.Label(root, text="Mancala", font=("Arial", 25), fg="red").pack()

    play_area = tk.Frame(root, width=800, height=300, bg="white")

    for i, puit in enumerate(puits):
        puit.bouton = tk.Button(
            play_area,
            text=str(puit.nbGraines),
            font=("Arial", 15),
            command=lambda id=i: event_puit(id),
        )
        puit.bouton.place(x=puit.x, y=puit.y, width=puit.width, height=puit.height)

    status_label = tk.Label(
        play_area, text="Message ici", font=("Arial", 16), bg="white"
    )
    status_label.place(x=100, y=100, width=600, height=100)

    play_area.pack(pady=10, padx=10)

    play_again_button = tk.Button(
        root, text="Nouvelle partie", font=("Arial", 12), command=event_reset
    )
    play_again_button.pack(pady=10)

    root.mainloop()

"""
 G +------+------+--<<<<<-Joueur 2----+------+------+------+ G
 R |      |L     |K     |J     |I     |H     |G     |      | R
 E |      |   4  |   4  |   4  |   4  |   4  |   4  |      | E
 N |      |      |      |      |      |      |      |      | N
 I |   0  +------+------+------+------+------+------+   0  | I
 E |      |A     |B     |C     |D     |E     |F     |      | E
 R |      |   4  |   4  |   4  |   4  |   4  |   4  |      | R
   |      |      |      |      |      |      |      |      | 
 2 +------+------+------+-Joueur 1->>>>>-----+------+------+ 1
"""
