from boisson import afficher_menu, traiter_choix

def main():
    commandes = []

    while True:
        afficher_menu()
        saisie = input("Entrez vos choix (ex : 1 2 1) ou 4 pour quitter : ")
        choix_liste = saisie.strip().split()

        quitter = False

        for choix in choix_liste:
            boisson = traiter_choix(choix)

            if boisson == "Quitter":
                quitter = True
                break
            else:
                boisson
                commandes.append(boisson)
                print(f"→ {boisson} ajouté à votre commande.")
           
           
           
    if commandes:
        print("\nVoici votre commande finale :")
        for index, item in enumerate(commandes, start=1):
            print(f"{index}. {item}")
    else:
        print("\nAucune boisson commandée.")

    print("Merci et à bientôt ! 👋")

if __name__ == "__main__":
    main()