#!/usr/bin/env python3

import sys 


def create_dataclients(data_client):
	""" On stocke les données de tous les clients dans une liste 'clients' 

	Args:
		data_client: une chaîne de caractères, le nom du fichier du dataset des clients.
	Returns:
		clients: une liste de liste (chaque élément représentera les données d'un client)
	"""

	clients = []
	
	for line in open(data_client, 'r').readlines():
		fields = line.split(',')
		clients.append(fields)
	
	return clients


def create_dataproducts(data_product):
	""" On stocke les données de tous les produits dans une liste 'produits' 

	Args:
		data_product: une chaîne de caractères, le nom du fichier du dataset des produits.
	Returns:
		products: une liste de liste (chaque élément représentera les données d'un produit)
	"""

	products = []

	for line in open(data_product, 'r').readlines():
		fields = line.split(',')
		products.append(fields)

	return products


def pourcentage(x, y):
	""" Pour un nombre x / y, on retourne l'equivalent sur 100

	Args:
		x: un entier
		y: un entier
	Returns:
		float
	"""
	return float(100 * x / y)


def statistique(data_client, data_product):
	""" Pour chaque produit, on affiche les genres du client qui aiment le plus le produit en question 
	avec son pourcentage par rapport à tous les clients.

	Args:
		data_client: une chaîne de caractères, le nom du fichier du dataset des clients.
		data_product: une chaîne de caractères, le nom du fichier du dataset des produits.
	Returns:
		Ne retourne rien.
	"""

	# les clients représentés dans une liste de liste:
	clients = create_dataclients(data_client)

	# les produits représentés dans une liste de liste:
	products = create_dataproducts(data_product)

	i=0

	# Pour chaque produit, on comptera nombre total de: femmes, d'hommes, de cadres et de non-cadres
	for line in open(data_product, 'r').readlines():
		fields = line.split(',')

		nb_femme = 0
		nb_homme = 0
		nb_cadre = 0
		nb_non_cadre = 0
		nbcli = 0

		for cli in fields[2:]:
			if clients[int(cli)][0] == 'F':
				nb_femme = nb_femme + 1

			else:
				nb_homme = nb_homme + 1
			
			if clients[int(cli)][1] == 'cadre':
				nb_cadre = nb_cadre + 1

			else:
				nb_non_cadre = nb_non_cadre + 1

			nbcli = nbcli + 1


		genre = 'femme'

		if nb_homme > nb_femme:
			genre = 'homme'

		status = 'cadre'
		if nb_non_cadre > nb_cadre:
			status = 'non cadre'

		print('product ' + str(i) + ': ' + genre + ' ' + status + " : " + str(pourcentage(nbcli, len(clients))) + '%')
		i = i + 1
	

def main():
	statistique('dataset_client', 'dataset_product')


if __name__ == "__main__":
    main()


