from optparse import OptionParser
import inspect


class Laboratoire:
    def __init__(self):
        while True:
            self.select_exercice()
            self.user_continue()

    def select_exercice(self):
        print("\nMéhodes disponibles:")
        methods = [
            i for i in inspect.getmembers(self, predicate=inspect.ismethod) if
            i[0] not in ["__init__", "select_exercice", "user_continue"]
        ]

        for i, value in enumerate(methods):
            print(f"    {i}. {value[0]}")

        chosen_exercice = input("\n\nQuel méthode souhaitez-vous exécuter ? - ")
        print("\n===== Exécution =====")
        exec(f'print(self.{methods[int(chosen_exercice)][0]}())')
        print("=====================")

    def user_continue(self):
        should_continue = input(
            "\n\nSouhaitez-vous exécuter une autre fonction ? [Y / n] ")
        if should_continue in ["n", "N", "no", "No", "NO", "non", "Non", "NON"]:
            quit()
