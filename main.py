"""FICHIER PRINCIPAL DE PROGRAMMATION PROCEDURALE
"""

from labos.labo_1 import Labo_1
def choose_labo():
    print("""------------------------------
    PROGRAMMATION PROCEDURALE
------------------------------

    Veuillez choisir le Labo:

    1. Labo 1
    2. Labo 2
    """)

    labo = input(" --> Labo choisi: ")

    match labo:
        case "1":
            test = Labo_1()

        case "2":
            print("Labo 2")

        case other:
            print("Labo inconnu")


if __name__ == '__main__':
    choose_labo()
