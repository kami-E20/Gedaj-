from .admin import register_admin
from .adminpanel import register_adminpanel
from .lockdown import register_lockdown
from .forcefilm import register_forcefilm
from .forcequiz import register_forcequiz
from .forcenews import register_forcenews
from .senddebug import register_senddebug
from .restorebackup import register_restorebackup
from .call import register_call
from .test import register_test
from .prochainfilm import register_prochainfilm
from .anniversaire import register_anniversaire  # ✅ Import manquant

AUTHORIZED_ADMINS = [5618445554, 879386491]

def register_admin_commands(bot):
    print("✅ Enregistrement des commandes admin...")

    register_admin(bot)
    print("  └─ /admin OK")

    register_adminpanel(bot)
    print("  └─ /adminpanel OK")

    register_lockdown(bot)
    print("  └─ /lockdown OK")

    register_forcefilm(bot)
    print("  └─ /forcefilm OK")

    register_forcequiz(bot)
    print("  └─ /forcequiz OK")

    register_forcenews(bot)
    print("  └─ /forcenews OK")

    register_senddebug(bot)
    print("  └─ /senddebug OK")

    register_restorebackup(bot)
    print("  └─ /restorebackup OK")

    register_call(bot)
    print("  └─ /call OK")

    register_test(bot)
    print("  └─ /test OK")

    register_prochainfilm(bot)
    print("  └─ /prochainfilm OK")

    register_anniversaire(bot, AUTHORIZED_ADMINS)
    print("  └─ /anniversaire OK ✅")

    print("✅ Toutes les commandes admin ont été enregistrées.")