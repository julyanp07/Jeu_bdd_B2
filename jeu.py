#importer random
import random
#depuis db_init importer la collection personnages et monstres
from db_init import collection_personnages, collection_monstres

#definir le main
def main():
#   les options sont jouer et quitter
    options = ["Jouer", "Quitter"]
#   tant que infini
    while True:
#       choix est egal a recuperer choix utilisateur
        choix = recuperer_choix_utilisateur(options)
#       si le choix est 1
        if choix == 1:
#           appeler demarrer jeu
            demarrer_jeu()
#       si le choix est 2
        if choix == 2:
#           break
            break


#récuperer un choix valide parmi les options
def recuperer_choix_valide(options):
#   tant que infini
    while True:
#       afficher les options numerotées
#           pour chaque option dans enumerate(options, start=1)
        for i, option in enumerate(options, start=1):
#               afficher {i}. {option}
            print(f"{i}. {option}")
#       demander un choix a l'utilisateur
        choix = input("Entrez votre choix :")
#       si le choix est valide
        if choix_est_valide(choix, 1, len(options)):
#           retourner le choix valide
            return int(choix)
#       afficher un message d'erreur
        print("Choix invalide, réessayez")


#choix_est_valide
def choix_est_valide(choix, minimum, maximum):
#   si le choix n'est pas isdigit()
    if not choix.isdigit():
#       return False
        return False
#   convertir le choix en entier
    choix = int(choix)
#   si le choix est inférieur au minimum ou superieur au maximum
    if choix < minimum or choix > maximum:
#       return False
        return False
#   return True
    return True


#def recuperer_choix_utilisateur
def recuperer_choix_utilisateur(options):
#   tant que infini
    while True:
#       afficher_options_numerotees
        afficher_options_numerotees(options)
#       entrer un choix ("Entrez votre choix :")
        choix = input("Entrez votre choix :")
#       si choix_est_valide(choix, 1, len(options)):
        if choix_est_valide(choix, 1, len(options)):
#           retourner int(choix)
            return int(choix)
#       print("Choix invalide, réessayer")
        print("Choix invalide, réessayez")

#def afficher_options_numerotees
def afficher_options_numerotees(options):
#   pour chaque option dans enumerate(options, start=1)
    for i, option in enumerate(options, start=1):
#       print(f"{i}. {option}")
        print(f"{i}. {option}")



#def demarrer_jeu
def demarrer_jeu():
#   initilaiser un pseudo a vide
    pseudo = ""
#   tant que le pseudo est vide 
    while pseudo == "":
#       demander un pseudo
        pseudo = input("Entrez votre pseudo :")
#       si le pseudo est vide
        if pseudo == "":
#           afficher message d'erreur
            print("Le pseudo ne peut pas etre vide")
#   equipe est egal a choisir equipe dans la collection personnage
    equipe = choisir_equipe(list(collection_personnages.find()))
#   ennemi est egal a choisir ennemi au hasard dans la collection monstres
    ennemi = random.choice(list(collection_monstres.find()))
#   victoire est egal a lancer combat
    victoire = lancer_combat(equipe, ennemi) 
#   si victoire
    if victoire:
#       afficher victoire
        print(f"Victoire")
#   sinon
    else:
#       afficher defaite
        print(f"Défaite")


#besoin la liste des personnages
def choisir_equipe(liste_personnages):
#   creer la variable equipe vide
    equipe = []
#   tant que l'equipe n'est pas de 3
    while len(equipe) < 3:
#       determiner la liste des personnages disponibles
        disponibles = determiner_disponibles(liste_personnages, equipe)
#       construire la liste des options a afficher disponibles
        options = construire_options(disponibles)
#       recuperer choix utilisateur valide
        choix = recuperer_choix_valide(options)
#       ajouter le personnage choisi a l'equipe index
        equipe.append(disponibles[choix - 1])
    return equipe

#determiner la liste des personnages disponibles, besoin de la liste de personnage et de equipe
def determiner_disponibles(liste_personnages, equipe):
#   initialiser la liste disponible
    disponible = []
#   pour personnage dans liste de personnage
    for personnage in liste_personnages:
#       si personnage n'est pas dans equipe
        if personnage not in equipe:
#           ajouter le personnage dans disponible
            disponible.append(personnage)
#   retourner disponible
    return disponible

#construire options affichables, besoin de disponible
def construire_options(disponible):
#   initialiser la liste option
    options = []
#   pour chaque index.personnage dans enumerate (disponible, start=1)
    for index, personnage in enumerate(disponible, start=1):
#       ajouter le personnage a options
        options.append(f"{personnage['NOM']} (PV {personnage['PV']}, ATK {personnage['ATK']}, DEF{personnage['DEF']})")
#   retourner options
    return options


#definir tour joueur
def tour_joueur(equipe, ennemi):
#   vivants est egal a lister vivants
    vivants = lister_vivants(equipe)
#   construire les options
    options = construire_options(vivants)
#   choix est recuperer choix utilisateur
    choix = recuperer_choix_utilisateur(options)
#   attaquant est vivant choix - 1
    attaquant = vivants[choix - 1]
#   attaquer
    attaquer(attaquant, ennemi)

#definir tour ennemi
def tour_ennemi(equipe, ennemi):
#   vivants est lister vivants
    vivants = lister_vivants(equipe)
#   la cible est un personnage vivant au hasard dans l'equipe vivante
    cible = random.choice(vivants)
#   attaquer
    attaquer(ennemi, cible)

#definir est vivant, a besoin de perso
def est_vivant(personnage):
#   retourner vrai si les pv si ils sont superieur a zero
    return personnage["PV"] > 0

#definir est equipe vivante, a besoin de equipe
def est_equipe_vivante(equipe):
#   pour chaque perso dans equipe
    for personnage in equipe:
#       si est vivant
        if est_vivant(personnage):
#           retourner vrai
            return True
#   retourner faux
    return False

#definir attaquer
def attaquer(attaquant, defenseur):
#   les degats sont l'attaque de l'attaquant moins la defense du defenseur
    degats = attaquant["ATK"] - defenseur["DEF"]
#   si les degats sont inferieurs a 1
    if degats < 1:
#       mettre 1 degat
        degats = 1
#   retirer les degats au pv du defenseur
    defenseur["PV"] -= degats
#   si les pv du defenseur sont inferieur a 0
    if defenseur["PV"] < 0:
#       mettre les pv a 0
        defenseur["PV"] = 0
#   si le defenseur est pas vivant
    if not est_vivant(defenseur):
#       afficher mort
        print(f"{defenseur['NOM']} est mort")

#definir lancer combat
def lancer_combat(equipe, ennemi):
#   tant que est equipe vivante(equipe) et est vivant(ennemi)
    while est_equipe_vivante(equipe) and est_vivant(ennemi):
#       afficher les pv des deux equipes
        for personnage in equipe:
            print(f"{personnage['NOM']} : {personnage['PV']} PV")
#       appeler tour joueur
        tour_joueur(equipe, ennemi)
#       si l'ennemi n'est pas vivant
        if not est_vivant(ennemi):
#           break
            break
#       appeler tour_ennemi
        tour_ennemi(equipe, ennemi)
#   retourner est equipe vivante
    return est_equipe_vivante(equipe)

#definir lister vivants
def lister_vivants(equipe):
#   initialiser la liste vivant a vide
    vivants = []
#   pour chaque perso dans equipe
    for personnage in equipe:
#       si est vivant
        if est_vivant(personnage):
#           ajouter perso a vivants
            vivants.append(personnage)
#   retourner vivants
    return vivants

#appeler main
main()