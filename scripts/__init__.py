# scripts/__init__.py
"""
Expose uniquement des éléments internes à `scripts` pour éviter tout import circulaire.
NE PAS importer commands_admin ici (ça a déjà causé des boucles).
"""

from .admin_notify import send_admin_news
from .backup import backup_donnees
from .fetch_anilist_news import fetch_anilist_news
from .fetch_cinema_news import fetch_cinema_news
from .notify_sorties import notify_admins_sorties

from .points import (
    ajouter_points,
    publier_meilleurs_abonnes as publier_top_points,
)

from .points_logic import (
    update_points,
    sauvegarder_points_utilisateurs,
    get_points,
    charger_points,
)

# Les tâches orchestrées et run_all proviennent de scripts.publish
from .publish import (
    publier_actu_privee,
    publier_anniversaires,
    publier_film,
    publier_quiz,
    publier_correction,
    publier_meilleurs_abonnes,
    publier_abonnes_du_mois,
    envoyer_statistiques,
    sauvegarder_donnees,
    notifier_admins_daily,   # 👈 ajouté ici
    run_all,
)

__all__ = [
    "send_admin_news",
    "backup_donnees",
    "fetch_anilist_news",
    "fetch_cinema_news",
    "notify_admins_sorties",
    "ajouter_points",
    "publier_top_points",
    "update_points",
    "sauvegarder_points_utilisateurs",
    "get_points",
    "charger_points",
    "publier_actu_privee",
    "publier_anniversaires",
    "publier_film",
    "publier_quiz",
    "publier_correction",
    "publier_meilleurs_abonnes",
    "publier_abonnes_du_mois",
    "envoyer_statistiques",
    "sauvegarder_donnees",
    "notifier_admins_daily",  # 👈 ajouté ici aussi
    "run_all",
]