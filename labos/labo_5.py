"""LABO 1

NOTE:
-----
Nous ne créons pas de paramètres par défaut car, comme nous sommes au sein
d'une classe, il faut d'abord appeler l'objet self (équivalent à 'this' dans
d'autres languages) pour pouvoir avoir accès aux méthodes de classe.
Du coup, on ne peux définir une fonction avec des paramètres correspondant à
l'appel d'une fonction de classe.

Nomenclature:
File = Queue
Pile = Stack

ENONCE DU LABO:
---------------
1. Sur base de la liste suivante : ["tata","toto","titi","tete","tutu","tyty"]
    a. Écrire une fonction qui prend en paramètre un mot et une pile et qui
    l’insère à l’intérieur de celle-ci. 
    b. Écrire une fonction prenant en paramètre une pile et qui la copie et
    retourne sa copie. 
    c. Écrire une fonction prenant en paramètre une pile et qui retourne la
    pile inversée. 
    d. Écrire une fonction qui retourne le dernier élément la pile insérée en
    paramètre. 
    e. Écrire une fonction qui prend en paramètre une pile, un mot et un
    nombre et qui insère ce mot dans la pile à l’emplacement à quoi correspond
    ce nombre. 
    f. Écrire une fonction qui prend en paramètre une pile et un nombre et qui
    supprime l’élément correspondant à l’emplacement du nombre. 
    g. Écrire une fonction qui prend en paramètre une pile et un mot et qui
    supprime l’élément correspondant au mot. 
    h. Faire un schéma de la mémoire pour les exercices a, b, c, d, e et f. 
 
 
2. Sur base de la liste suivante : ["tata","toto","titi","tete","tutu","tyty"]
    a. Écrire une fonction qui prend en paramètre un mot et une file et qui
    l’insère à l’intérieur de celle-ci. 
    b. Écrire une fonction prenant en paramètre une file et qui la copie et
    retourne sa copie. 
    c. Écrire une fonction qui retourne le premier élément la file insérée en
    paramètre. 
    d. Écrire une fonction qui prend en paramètre une file, un mot et un
    nombre et qui insère ce mot dans la file à l’emplacement à quoi correspond
    ce nombre. 
    e. Écrire une fonction qui prend en paramètre une file et un nombre et qui
    supprime l’élément correspondant à l’emplacement du nombre. 
    f. Écrire une fonction qui prend en paramètre une file et un mot et qui
    supprime l’élément correspondant au mot. 
    g. Faire un schéma de la mémoire pour les exercices a, b, c, d et e. 
"""

from labos.labo_class import Laboratoire
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4).pprint


class Pile():
    """Une Pile ou 'stack' en anglais ressemble à une liste mais à la
    particuarité de fonctionner en LIFO. En d'autre termes, le dernier
    élémént à être ajouté à la liste sera le premier élément à être
    traité.

    - append:   
    - copy: puisqu'une pile est LIFO, le dernier élément devient le premier
            élément de la copie.
    """
    def __init__(self):
        self.values = []
        # methodes de liste
        # 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

    def push(self, element):
        """Ajoute un élément à en haut de la pile (dernier élément) ceci ne
        change pas du comportement d'une liste
        """
        self.values.append(element)


    def copy(self):
        """Copie une pile et retourne la copie
        """
        return self.values.copy()

    def reverse(self):
        """Retourne la pile et la retourne la pile inversée.
        """
        # On travaille sur une copie pour ne pas altérer l'original
        stack_copy = self.values.copy()
        stack_copy.reverse()
        return stack_copy

    def pop(self, index=-1):
        """Supprime un élément de la pile. Par défaut, il s'agit du dernier
        élément de la pile.
        Lorsqu'un indice (index) est passé en argument, c'est l'élément à
        l'indice donné qui sera supprimé.
        """
        self.values.pop(index)
        return self.values

    def insert(self, element, index):
        """Insère un élément à la pile à l'index donné.
        """
        self.values.insert(index, element)
        return self.values


def create_my_stack():
    stack = Pile()
    ma_pile = ["tata","toto","titi","tete","tutu","tyty"]

    for i in ma_pile:
        stack.push(i)

    return stack


class Labo_5(Laboratoire):
    def push_to_stack(self, mot="exemple", pile=create_my_stack()):
        """fonction qui prend en paramètre un mot et une pile et qui
        l’insère à l’intérieur de celle-ci.
        """
        pp(f"Pile initiale: {pile.values}")
        pp("Résultat:")
        pile.push(mot)
        return pile.values

    def copy_stack(self, pile=create_my_stack()):
        """fonction prenant en paramètre une pile et qui la copie et
        retourne sa copie.
        """
        pp(f"Pile initiale: {pile.values}")
        pp("Résultat:")
        return pile.copy()

    def reverse_stack(self, pile=create_my_stack()):
        """fonction prenant en paramètre une pile et qui retourne la
        pile inversée.
        """
        pp(f"Pile initiale: {pile.values}")
        pp("Résultat:")
        return pile.reverse()

    def pop_stack(self, pile=create_my_stack()):
        """fonction qui retourne le dernier élément la pile insérée en
        paramètre.
        """
        pp(f"Pile initiale: {pile.values}")
        pp("Résultat:")
        return pile.pop()

    def insert_at_index(self, mot="insertion", index=3, pile=create_my_stack()):
        """fonction qui prend en paramètre une pile, un mot et un
        nombre et qui insère ce mot dans la pile à l’emplacement à quoi
        correspond ce nombre
        """
        pp(f"Pile initiale: {pile.values}")
        pp("Résultat:")
        return pile.insert(mot, index)

    def pop_by_index(self, index=3, pile=create_my_stack()):
        """fonction qui prend en paramètre une pile et un nombre et qui
        supprime l’élément correspondant à l’emplacement du nombre. 
        """
        pp(f"Pile initiale: {pile.values}")
        pp("Résultat:")
        return pile.pop(index)


    def pop_by_value(self, mot="tutu", pile=create_my_stack()):
        """fonction qui prend en paramètre une pile et un mot et qui
        supprime l’élément correspondant au mot
        """
        pp(f"Pile initiale: {pile.values}")
        pp("Résultat:")
        try:
            index = pile.values.index(mot)
        except ValueError:
            return f"Le mot {mot} ne se trouve pas dans la pile."

        return pile.pop(index)

    def memory_schema(self):
        """un schéma de la mémoire pour les exercices a, b, c, d, e et f.
        """
        return
