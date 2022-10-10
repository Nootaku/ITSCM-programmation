"""LABO 4

ENONCE DU LABO:
---------------

1. Écrire une fonction prenant en paramètre un nombre entier et retournant sa
factorielle.
L’algorithme devra être itératif.
Cette fonction sera nommée :  iterativfactoriel()

2. Écrire une fonction prenant en paramètre un nombre entier et retournant sa
factorielle.
L’algorithme devra être récursif.
Cette fonction sera nommée :  recursivfactoriel()

3. Écrire une procédure prenant en paramètre un nombre entier et permettant
d’afficher la suite de Fibonacci qui précéde le nombre entré en paramètre et
cela de manière récursive.
Exemple : 5 en paramètre affiche : 0 1 1 2 3
Cette fonction sera nommée :  fibonacci()

BONUS :

4. Écrire une fonction prenant en paramètre un tableau JSON et affichant tous
les noms d’élèves de ce tableau et cela de manière récursive.
Cette fonction sera nommée :  findstud()
"""

from labos.labo_class import Laboratoire
from helpers.factiorial import (
    recursive_factorial,
    recursive_fibonacci,
    recursive_student,
    flatten_list
)


student_list = [
    {
        'genre': 'groupe',
        'nom': '2e',
        'étudiants': [
            {
                'genre': 'étudiant',
                'nom': 'Vanbergen',
                'prénom': 'Georges'
            },
            {
                'genre': 'groupe',
                'nom': 'télécom',
                'étudiants': [
                    {
                        'genre': 'étudiant',
                        'nom': 'Debrouwere',
                        'prénom': 'Eric'
                    },
                    {
                        'genre': 'étudiant',
                        'nom': 'Folley',
                        'prénom': 'Axel'
                    },
                ]
            },
            {
                'genre': 'groupe',
                'nom': 'électronique',
                'étudiants': [
                    {
                        'genre': 'étudiant',
                        'nom': 'Debrecht',
                        'prénom': 'Patrick'
                    },
                    {
                        'genre': 'étudiant',
                        'nom': 'Jackson',
                        'prénom': 'Eliot'
                    },
                ]
            }
        ]
    }
]


class Labo_4(Laboratoire):
    def iterativfactoriel(self, n: int = 5) -> int:
        """Retourne la factorielle d'un nombre entier en utilisant la méthode
        itérative.

        Note:
            - La factorielle d'un entier naturel n est le produit des nombres
            entiers strictement positifs inférieurs ou égaux à n.
            --> https://fr.wikipedia.org/wiki/Factorielle
        """
        # Strictement positifs
        if n < 0:
            return "Nombre positif requis."

        if n < 2:
            return 1

        factorial = 1

        for i in range(1, n + 1):
            factorial = factorial * i

        return factorial

    def recursivfactoriel(self, n: int = 5) -> int:
        """Retourne la factorielle d'un nombre entier en utilisant la méthode
        recursive.
        """
        # Strictement positifs
        if n < 0:
            return "Nombre positif requis."

        if n < 1:
            return 1

        return recursive_factorial(n)

    def fibonacci(self, n: int = 5) -> list[int]:
        """Retroune un string représentant les n premiers chiffres de la suite
        de fibonacci de manière récursive.

        Note:
            Le calcul de la suite de fibonacci se fait par récursion, mais
            afin de rendre le résultat lisible, l'appel de la fonction
            récursive se fait par itération.
        """
        fibonacci_series = [recursive_fibonacci(i) for i in range(n)]
        return fibonacci_series

    def findstud(self, student_table: list = student_list) -> list:
        """Retourne la liste des étudiants présent dans le tableau d'&tudiants
        de manière révursive.

        Note:
            L'obtention des nom d'éleves se fait par récursion, mais
            afin de rendre le résultat lisible, l'appel de la fonction
            récursive se fait par itération.
        """
        student_names = [recursive_student(i) for i in student_table]
        flat_list = flatten_list(student_names)
        return flat_list
