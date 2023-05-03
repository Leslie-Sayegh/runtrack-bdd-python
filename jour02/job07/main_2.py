import mysql.connector

class Salariee:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cur = self.db.cursor()

    def __del__(self):
        self.db.close()

    def create(self, nom, prenom, service):
        query = "INSERT INTO employes (nom, prenom, service) VALUES (%s, %s, %s)"
        values = (nom, prenom, service)
        self.cur.execute(query, values)
        self.db.commit()
        print(f"Le salarié {nom} {prenom} a été ajouté avec succès dans la base de données.")

    def read(self):
        self.cur.execute("SELECT * FROM employés")
        result = self.cur.fetchall()
        for row in result:
            print(row)

    def update(self, salariee_id, nom=None, prenom=None, service=None):
        query = "UPDATE employes SET"
        if nom:
            query += f" nom='{nom}',"
        if prenom:
            query += f" prenom='{prenom}',"
        if service:
            query += f" services='{service}',"
        query = query[:-1]  # remove trailing comma
        query += f" WHERE id={salariee_id}"
        self.cur.execute(query)
        self.db.commit()
        print(f"Le salarié avec l'ID {salariee_id} a été modifié avec succès dans la base de données.")

    def delete(self, salariee_id):
        query = f"DELETE FROM salariée WHERE id={salariee_id}"
        self.cur.execute(query)
        self.db.commit()
        print(f"Le salarié avec l'ID {salariee_id} a été supprimé avec succès de la base de données.")

# Création d'un objet Salariee avec les informations de connexion à la base de données
salariee = Salariee("localhost", "root", "Siriana!06110", "laplateforme")

# Création d'un nouveau salarié
salariee.create("Chossis", "Siriana", "Technique")

# Affichage de tous les salariés
salariee.read()

# Modification d'un salarié existant
salariee.update(3, nom="Chateau-Dos Santos", prenom="Julie")

# Suppression d'un salarié existant
#salariee.delete(2)