from telebot.types import Message
from datetime import datetime

def register_prochainfilm(bot):
    @bot.message_handler(commands=['prochainfilm'])
    def handle_prochainfilm(message: Message):
        sorties = get_prochaines_sorties()
        reponse = "🎥 **Prochaines sorties cinéma, séries & animés** 📆\n\n"

        for i, item in enumerate(sorties, 1):
            reponse += f"{i}. *{item['titre']}* — {item['date']} ({item['plateforme']})\n"

        bot.send_message(message.chat.id, reponse, parse_mode="Markdown")

def get_prochaines_sorties():
    return [
        {"titre": "Dune : Deuxième Partie", "date": "08 août 2025", "plateforme": "Cinéma"},
        {"titre": "Avatar : Le Portail", "date": "15 août 2025", "plateforme": "Cinéma"},
        {"titre": "One Piece Live Action – Saison 2", "date": "20 août 2025", "plateforme": "Netflix"},
        {"titre": "Jujutsu Kaisen : Film 2", "date": "22 août 2025", "plateforme": "Crunchyroll"},
        {"titre": "Spider-Man Beyond", "date": "30 août 2025", "plateforme": "Cinéma"},
        {"titre": "The Boys – Saison 5", "date": "02 septembre 2025", "plateforme": "Prime Video"},
        {"titre": "Demon Slayer : L'Ultime Bataille", "date": "05 septembre 2025", "plateforme": "Crunchyroll"},
        {"titre": "The Mandalorian – Saison 4", "date": "06 septembre 2025", "plateforme": "Disney+"},
        {"titre": "Miraculous World – Rio", "date": "10 septembre 2025", "plateforme": "Netflix"},
        {"titre": "The Witcher – Saison 4", "date": "15 septembre 2025", "plateforme": "Netflix"},
        {"titre": "Shingeki no Kyojin – Épilogue", "date": "20 septembre 2025", "plateforme": "Crunchyroll"},
        {"titre": "Deadpool & Wolverine", "date": "22 septembre 2025", "plateforme": "Disney+"},
        {"titre": "My Hero Academia : Film 4", "date": "25 septembre 2025", "plateforme": "Cinéma"},
        {"titre": "Loki – Saison 3", "date": "27 septembre 2025", "plateforme": "Disney+"},
        {"titre": "Dragon Ball Super : Renaissance", "date": "30 septembre 2025", "plateforme": "Crunchyroll"},
        {"titre": "The Crown – Final", "date": "05 octobre 2025", "plateforme": "Netflix"},
        {"titre": "Solo Leveling – Saison 2", "date": "10 octobre 2025", "plateforme": "Crunchyroll"},
        {"titre": "Kingdom of Wakanda", "date": "12 octobre 2025", "plateforme": "Disney+"},
        {"titre": "Bleach TYBW – Partie 3", "date": "15 octobre 2025", "plateforme": "Disney+"},
        {"titre": "Harry Potter – La Série", "date": "20 octobre 2025", "plateforme": "HBO"},
        {"titre": "Chainsaw Man – Saison 2", "date": "25 octobre 2025", "plateforme": "Crunchyroll"},
        {"titre": "Black Clover : L'Empire Déchu", "date": "28 octobre 2025", "plateforme": "Netflix"},
        {"titre": "Moana 2 (Vaiana)", "date": "30 octobre 2025", "plateforme": "Disney+"},
        {"titre": "Tokyo Revengers – Final", "date": "02 novembre 2025", "plateforme": "Crunchyroll"},
        {"titre": "Avatar – La Légende de Korra : Le Retour", "date": "05 novembre 2025", "plateforme": "Netflix"},
        {"titre": "Percy Jackson – Saison 2", "date": "07 novembre 2025", "plateforme": "Disney+"},
        {"titre": "Mob Psycho 100 – Film final", "date": "10 novembre 2025", "plateforme": "Crunchyroll"},
        {"titre": "Frozen 3", "date": "15 novembre 2025", "plateforme": "Cinéma"},
        {"titre": "Ghibli Stories : Le Monde Caché", "date": "20 novembre 2025", "plateforme": "Netflix"},
        {"titre": "Batman : Rebirth", "date": "25 novembre 2025", "plateforme": "HBO"},
    ]