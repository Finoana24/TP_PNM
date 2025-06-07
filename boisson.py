def traiter_choix():
    print("Que voulez-vous boire ?")
    print("1 - Café")
    print("2 - Thé")
    print("3 - Eau chaude")
    print("4 - Quitter le menu")

def gerer_choix():
    commandes = []
    while True:
        traiter_choix()
        choix = input("Veuillez entrer le numéro de boisson:")
        if choix == "1":
            print("Vous avez choisi un café!")
            commandes.append("café")
        elif choix == "2":
            print("Vous avez choisi du thé!")
            commandes.append("thé")
        elif choix == "3":
            print("Vous avez choisi de l'eau chaude!")
            commandes.append("eau chaude")
        elif choix == "4":
            print("Vous avez quitté le menu!")
            break
        else:
            print("Votre choix est invalide, veuillez réessayer.")
    
    return commandes

# Programme principal
print("=== SYSTÈME DE COMMANDE DE BOISSONS ===")
commandes = gerer_choix()

print("\n--- Votre commande ---")
if commandes:
    compteur = {}
    pluriels = {
        "café": "cafés",
        "thé": "thés",
        "eau chaude": "eaux chaudes"
    }
    
    # Compter les boissons
    for boisson in commandes:
        compteur [boisson] = compteur.get(boisson, 0) + 1
    
    # Afficher le résumé
    for boisson, nombre in compteur.items():
        nom_boisson = boisson if nombre == 1 else pluriels.get(boisson, boisson + "s")
        print(f"{nombre} {nom_boisson}")
else:
    print("Aucune boisson commandée")

print("\nMerci pour votre commande!")
