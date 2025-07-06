import requests
from datetime import datetime, timedelta

def fetch_anime_sorties():
    target_date = datetime.now() + timedelta(days=7)
    query = f"""
    {{
      Page(perPage: 5) {{
        media(type: ANIME, sort: POPULARITY_DESC, seasonYear: {target_date.year}) {{
          title {{
            romaji
          }}
          startDate {{
            year
            month
            day
          }}
          description
          coverImage {{
            large
          }}
          siteUrl
        }}
      }}
    }}
    """
    response = requests.post("https://graphql.anilist.co", json={'query': query})
    data = response.json()
    results = []
    for media in data["data"]["Page"]["media"]:
        s = media["startDate"]
        if s["year"] == target_date.year and s["month"] == target_date.month and s["day"] == target_date.day:
            results.append({
                "titre": media["title"]["romaji"],
                "description": media.get("description", "Pas de description."),
                "image": media["coverImage"]["large"],
                "date": f"{s['day']:02}/{s['month']:02}/{s['year']}",
                "lien": media["siteUrl"]
            })
    return results