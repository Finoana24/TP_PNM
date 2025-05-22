def afficher_menu():
    print("Que souhaitez-vous boire ?")
    print("1. Café")
    print("2. Thé")
    print("3. Eau chaude")
    print("4. Quitter")

def traiter_choix(choix):
    if choix == "1":
        print("Vous avez choisi : Café.")
    elif choix == "2":
        print("Vous avez choisi : Thé.")
    elif choix == "3":
        print("Vous avez choisi : Eau chaude.")
    elif choix == "4":
        print("Au revoir !")
    else:
        print("Choix invalide, veuillez réessayer.")