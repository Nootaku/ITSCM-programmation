"""LABO 3

ENONCE DU LABO:
---------------
1. Sur base de l'exercice 6 du laboratoire n°2, écrire une fonction qui prend
en paramètre un dictionnaire et qui le trie en utilisant le tri à bulles.
Le tri s'effectuera sur base de la clé et la fonction retournera le
dictionnaire trié.
Cette fonction sera nommée :  bubbleSort()

2. Sur base de l'exercice 6 du laboratoire n°2, écrire une fonction qui prend
en paramètre un dictionnaire et qui le trie en utilisant le tri par insertion.
Le tri s'effectuera sur base de la clé et la fonction retournera le
dictionnaire trié.
Cette fonction sera nommée :  insertSort()

3. Sur base de l'exercice 6 du laboratoire n°2, écrire une fonction qui prend
en paramètre un dictionnaire et qui le trie en utilisant le tri par sélection.
Le tri s'effectuera sur base de la clé et la fonction retournera le
dictionnaire trié.
Cette fonction sera nommée :  selectSort()

4. Sur base de l'exercice 6 du laboratoire n°2, écrire une fonction qui prend
en paramètre un dictionnaire et qui le trie en utilisant le tri par fusion.
Le tri s'effectuera sur base de la clé et la fonction retournera le
dictionnaire trié.
Cette fonction sera nommée :  fusionSort()

5. Sur base de l'exercice 6 du laboratoire n°2, écrire une fonction qui prend
en paramètre un dictionnaire et qui le trie en utilisant la fonction native
sorted().
Le tri s'effectuera sur base de la clé et la fonction retournera le
dictionnaire trié.
Cette fonction sera nommée :  sortedSort()

6. Sur base de l'exercice 6 du laboratoire n°2, écrire une fonction qui prend
en paramètre un dictionnaire et qui le trie en utilisant la fonction native
sort().
Le tri s'effectuera sur base de la clé et la fonction retournera le
dictionnaire trié.
Cette fonction sera nommée :  sortSort()
"""

from labos.labo_class import Laboratoire
from helpers.sorting import mergeSort


def splitdict():
    """Pour un dictionnaire par défaut (stud), retourne 2 dictionnaires:
        - studpass: contient les clés/valeurs dont la valeur est > 9
        - studfail: contient les clés/valeurs dont la valeur est < 10
    """
    # Génération du dictionnaire par défaut
    stud = {
        "stud 1": 14,
        "stud 2": 13,
        "stud 3": 9,
        "stud 4": 12,
        "stud 5": 3,
        "stud 6": 8,
        "stud 7": 16,
        "stud 8": 13,
        "stud 9": 13,
        "stud 10": 15,
        "stud 11": 14,
        "stud 12": 19,
        "stud 13": 10,
        "stud 14": 10,
        "stud 15": 13,
        "stud 16": 7,
        "stud 17": 12,
        "stud 18": 15,
        "stud 19": 9,
        "stud 20": 17
    }

    # Split du dictionnaire
    # cette méthode nous permèt de n'itérer le dictionnaire stud qu'une
    # seule fois
    studpass = dict()

    for key, value in stud.items():
        if value > 9:
            studpass[key] = value

    return studpass


class Labo_3(Laboratoire):
    def bubbleSort(self, dict_to_be_sorted: dict = splitdict()) -> dict:
        """Trie un dictionnaire sur base du nom de la clé en utilisant un Tri
        à Bulles (Bubble Sort).

        Note - opérateur logique sur des string:
            En python il est possible d'exécuter des opérateurs logique sur
            des strings. Ceci résulte en:
            "a" < "b" == True
            Cependant, l'opérateur ne considère pas la longueur du string
            comme un élément logique. Ainsi:
            "a 10" < "a 2" == True

        Note - Tri à Bulles - O(n^2):
            Si j'ai 3 index [5, 1, 3], le Tri à Bulles (TB) commence toujours
            par l'index 0 et demande: "est-ce que index 0 est > que index 1 ?"
            --> Si oui, il inverse les indexs
            --> Si non, il ne fait rien
            Ensuite il passe à l'index 1 et repose la même question:
            "index 1 > index 2 ?"
            Et ainsi de suite jusqu'à la fin de la liste.
            Ceci est une itération et permet de trié le chiffre le plus grand
            en fin de liste.

            En d'autres termes, il faut traverser la liste n fois (ou n est la
            longueur de la liste) et chaque iteration trie 1 chiffre.
            D'abord n puis n-1, puis n-2 etc.
        """
        print(f"Dictionnaire: {dict_to_be_sorted}")
        key_list = list(dict_to_be_sorted.keys())

        # Longueur du Dictionnaire
        n = len(key_list)

        # Itération pour chaque element dans la liste:
        for i in range(n):
            # Itération de chaque élément SAUF ceux qui sont déjà triés:
            for j in range(0, n - i - 1):
                # Echange de la place de l'élément si celui-ci est plus grand
                # que l'élément qui le suit:
                if key_list[j] > key_list[j + 1]:
                    key_list[j], key_list[j + 1] = key_list[j + 1], key_list[j]

        # Création d'un nouveau dictionnaire
        new_dict = {}
        for i in key_list:
            new_dict[i] = dict_to_be_sorted[i]

        print("Résultat:")
        return new_dict

    def insertSort(self, dict_to_be_sorted: dict = splitdict()) -> dict:
        """Trie un dictionnaire sur base du nom de la clé en utilisant un tri
        par insertion.

        Note - Tri par Insertion (Insertion Sort):
            Le Tri par Insertion fait une itération de chaque élément de la
            liste. Pour chaque élément a l'indice n, on va comparé l'élément
            à n - 1.
            Si n < n - 1, alors on va échanger la place des deux éléments puis
            comparer n à n - 2 et ainsi de suite.
        """
        print(f"Dictionnaire: {dict_to_be_sorted}")
        key_list = list(dict_to_be_sorted.keys())

        # Longueur du Dictionnaire
        n = len(key_list)

        # Itération pour chaque élément de la liste commencant au 2ème élément
        for i in range(1, n):
            # mise en mémoire de l'élément
            value = key_list[i]

            # création d'un pointeur
            previous_key = i - 1

            # Loop jusqu'à ce qu'on trouve une valeur plus petite
            # On ne peux pas avoir d'index inférieur à 0
            while (
                previous_key >= 0 and
                value < key_list[previous_key]
            ):
                # Si la valeur de l'élément est plus petite que la valeur de
                # l'élément précédent, inverser les valeurs
                key_list[previous_key + 1] = key_list[previous_key]
                previous_key -= 1

            key_list[previous_key + 1] = value

        # Création d'un nouveau dictionnaire
        new_dict = {}
        for i in key_list:
            new_dict[i] = dict_to_be_sorted[i]

        print("Résultat:")
        return new_dict

    def selectSort(self, dict_to_be_sorted: dict = splitdict()) -> dict:
        """Trie un dictionnaire sur base du nom de la clé en utilisant un tri
        par sélection.

        Note - Tri par sélection - Select Sort:
            Pour chaque élément de la liste de longeur n avec un index i
            on set une valeur minimale à i
            si la valeure minimale est suppérieure à i+1 alors la nouvelle
            valeur minimale devient i+1.
            Le processus est répété jusqu'à arriver a n
            Ceci défini le premier élément de la liste triée.
            On répète ce processus entier jusqu'à ce que toute la liste soit
            triée.
        """
        print(f"Dictionnaire: {dict_to_be_sorted}")
        key_list = list(dict_to_be_sorted.keys())

        # Longueur du Dictionnaire
        n = len(key_list)

        # Itération, pas besoin de faire le dernier élément car le select sort compare
        # avec les chiffres qui suivent. Le dernier élément est donc toujours trié.
        for i in range(n - 1):
            # Création d'un pointeur
            min_index = i

            # Iteration (n - 1 car on compare à )
            for j in range(i + 1, n):
                if key_list[j] < key_list[min_index]:
                    min_index = j

            key_list[i], key_list[min_index] = key_list[min_index], key_list[i]

    # Création d'un nouveau dictionnaire
        new_dict = {}
        for i in key_list:
            new_dict[i] = dict_to_be_sorted[i]

        print("Résultat:")
        return new_dict

    def fusionSort(self, dict_to_be_sorted: dict = splitdict()) -> dict:
        """Trie un dictionnaire sur base du nom de la clé en utilisant tri par fusion.

        Note - Tri par fusion - Merge sort:
            Le tri par fusion consiste à subdiviser une liste en plus petites
            listes jusqu'à obtenir des éléments individuels, puis à
            reconstituer les listes en triant les éléments à l'aide de
            pointeurs.
            Chaque fois qu'un élément est placé dans la liste reconditionnée
            le pointeur avance d'un indice dans sa (sub-)liste respectives
            jusqu'à obtenir une liste complète.
        """
        print(f"Dictionnaire: {dict_to_be_sorted}")
        key_list = list(dict_to_be_sorted.keys())

        # Tri par fusion
        key_list = mergeSort(key_list)

        # Création d'un nouveau dictionnaire
        new_dict = {}
        for i in key_list:
            new_dict[i] = dict_to_be_sorted[i]

        print("Résultat:")
        return new_dict

    def sortedSort(self, dict_to_be_sorted: dict = splitdict()) -> dict:
        """Trie un dictionnaire sur base du nom de la clé en utilisant la
        fonction native sorted().
        """
        print(f"Dictionnaire: {dict_to_be_sorted}")
        key_list = list(dict_to_be_sorted.keys())

        key_list = sorted(key_list)

        # Création d'un nouveau dictionnaire
        new_dict = {}
        for i in key_list:
            new_dict[i] = dict_to_be_sorted[i]

        print("Résultat:")
        return new_dict

    def sortSort(self, dict_to_be_sorted: dict = splitdict()) -> dict:
        """Trie un dictionnaire sur base du nom de la clé en utilisant la
        fonction native sort().
        """
        print(f"Dictionnaire: {dict_to_be_sorted}")
        key_list = list(dict_to_be_sorted.keys())

        key_list.sort()

        # Création d'un nouveau dictionnaire
        new_dict = {}
        for i in key_list:
            new_dict[i] = dict_to_be_sorted[i]

        print("Résultat:")
        return new_dict