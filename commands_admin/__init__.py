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

def register_admin_commands(bot):
    register_admin(bot)
    register_adminpanel(bot)
    register_lockdown(bot)
    register_forcefilm(bot)
    register_forcequiz(bot)
    register_forcenews(bot)
    register_senddebug(bot)
    register_restorebackup(bot)
    register_call(bot)
    register_test(bot)
    register_prochainfilm(bot)