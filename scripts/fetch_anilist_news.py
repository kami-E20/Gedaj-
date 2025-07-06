import requests

def fetch_anilist_news():
    query = """
    {
      Page(perPage: 1) {
        media(type: ANIME, sort: TRENDING_DESC) {
          title {
            romaji
          }
          description(asHtml: false)
          coverImage {
            large
          }
          siteUrl
        }
      }
    }
    """
    url = "https://graphql.anilist.co"
    response = requests.post(url, json={'query': query})
    data = response.json()
    if not data.get("data"):
        return None
    media = data["data"]["Page"]["media"][0]
    return {
        "titre": media["title"]["romaji"],
        "description": media["description"],
        "image": media["coverImage"]["large"],
        "lien": media["siteUrl"]
    }