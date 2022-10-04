"""LAB0 2

ENONCE DU LABO:
---------------
1. Ecrire une fonction qui génère une liste comprenant des entier
pseudo-aléatoire compris entre a et b, et la retourne. Cette fonction
prendre en paramètre a, b et la taille de la liste.
Cette fonction sera nommée :  genlist2()

2. Ecrire une fonction qui créé un tuple de nombres entiers générés à l'aide
de la fonction gennum () et qui le retourne.
Cette fonction sera nommée :  gentuple()

3. Écrire une fonction qui reçoit en paramètre 1 liste d'entiers et la
convertit en tuple.
Cette fonction sera nommée :  totuple()

4. Écrire une fonction qui reçoit en paramètre 1 listes d'entier et vérifie si
elle contient des doublons. Elle devra ensuite retourner une liste sans
doublon.
Elle sera nommée :  noduplicate()

5. Écrire une fonction qui reçoit en paramètre 2 listes d'entier, les
concatène et convertit la résultante en set. Cette fonction retourne un
booléen, true si le set contient des valeurs et false si il est vide.
Elle sera nommée :  toset()

6. Écrire une fonction qui génère le dictionnaire suivant :

stud = {" stud 1" : 14 , " stud 2" : 13 , " stud 3" : 9 , " stud 4" : 12 ,
 " stud 5" : 3 , " stud 6" : 8 , " stud 7" : 16 , " stud 8" : 13 ,
" stud 9" : 13 , " stud 10" : 15 , " stud 11" : 14 , " stud 12" : 19 ,
" stud 13" : 10 , " stud 14" : 10 , " stud 15" : 13 , " stud 16" : 7 ,
" stud 17" : 12 , " stud 18" : 15 , " stud 19" : 9 , " stud 20" : 17 ,}

Cette fonction devra séparer ce dictionnaire en 2 dictionnaires nommé studpass
dont les valeurs sont supérieures ou égales à 10 et studfail dont les valeurs
sont inférieures à 10. Elle devra ensuite retourner les 2 dictionnaires.
Cette fonction sera nommée :  splitdict()

7. Écrire une fonction qui demande à l'utilisateur d'introduire un nombre et
une lettre. Elle affectera ces données dans un dictionnaire de sorte à ce que
le nombre soit la clé et le chiffre la valeur. La taille du dictionnaire est
reçue en paramètre.
Cette fonction sera nommée :  gendict()

8. Écrire une fonction générant un dictionnaire contenant l'alphabet français.
La clé étant le valeur ASCII de la lettre et la valeur étant la lettre.
Exemple : {97 : "a",   98 : "b",   99 : "c",  ... }
Cette fonction devra ensuite demander d'introduire une clé pour afficher sa
valeur. Et cela jusqu'à ce que l'utilisateur n'a pas introduit 0.
Si l'utilisateur introduit une valeur inférieur ou supérieur aux clés
disponibles, alors la fonction devra afficher « valeur non disponible ».

9. Écrire une fonction principale (si ce n'est pas déjà fait) et appeler
toutes les fonctions des exercices précédents.
"""
from labos.labo_class import Laboratoire
from random import randint


def gennum(a: int = 0, b: int = 10) -> int:
    """Retourne un nombre entier compris entre a et b généré de manière
    aléatoire.
    Par défaut a=0 et b=10
    """
    return randint(a, b)


class Labo_2(Laboratoire):
    def genlist2(self, a: int = 0, b: int = 10, n: int = 10) -> list[int]:
        """Retourne une liste de n entiers compris entre a et b générés
        aléatoirement.
        Par défaut a=0, b=10, n=10
        """
        return [randint(a, b) for i in range(n)]

    def gentuple(self, a: int = 0, b: int = 10) -> tuple:
        """Ecrire une fonction qui créé un tuple de nombres entiers générés à
        l'aide de la fonction gennum () et qui le retourne.
        """
        return (gennum(a, b), gennum(a, b))

    def totuple(self, int_list: list[int] = None) -> tuple:
        """Convertit un liste d'entiers en tuple d'entiers et le retourne.
        """
        # Génération d'une liste par défaut
        if int_list is None:
            int_list = self.genlist2()
            print(f"Liste d'entrée: {int_list}")

        return tuple(int_list)

    def noduplicate(self, int_list: list[int] = []) -> list[int]:
        """Retourne la liste d'entiers passée en paramètre sans doublons.
        Note:
            L'utlisation du constructeur set(liste) modifie l'indexation des
            valeurs et trie les valeurs par ordre croissant.
            C'est pourquoi nous utilisons une solution un peu plus complexe.
            Infos ici: https://stackoverflow.com/a/17016257
        """
        # Génération d'une liste par défaut
        if len(int_list) == 0:
            int_list = self.genlist2()
            print(f"Liste d'entrée: {int_list}")

        return list(dict.fromkeys(int_list))

    def toset(self, a: list[int] = [], b: list[int] = []) -> bool:
        """Concatène les listes a et b, puis convertit le résultat en set.
        Retourne True si le set contient des valeurs, sinon False.
        Note:
            Nous avons choisi de générer des listes par défaut.
            Pour cela nous utilisons le if-else au début de notre méthode.
        """
        # Génération de listes par défaut
        if len(a) == 0:
            a = self.genlist2()
            print(f"Liste 1: {a}")

        if len(b) == 0:
            b = self.genlist2()
            print(f"Liste 1: {b}")

        # Concaténation de listes
        concatenated_list = a + b

        # Conversion en set
        set_conversion = set(concatenated_list)

        # Valeur de retour
        if len(set_conversion) < 1:
            return False

        return True

    def splitdict(self):
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
        studfail = dict()

        for key, value in stud.items():
            if value > 9:
                studpass[key] = value
            else:
                studfail[key] = value

        return studpass, studfail

    def gendict(self, dict_size: int = 3) -> dict:
        """Retourne un dictionnaire généré à l'aide d'inputs.
        Pour chaque paire de clé/valeur, demande à l'utilisateur d'insérer une
        clé et une valeur.
        """
        my_new_dict = dict()

        for i in range(dict_size):
            key = input("Veuillez introduire une clé: ")
            value = input("Veuillez introduire une valeur de type int: ")

            try:
                my_new_dict[key] = int(value)
            except ValueError:
                my_new_dict[key] = value

        return my_new_dict

    def alphabet(self):
        """Génère un dictionnaire de l'alphabet français.
        Ensuite crée une loop infinie demandant à l'utilisateur d'introduire
        un chiffre correspondant à une clé du dictionnaire.
        Si la clé est inconnue, renvoie un message par défaut.
        Si la clé demandée est 0, sortir de la loop.

        Notes:
            - Les lettres de l'alphabet se situent entre la valeur 65 (A) et
            122 (z).
            - Ceci comprend les majuscules et minuscules ainsi que quelques
            charactères spéciaux
            - Voir https://www.ascii-code.com/
        « valeur non disponible ».
        """
        alphabet_dict = dict()
        for i in range(65, 123):
            alphabet_dict[i] = chr(i)

        user_stop = False

        while user_stop is False:
            my_key = input("Veuillez introduire un nombre: ")

            if my_key == "0":
                user_stop = True

            else:
                try:
                    print(
                        f"    --> La valeur ASCII du nombre {my_key} est: "
                        f"{alphabet_dict[int(my_key)]}"
                    )
                except KeyError:
                    print("    --> La valeur demandée est non-disponible.")
