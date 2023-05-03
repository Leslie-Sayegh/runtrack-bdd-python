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
cur.execute("SELECT nom, capacite From salles")


res = cur.fetchall()

for nom, capacite in res:
    print(nom, capacite)

cur.close()

