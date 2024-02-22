# Liste des catégories YouTube avec leurs identifiants
categories_youtube = {
    "Musique": "10",
    "Divertissement": "17",
    "humour":"7"
    "animaux":"5"
    "américain":"10"
    "français":"12"

# Gestion des tarifs pour les abonnements premium
TARIFS_PREMIUM = {
    "Basique": 3,
    "Avancé": 7,
    "Premium+": 12.99
}

# Durée d'expiration des abonnements premium+ (en jours)
EXPIRATION_PREMIUM_PLUS = 180  # 180 jours (6 mois)

# Fonction pour vérifier si l'utilisateur est un abonné premium
def est_abonne_premium():
    if 'premium_type' in session:
        return True
    return False