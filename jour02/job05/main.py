# -*- coding: utf-8 -*-
import mysql.connector

#connexion au base de données
db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Siriana!06110",
  database = "laplateforme"

)

#créer un curseur de base de données pour effectuer des opérations SQL
cur = db.cursor()

#exécuter le curseur avec la méthode execute() et transmis la requête SQL
cur.execute("SELECT nom, superficie From etage")


res = cur.fetchall()

#initialiser la variable total_superficie à 0
total_superficie = 0

#itérer sur les tuples de la liste res pour calculer la superficie totale
for nom, superficie in res:
    total_superficie += superficie

print("La superficie totale est de", total_superficie)

#fermer le curseur et la connexion à la base de données
cur.close()