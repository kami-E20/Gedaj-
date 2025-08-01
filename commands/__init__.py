from .start import register_start
from .help import register_help
from .quiz import register_quiz
from .correction import register_correction
from .filmdujour import register_filmdujour
from .suggestion import register_suggestion
from .spoiler import register_spoiler
from .avis import register_avis
from .fanpass import register_fanpass
from .classement import register_classement
from .translate import register_translate
from .lang import register_lang
from .abodumois import register_abodumois
from .inviter import register_inviter
from .prochainfilm import register_prochainfilm
from .vision import register_vision
from .defi import register_defi
from .source import register_source
from .recompenses import register_recompenses
from .textlistener import register_text_listener  # 🧠 écoute des messages texte

def register_user_commands(bot):
    register_start(bot)
    register_help(bot)
    register_quiz(bot)
    register_correction(bot)
    register_filmdujour(bot)
    register_suggestion(bot)
    register_spoiler(bot)
    register_avis(bot)
    register_fanpass(bot)
    register_classement(bot)
    register_translate(bot)
    register_lang(bot)
    register_abodumois(bot)
    register_inviter(bot)
    register_prochainfilm(bot)
    register_vision(bot)
    register_defi(bot)
    register_source(bot)
    register_recompenses(bot)
    register_text_listener(bot)