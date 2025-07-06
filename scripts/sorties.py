import requests
from datetime import datetime, timedelta

def fetch_sorties_prochaines():
    target_date = datetime.now() + timedelta(days=7)
    month = target_date.month
    year = target_date.year

    query = f"""
    {{
      Page(perPage: 5) {{
        media(type: ANIME, sort: POPULARITY_DESC, seasonYear: {year}) {{
          title {{
            romaji
          }}
          startDate {{
            year
            month
            day
          }}
          description
          siteUrl
          coverImage {{
            large
          }}
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