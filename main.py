"""FICHIER PRINCIPAL DE PROGRAMMATION PROCEDURALE
"""

from labos.labo_1 import Labo_1
from labos.labo_2 import Labo_2
from labos.labo_3 import Labo_3
from labos.labo_4 import Labo_4


def choose_labo():
    print("""----------------------------------
    PROGRAMMATION PROCEDURALE
----------------------------------

    Veuillez choisir le Labo:

    1. Labo 1
    2. Labo 2
    3. Labo 3
    4. Labo 4
    """)

    labo = input(" --> Labo choisi: ")

    match labo:
        case "1":
            Labo_1()

        case "2":
            Labo_2()

        case "3":
            Labo_3()

        case "4":
            Labo_4()

        case other:
            print("Labo inconnu")


if __name__ == '__main__':
    choose_labo()
