def mergeSort(array_to_sort: list) -> list:
    """Méthode d'aide pour la méthode fusionSort() du labo 3.
    Cette méthode est la logique du tri par fusion.
    """
    # Subdivision de la liste en 2 jusqu'à obtenir des liste de longueur 1
    if len(array_to_sort) > 1:
        middle = len(array_to_sort) // 2  # point médian de la liste
        sub_left = array_to_sort[:middle]
        sub_right = array_to_sort[middle:]

        # Répéter le processus - récursivité jusqu'à l'unité
        mergeSort(sub_left)
        mergeSort(sub_right)

        # Réassembler les listes (fusion)
        i = j = k = 0

        while i < len(sub_left) and j < len(sub_right):
            # Si le pointeur de gauche désigne une valeur inférieure au
            # pointeur de droite, utiliser la valeur désignée par le
            # pointeur de gauche et incrémenté l'index du pointeur gauche.
            if sub_left[i] < sub_right[j]:
                array_to_sort[k] = sub_left[i]
                i += 1

            # Sinon, utiliser la valeur désignée par le pointeur de droite
            # et incrémenter l'index du pointeur de droite.
            else:
                array_to_sort[k] = sub_right[j]
                j += 1

            # Incrémenter le pointeur de la liste principale.
            k += 1

        # S'assurer que tous les éléments aient bien été utilisés.
        while i < len(sub_left):
            array_to_sort[k] = sub_left[i]
            i += 1
            k += 1

        while j < len(sub_right):
            array_to_sort[k] = sub_right[j]
            j += 1
            k += 1

    return array_to_sort
