#region Fonctions
def DeuxDerniersChiffresAnnee(annee) :  #Récupère les deux derniers chiffres de l'année
    return int(str(annee)[-3:])

def selonMois(mois) :  #Selon le mois, retourne la valeur
    if mois == 1 :
        return 0
    elif mois == 2 :
        return 3
    elif mois == 3 :
        return 3
    elif mois == 4 :
        return  6
    elif mois == 5 :
        return  1
    elif mois == 6 :
        return 4
    elif mois == 7 :
        return 6
    elif mois == 8 :
        return 2
    elif mois == 9 :
        return 5
    elif mois == 10 :
        return 0
    elif mois == 11 :
        return 3
    elif mois == 12 :
        return 5

def Bissextile(annee) :  #Vérifie si l'année donnée est bissextile ou non
    bissextile = False
    if annee % 400 == 0 :
        bissextile = True
    elif annee % 100 == 0 :
        bissextile = False
    elif annee % 4 == 0 :
        bissextile = True
    return bissextile

def ValeurSiecle(annee) :  #Récupère les deux premiers chiffres du siècle
    if int(str(annee)[:2]) == 16 :
        return 6
    elif int(str(annee)[:2]) == 17 :
        return 4
    elif int(str(annee)[:2]) == 18 :
        return 2
    elif int(str(annee)[:2]) == 19 :
        return 0
    elif int(str(annee)[:2]) == 20 :
        return 6
    elif int(str(annee)[:2]) == 21 :
        return 4

def JourFonction(reste) :  #Indique à quel jour correspond le reste dans le traitement
    if reste == 0 :
        return "Dimanche"
    elif reste == 1 :
        return "Lundi"
    elif reste == 2 :
        return "Mardi"
    elif reste == 3 :
        return "Mercredi"
    elif reste == 4 :
        return "Jeudi"
    elif reste == 5 :
        return "Vendredi"
    elif reste == 6 :
        return "Samedi"
#endregion

#region Programme : savoir le jour de la semaine pour une date donnée dans le calendrier grégorien.
date = input("Saisissez une date au format : JJ/MM/AAAA") #Demande à l'utilisateur de saisir une date

if "/" in date : #Vérifie si la date est au bon format(vérifie seulement si au moins un / est compris dans la saisie, donc pas sûr à 100% que la date soit au bon format...
    jour, mois, annee = date.split("/")
else :
    date = input("La date n'est pas valide : entrez une date respectant le format JJ/MM/AAAA")#Redemande à l'utilisateur de saisir une date si sa saisie était erronée
    jour, mois, annee = date.split("/")

jour = int(jour) #Conversion du jour de la date saisie en int
mois = int(mois) #Conversion du mois de la date saisie en int
annee = int(annee) #Conversion de l'année de la date saisie en int

if annee == 1582 : #Si l'année est 1582,
    if mois <= 10 : #on vérifie que le mois n'est pas antérieur à Novembre, sinon on affiche un message d'erreur
        print("La date doit être comprise entre le 1 Novembre 1582 et + l'infini")

elif annee < 1582 : #On vérifie que l'année n'est pas antérieur à 1582, sinon on affiche un message d'erreur
        print("La date doit être comprise entre le 1 Novembre 1582 et + l'infini")

else : #Si la date est conforme
    deuxChiffresAnnee = DeuxDerniersChiffresAnnee(annee) #On récupère les deux derniers chiffres de l'année
    quartNombre = deuxChiffresAnnee // 4 #On divise le nombre formé par ces 2 chiffres par 4 sans prendre en compte le reste
    deuxChiffresAnnee = deuxChiffresAnnee + quartNombre #On ajoute à ce nombre le résultat de la division par 4 sans prendre en compte le reste
    deuxChiffresAnnee = deuxChiffresAnnee + jour #On additionne ce nombre et le jour
    ajoutMois = selonMois(mois) #On récupère la valeur via la fonction selonMois
    deuxChiffresAnnee = deuxChiffresAnnee + ajoutMois #On additionne le nombre avec la valeur récupérée via la fonction selonMois
    if Bissextile(annee) and mois <= 2 : #Si l'année est bissextile et le mois est janvier ou février,
        deuxChiffresAnnee = deuxChiffresAnnee - 1 #on soustrait 1 au nombre
    valeur = ValeurSiecle(annee) #On récupère la valeur correspondant aux deux premiers chiffres de l'année
    deuxChiffresAnnee = deuxChiffresAnnee + valeur #On additionne au nombre la valeur correspondante
    reste = deuxChiffresAnnee % 7 #On divise la somme par 7 et on garde le reste

    resultat = JourFonction(reste) #On convertit le reste en jour de la semaine via la fonction JourFonction
    print("Le jour correspondant au", date, "est", resultat) #On affiche le jour en toutes lettres correspondant à la date saisie par l'utilisateur
#endregion