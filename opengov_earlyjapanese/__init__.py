"""OpenGov-EarlyJapanese - Comprehensive AI-powered Japanese language learning platform."""

__version__ = "0.1.0"
__author__ = "Nik Jois"
__email__ = "nikjois@llamasearch.ai"

from .config import settings
from .core.hiragana import HiraganaTeacher
from .core.katakana import KatakanaTeacher
from .core.kanji import KanjiMaster
from .core.grammar import GrammarTeacher
from .core.srs import SpacedRepetitionSystem

__all__ = [
    "settings",
    "HiraganaTeacher",
    "KatakanaTeacher",
    "KanjiMaster",
    "GrammarTeacher",
    "SpacedRepetitionSystem",
    "__version__",
]
