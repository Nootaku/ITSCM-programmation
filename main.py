"""FICHIER PRINCIPAL DE PROGRAMMATION PROCEDURALE
"""

from labos.labo_1 import Labo_1
from labos.labo_2 import Labo_2


def choose_labo():
    print("""----------------------------------
    PROGRAMMATION PROCEDURALE
----------------------------------

    Veuillez choisir le Labo:

    1. Labo 1
    2. Labo 2
    """)

    labo = input(" --> Labo choisi: ")

    match labo:
        case "1":
            exercice = Labo_1()

        case "2":
            exercice = Labo_2()

        case other:
            print("Labo inconnu")


if __name__ == '__main__':
    choose_labo()
