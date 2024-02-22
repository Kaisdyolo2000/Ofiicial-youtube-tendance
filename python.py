# Fonction pour récupérer les vidéos YouTube les plus récentes et populaires par catégorie
def recuperer_videos_populaires_par_categorie(categorie):
    url = f"https://www.googleapis.com/youtube/v3/search?key={API_KEY}&part=snippet&order=date&type=video&videoCategoryId={categorie}&maxResults=5"
    response = requests.get(url)
    data = response.json()
    videos = []
    for item in data["items"]:
        titre = item["snippet"]["title"]
        lien = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        image = item["snippet"]["thumbnails"]["high"]["url"]
        videos.append({"titre": titre, "lien": lien, "image": image})
    return videos

# Fonction pour récupérer les vidéos par catégorie
def recuperer_videos_par_categorie():
    videos_par_categorie = {}
    for categorie, id_categorie in categories_youtube.items():
        videos = recuperer_videos_populaires_par_categorie(id_categorie)
        videos_par_categorie[categorie] = videos
    return videos_par_categorie