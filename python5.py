# Planification de l'exécution de la fonction pour changer les données des vidéos toutes les deux semaines
schedule.every(2).weeks.do(changer_donnees_videos)

# Planification de l'exécution de la fonction pour changer les images pendant les fêtes (par exemple, chaque mois)
schedule.every().month.do(changer_images_pendant_les_fetes)

# Planification de l'exécution de la fonction pour annuler l'abonnement premium+ chaque mois
schedule.every().month.do(annuler_abonnement_premium_plus)

# Boucle pour exécuter les planifications en arrière-plan
while True:
    schedule.run_pending()
    time.sleep(1)

# Point d'entrée de l'application Flask
if __name__ == '__main__':
    app.run(debug=True)