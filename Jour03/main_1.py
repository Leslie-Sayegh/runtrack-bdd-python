import mysql.connector

# Connectez-vous à la base de données
mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "Siriana!06110",
  database="boutique"
)

# Créez un curseur pour exécuter des requêtes SQL
mycursor = mydb.cursor()

# Exécutez une requête SELECT pour obtenir les noms des produits
mycursor.execute("SELECT nom FROM produit")

# Parcourez les résultats et affichez les noms des produits
for produit in mycursor:
  print(produit[0])
