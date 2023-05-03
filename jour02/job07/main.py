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

# join tables and retrieve data
cur.execute("SELECT employes.nom, employes.prenom, services.nom FROM employes JOIN services ON employes.ID=services.ID")

# print result
for (nom, prenom, service) in cur:
  print(f"{nom} {prenom} travaille dans le service {service}")

# close connection
db.close()