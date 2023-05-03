import sqlite3

# Se connecter à la base de données ou la créer si elle n'existe pas
conn = sqlite3.connect('zoo.db')

# Créer la table "animal"
conn.execute('''CREATE TABLE IF NOT EXISTS animal
            (id INTEGER PRIMARY KEY,
             nom TEXT NOT NULL,
             race TEXT,
             cage_id INTEGER,
             date_naissance TEXT,
             pays_origine TEXT,
             FOREIGN KEY (cage_id) REFERENCES cage(id))''')

# Créer la table "cage"
conn.execute('''CREATE TABLE IF NOT EXISTS cage
            (id INTEGER PRIMARY KEY,
             superficie REAL,
             capacite_max INTEGER)''')

conn.commit()
conn.close()


def ajouter_animal(nom, race, cage_id, date_naissance, pays_origine):
    conn = sqlite3.connect('zoo.db')
    conn.execute(f"INSERT INTO animal(nom, race, cage_id, date_naissance, pays_origine) VALUES('{nom}', '{race}', {cage_id}, '{date_naissance}', '{pays_origine}')")
    conn.commit()
    conn.close()

def supprimer_animal(id):
    conn = sqlite3.connect('zoo.db')
    conn.execute(f"DELETE FROM animal WHERE id={id}")
    conn.commit()
    conn.close()

def modifier_animal(id, nom=None, race=None, cage_id=None, date_naissance=None, pays_origine=None):
    conn = sqlite3.connect('zoo.db')
    update_query = f"UPDATE animal SET "
    if nom:
        update_query += f"nom='{nom}', "
    if race:
        update_query += f"race='{race}', "
    if cage_id:
        update_query += f"cage_id={cage_id}, "
    if date_naissance:
        update_query += f"date_naissance='{date_naissance}', "
    if pays_origine:
        update_query += f"pays_origine='{pays_origine}', "
    # Supprimer la dernière virgule et l'espace inutiles
    update_query = update_query[:-2]
    update_query += f" WHERE id={id}"
    conn.execute(update_query)
    conn.commit()
    conn.close()

def ajouter_cage(superficie, capacite_max):
    conn = sqlite3.connect('zoo.db')
    conn.execute(f"INSERT INTO cage(superficie, capacite_max) VALUES({superficie}, {capacite_max})")
    conn.commit()
    conn.close()

def supprimer_cage(id):
    conn = sqlite3.connect('zoo.db')
    conn.execute(f"DELETE FROM cage WHERE id={id}")
    conn

def afficher_animaux():
    conn = sqlite3.connect('zoo.db')
    animaux = conn.execute("SELECT * FROM animal")
    for animal in animaux:
        print(animal)
    conn.close()

