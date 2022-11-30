"""LABO 6

Élaboration d’un programme d'authentification.
Au démarrage, votre programme demandera à l'utilisateur d'insérer son nom
d'utilisateur ("login") ainsi que son mot de passe.
Il fera ensuite une vérification de ces données avec les données recueillies
dans le fichier .txt (base de données) où sera stocké toutes les données des
utilisateurs.
Le fichier .txt devra contenir dans l'ordre le login, le mot de passe, le nom,
le prénom et l'âge à chaque ligne du fichier et chaque élément séparé par une
virgule.
"""
import csv
from labos.labo_class import Laboratoire
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4).pprint
db_path = "bdd/bdd.txt"


def get_user_data():
	"""Receuille et retourne des données d'utilisateur.
	"""
	username = input("Nom d'utilisateur: ")
	password = input("Mot de passe: ")

	return username, password


def valid_credentials(path_to_db: str, user_credentials: dict):
	"""Ouvre une BDD et compare les données d'autentification de l'utilisateur
	avec le contenu de la BDD. Si les données d'autentifications sont corectes
	retourne True, sinon False
	"""

	# ouvre la BDD en mode "csv" pour facilement séparer les éléments
	with open(path_to_db) as db:
		csv_reader = csv.reader(db)

		for row in csv_reader:
			if (
				row[0] == user_credentials['username'] and
				row[1] == user_credentials['password']
			):
				return True

	return False


def get_data_from_db(path_to_db: str, username: str):
	"""Ouvre un BDD et cherche l'utilisateur avec le nom username.
	Retourne les données de l'utilisateur.
	"""
	with open(path_to_db) as db:
		csv_reader = csv.reader(db)

		for row in csv_reader:
			if row[0] == username:
				return {
					'username': row[0],
					'name': row[2],
					'firstname': row[3],
					'age': row[4]
				}


class Labo_6(Laboratoire):
	def login(self):
		username, password = get_user_data()
		is_valid_credentials = valid_credentials(
			path_to_db=db_path,
			user_credentials={
				'username': username,
				'password': password
			}
		)

		if is_valid_credentials:
			user = get_data_from_db(
				path_to_db="bdd/bdd.txt",
				username=username
			)
			return f"\n--> Bienvenue, {user['name']} {user['firstname']}"
		else:
			return "\n--> Erreur d'authentification."

	def write_db(self, path_to_db=db_path, mode="w"):
		"""Ecriture d'un fichier "BDD".
		Retourne True si le fichier s'est correctement écrit.
		"""
		users = [
			{
				'username': 'login1',
				'password': 'pass1234',
				'last_name': 'Doe',
				'first_name': 'John',
				'age': 35,
			},
			{
				'username': 'login2',
				'password': 'pass7894',
				'last_name': 'Blah',
				'first_name': 'Jane',
				'age': 30,
			}
		]

		try:
			with open(path_to_db, mode) as file:
				writer = csv.writer(file)
				for i in users:
					values = [value for value in i.values()]
					writer.writerow(values)

			return True
		except Exception as e:
			print(str(e))
			return False