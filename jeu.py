#def main

#afficher menu



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
#       print(f"{1}. {option}")


#si choix est 1
#   demarrer_jeu
#
#si choix est 2
#   afficher_classement
#
#si choix est 3
#   break


#def demarrer_jeu
#   initilaiser un pseudo a vide
#   tant que le pseudo est vide 
#       demander un pseudo
#       si le pseudo est vide
#       afficher message d'erreur
#       choisir_equipe


#def choisir_equipe
#   recuperer les persos de la db
#   initialiser une equipe vide
#   tant que l'equipe a moins de 3 persos
#       afficher l'equipe de l'utilisateur
#       pour chaque perso dans equipe
#           afficher le nom du perso
#       afficher les persos disponibles
#       disponible = perso pas dans equipe
#       options = chaque perso disponible
#           afficher les noms pv atk def
#       choix = recuperer_choix_utilisateur(options)
#       ajouter choix a l'equipe
#   retourner l'equipe


#def est_vivant
#   retourner pv du perso si superieur a 0

#def est_equipe_vivante
#   retourner les persos vivants a l'equipe


#def tour_joueur
#   attaquant egal perso vivant au hasard dans equipe vivante
#   la cible est l'ennemi vivant
#   attaquer

#def tour_enemi
#   l'attaquant est l'ennemi
#   la cible est un perso vivant au hasard de equipe vivante
#   attaquer




#besoin la liste des personnages
#   creer la variable equipe vide
#   tant que l'equipe n'est pas complete
#       determiner la liste des personnages disponibles
#       construire la liste des options a afficher disponibles
#       recuperer choix utilisateur valide
#       ajouter le personnage choisi a l'equipe index

#determiner la liste des personnages disponibles
#   initialiser la liste disponible
#   pour personnage dans liste de personnage
#       si personnage n'est pas dans equipe
#           ajouter le personnage dans disponible
#   retourner disponible

#construire options affichables, besoin de disponible
#   initialiser la liste option
#   pour chaque personnage dans enumerate (disponible, start=1)
#       ajouter le personnage a options
#   retourner options