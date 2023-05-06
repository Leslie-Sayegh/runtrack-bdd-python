import mysql.connector

import tkinter
from tkinter import *
from tkinter import messagebox 

#creer objet = creer pt fenetre 
window = Tk()
#titre fenetre
window.title("Tic-Tac-Toe")
# Fonction pour afficher la liste des produits
def afficher_produits():
    mycursor.execute("SELECT * FROM produit")
    produits = mycursor.fetchall()
    for i, produit in enumerate(produits):
        for j, champ in enumerate(produit):
            champ_label = Label(tableau_bord, text=str(champ))
            champ_label.grid(row=i+1, column=j)
 
# Fonction pour ajouter un produit
def ajouter_produit():
    # Code pour ajouter un produit dans la base de données
    # Après l'ajout, appeler la fonction afficher_produits() pour mettre à jour le tableau
 
# Fonction pour supprimer un produit
    def supprimer_produit():
    # Code pour supprimer un produit de la base de données
    # Après la suppression, appeler la fonction afficher_produits() pour mettre à jour le tableau
 
# Fonction pour modifier un produit
        def modifier_produit():
    # Code pour modifier un produit dans la base de données
    # Après la modification, appeler la fonction afficher_produits() pour mettre à jour le tableau

# Connectez-vous à la base de données
            mydb = mysql.connector.connect(
            host="localhost",
            user="votre_nom_d'utilisateur",
            password="Siriana!06110",
            database="boutique"
)

# Créez un curseur pour exécuter des requêtes SQL
            mycursor = mydb.cursor()

# Créez une fenêtre Tkinter pour le tableau de bord
tableau_bord = Tk()
tableau_bord.title("Tableau de bord de gestion des stocks")

# Ajoutez des boutons pour ajouter, supprimer et modifier les produits
ajouter_bouton = Button(tableau_bord, text="Ajouter un produit", command=ajouter_produit)
ajouter_bouton.grid(row=0, column=0)
supprimer_bouton = Button(tableau_bord, text="Supprimer un produit", command=supprimer_produit)
supprimer_bouton.grid(row=0, column=1)
modifier_bouton = Button(tableau_bord, text="Modifier un produit", command=modifier_produit)
modifier_bouton.grid(row=0, column=2)

# Ajoutez une étiquette pour les noms de colonnes
id_label = Label(tableau_bord, text="ID")
id_label.grid(row=1, column=0)
nom_label = Label(tableau_bord, text="Nom")
nom_label.grid(row=1, column=1)
description_label = Label(tableau_bord, text="Description")
description_label.grid(row=1, column=2)
prix_label = Label(tableau_bord, text="Prix")
prix_label.grid(row=1, column=3)
quantite_label = Label(tableau_bord, text="Quantité")
quantite_label.grid(row=1, column=4)
categorie_label = Label(tableau_bord, text="Catégorie")
categorie_label.grid(row=1, column=5)

# Affichez la liste complète des produits
afficher_produits()

# Lancez la boucle principale de Tkinter
tableau_bord.mainloop()
