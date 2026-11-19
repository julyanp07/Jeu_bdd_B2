#importer random
#depuis connexion importer la collection personnages et monstres

#definir le main
#   les options sont jouer et quitter
#   tant que infini
#       choix est egal a recuperer choix utilisateur
#       si le choix est 1
#           appeler demarrer jeu
#       si le choix est 2
#           break


#récuperer un choix valide parmi les options
#   tant que infini
#       afficher les options numerotées
#           pour chaque option dans enumerate(options, start=1)
#               afficher {i}. {option}
#       demander un choix a l'utilisateur
#       si le choix est valide
#           retourner le choix valide
#       afficher un message d'erreur


#choix_est_valide
#   si le choix n'est pas isdigit()
#       return False
#   convertir le choix en entier
#   si le choix est inférieur au minimum ou superieur au maximum
#       return False
#   return True


#def recuperer_choix_utilisateur
#   tant que infini
#       afficher_options_numerotees
#       entrer un choix ("Entrez votre choix :")
#       si choix_est_valide(choix, 1, len(options)):
#           retourner int(choix)
#       print("Choix invalide, réessayer")

#def afficher_options_numerotees 
#   pour chaque option dans enumerate(options, start=1)
#       print(f"{i}. {option}")



#def demarrer_jeu
#   initilaiser un pseudo a vide
#   tant que le pseudo est vide 
#       demander un pseudo
#       si le pseudo est vide
#       afficher message d'erreur
#   equipe est egal a choisir equipe dans la collection personnage
#   ennemi est egal a choisir ennemi au hasard dans la collection monstres
#   victoire est egal a lancer combat
#   si victoire
#       afficher victoire
#   sinon
#       afficher defaite


#besoin la liste des personnages
#   creer la variable equipe vide
#   tant que l'equipe n'est pas de 3
#       determiner la liste des personnages disponibles
#       construire la liste des options a afficher disponibles
#       recuperer choix utilisateur valide
#       ajouter le personnage choisi a l'equipe index

#determiner la liste des personnages disponibles, besoin de la liste de personnage et de equipe
#   initialiser la liste disponible
#   pour personnage dans liste de personnage
#       si personnage n'est pas dans equipe
#           ajouter le personnage dans disponible
#   retourner disponible

#construire options affichables, besoin de disponible
#   initialiser la liste option
#   pour chaque index.personnage dans enumerate (disponible, start=1)
#       ajouter le personnage a options
#   retourner options


#definir tour joueur
#   vivants est egal a lister vivants
#   construire les options
#   choix est recuperer choix utilisateur
#   attaquant est vivant choix - 1
#   attaquer

#definir tour ennemi
#   vivants est lister vivants
#   la cible est un personnage vivant au hasard dans l'equipe vivante
#   attaquer

#definir est vivant, a besoin de perso
#   retourner vrai si les pv si ils sont superieur a zero

#definir est equipe vivante, a besoin de equipe
#   pour chaque perso dans equipe
#       si est vivant
#           retourner vrai
#   retourner faux

#definir attaquer
#   les degats sont l'attaque de l'attaquant moins la defense du defenseur
#   si les degats sont inferieurs a 1
#       mettre 1 degat
#   retirer les degats au pv du defenseur
#   si les pv du defenseur sont inferieur a 0
#       mettre les pv a 0
#   si le defenseur est pas vivant
#   afficher mort

#definir lancer combat
#   tant que est equipe vivante(equipe) et est vivant(ennemi)
#       afficher les pv des deux equipes
#       appeler tour joueur
#       si l'ennemi n'est pas vivant
#           break
#       appeler tour_ennemi
#   retourner est equipe vivante

#definir lister vivants
#   initialiser la liste vivant a vide
#   pour chaque perso dans equipe
#       si est vivant
#           ajouter perso a vivants
#   retourner vivants

#appeler main