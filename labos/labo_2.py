"""LAB0 2

1. Ecrire une fonction qui génère une liste comprenant des entier pseudo-aléatoire compris
entre a et b, et la retourne. Cette fonction prendre en paramètre a, b et la taille de la liste.
Cette fonction sera nommée :  genlist2()

2. Ecrire une fonction qui créé un tuple de nombres entiers générés à l’aide de la fonction
gennum () et qui le retourne. Cette fonction sera nommée :  gentuple()

3. Écrire une fonction qui reçoit en paramètre 1 liste d’entiers et la convertit en tuple.
Cette fonction sera nommée :  totuple()

4. Écrire une fonction qui reçoit en paramètre 1 listes d’entier et vérifie si elle contient des
doublons. Elle devra ensuite retourner une liste sans doublon.
Elle sera nommée :  noduplicate()

5. Écrire une fonction qui reçoit en paramètre 2 listes d’entier, les concatène et convertit la
résultante en set. Cette fonction retourne un booléen, true si le set contient des valeurs et
false si il est vide.
Elle sera nommée :  toset()

6. Écrire une fonction qui génère le dictionnaire suivant :

stud = {" stud 1" : 14 , " stud 2" : 13 , " stud 3" : 9 , " stud 4" : 12 ,
 " stud 5" : 3 , " stud 6" : 8 , " stud 7" : 16 , " stud 8" : 13 ,
" stud 9" : 13 , " stud 10" : 15 , " stud 11" : 14 , " stud 12" : 19 ,
" stud 13" : 10 , " stud 14" : 10 , " stud 15" : 13 , " stud 16" : 7 ,
" stud 17" : 12 , " stud 18" : 15 , " stud 19" : 9 , " stud 20" : 17 ,}

Cette fonction devra séparer ce dictionnaire en 2 dictionnaires nommé studpass dont les
valeurs sont supérieures ou égales à 10 et studfail dont les valeurs sont inférieures à 10.
Elle devra ensuite retourner les 2 dictionnaires.
Cette fonction sera nommée :  splitdict()

7. Écrire une fonction qui demande à l’utilisateur d’introduire un nombre et une lettre.
Elle affectera ces données dans un dictionnaire de sorte à ce que le nombre soit la clé et le
chiffre la valeur. La taille du dictionnaire est reçue en paramètre.
Cette fonction sera nommée :  gendict()

8. Écrire une fonction générant un dictionnaire contenant l’alphabet français.
La clé étant le valeur ASCII de la lettre et la valeur étant la lettre.
Exemple : {97 : "a",   98 : "b",   99 : "c",  ... }
Cette fonction devra ensuite demander d’introduire une clé pour afficher sa valeur.
Et cela jusqu’à ce que l’utilisateur n’a pas introduit 0.
Si l’utilisateur introduit une valeur inférieur ou supérieur aux clés disponibles, alors la
fonction devra afficher « valeur non disponible ».

9. Écrire une fonction principale (si ce n’est pas déjà fait) et appeler toutes les fonctions des
exercices précédents.
"""
