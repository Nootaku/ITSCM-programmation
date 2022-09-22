"""LABO 1

NOTE:
-----
Nous ne créons pas de paramètres par défaut car, comme nous sommes au sein
d'une classe, il faut d'abord appeler l'objet self (équivalent à 'this' dans
d'autres languages) pour pouvoir avoir accès aux méthodes de classe.
Du coup, on ne peux définir une fonction avec des paramètres correspondant à
l'appel d'une fonction de classe.

ENONCE DU LABO:
---------------
1. Ecrire une méthode prenant en paramètre 2 entiers a et b, génère un nombre entier de
manière « aléatoire » compris entre a et b, et le retourne.
Cette méthode sera nommée :  gennum()

2. Ecrire une méthode qui créé une liste de nombres entiers générés à l’aide de la méthode
gennum () et qui la retourne. Cette méthode sera nommée :  genlist()

3. Écrire une méthode qui reçoit en paramètre une liste d’entiers et affiche son contenu.
Cette méthode sera nommée :  printlist()

4. Écrire une méthode qui reçoit en paramètre un nombre entier et qui vérifie si la valeur est
paire ou impaire. Cette méthode retourne un booléen (true si paire et false si impaire).
Elle sera nommée :  ispair()

5. Écrire une méthode qui reçoit en paramètre 2 listes d’entiers et qui retourne la valeur la plus
grande de ces 2 listes. Cette méthode sera nommée :  maxnumber()

6. Écrire une méthode qui reçoit en paramètre 2 listes d’entiers et qui retourne la valeur la plus
petite de ces 2 listes. Cette méthode sera nommée :  minnumber()

7. Écrire une méthode qui reçoit en paramètre une liste d’entiers, copie ses éléments sauf les
valeurs paires dans l’ordre inverse et la retourne.
Cette méthode sera nommée :  inverslist()

8. Écrire une méthode qui reçoit en paramètre une dimension N et M, génère une liste
d’entiers à 2 dimensions, la remplie à l’aide de la méthode gennum() et la retourne.
Cette méthode sera nommée : genlist2d()
Un exercice supplémentaire serait une variante de cet exercice avec genlist() au lieu de
gennum().

9. Écrire une méthode qui reçoit en paramètre une liste d’entiers à 2 dimensions, la convertit
en une liste à 1 dimension via le module numpy et la retourne.
Cette méthode sera nommée :  convto1d()

10.  Écrire une méthode qui reçoit en paramètre une liste d’entiers et retourne une liste
contenant uniquement les valeurs impaires triées dans l’ordre croissant.
Cette méthode sera nommée :  sortlist()

11.  Écrire une méthode principale (si ce n’est pas déjà fait) et appeler toutes les méthodes des
exercices précédents.
"""
import numpy as np
from pprint import PrettyPrinter
from labos.labo_class import Laboratoire
from random import randint

pp = PrettyPrinter(indent=4).pprint


class Labo_1(Laboratoire):
    def gennum(self, a: int = 0, b: int = 10) -> int:
        """Retourne un nombre entier compris entre a et b généré de manière
        aléatoire.
        Par défaut a=0 et b=10
        """
        return randint(a, b)


    def genlist(self, n: int = 10) -> list[int]:
        """Retourne une liste de n nombres entiers générés à l'aide de
        gennum().
        Par défaut n=10
        """
        return [self.gennum() for i in range(n)]

    def printlist(self, input_list: list = [1, 2, 3, "foo", "bar"]):
        """Print le contenu d'une liste.
        Par défaut input_list=[1, 2, 3, 'foo', 'bar']
        """
        pp(input_list)

        return "--> No return value for a print"

    def ispair(self, number: int = None) -> bool:
        """Retourne True si number est pair et False si number est impair.
        """
        # Création d'un nombre par défaut
        if number is None:
            number = self.gennum(0, 100)
            print(f"Le nombre '{number}' est-il pair ?")

        return number % 2 == 0

    def maxnumber(self, a: list[int] = None, b: list[int] = None) -> int:
        """Retourne la plus grande valeur présente dans deux listes.
        """
        # Création de listes par défaut
        if a is None:
            a = self.genlist()
            print(f"Liste 1: {a}")

        if b is None:
            b = self.genlist()
            print(f"Liste 2: {b}")

        max_a = max(a)
        max_b = max(b)

        if max_a > max_b:
            return max_a

        return max_b

    def minnumber(self, a: list[int] = None, b: list[int] = None) -> int:
        """Retourne la plus petite valeur présente dans deux listes.
        """
        # Création de listes par défaut
        if a is None:
            a = self.genlist()
            print(f"Liste 1: {a}")

        if b is None:
            b = self.genlist()
            print(f"Liste 2: {b}")

        min_a = min(a)
        min_b = min(b)

        if min_a > min_b:
            return min_b

        return min_a

    def inverslist(self, int_list: list[int] = None) -> list[int]:
        """Retourne une liste d'entiers. La liste retournée correspond aux
        chiffres impairs de la liste donnée en paramètre inversée.
        """
        # Création d'une liste par défaut
        if int_list is None:
            int_list = self.genlist()
            print(f"Liste d'entiers: {int_list}")

        return_list = [i for i in int_list if self.ispair(i) is False]
        return_list.reverse()

        return return_list

    def convto1d(
        self,
        # la méthode rand(cols (d0), rows (d1)) génère aléatoirement une array
        two_d_array: np.array = np.random.random_integers(0, 10, (3, 5))
    ) -> np.array:
        """Convertit une liste 2D en liste 1D et la retourne.
        Note:
        Nous utilisons des array numpy à la place de listes.
        """
        print("Liste d'entrée:")
        pp(two_d_array)

        print("\nListe de sortie:")
        return two_d_array.flatten().tolist()

    def sortlist(self, int_list: list[int] = None) -> list[int]:
        """Retourne une liste d'entiers correspondant aux chiffres pairs
        ordonnés par order croissant de la liste d'entiers en paramètre.
        """
        # Création d'une liste par défaut
        if int_list is None:
            int_list = self.genlist()
            print(f"Liste d'entiers: {int_list}")

        return_list = [i for i in int_list if self.ispair(i)]
        return_list.sort()

        return return_list
