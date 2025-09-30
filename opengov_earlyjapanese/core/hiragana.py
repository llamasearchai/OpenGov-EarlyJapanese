"""Hiragana teaching module."""

from typing import Dict, List, Optional

from pydantic import BaseModel

from opengov_earlyjapanese.core.models import Character
from opengov_earlyjapanese.utils.logger import get_logger

logger = get_logger(__name__)


class HiraganaLesson(BaseModel):
    row: str
    characters: List[str]
    mnemonics: Dict[str, str]


class HiraganaTeacher:
    """Teaches hiragana characters."""

    def __init__(self) -> None:
        self.characters = self._initialize_hiragana()
        self.rows = self._organize_by_rows()

    def _initialize_hiragana(self) -> Dict[str, Character]:
        hiragana_data = {
            "あ": ("a", "a_row", "Looks like an Apple with a leaf"),
            "い": ("i", "a_row", "Two vertical lines like 'ee' in 'eel'"),
            "う": ("u", "a_row", "Sideways 'u' with a swoosh"),
            "え": ("e", "a_row", "Looks like an Exotic bird"),
            "お": ("o", "a_row", "Person with a big 'Oh!' mouth"),
            "か": ("ka", "ka_row", "Knife CArving wood"),
            "き": ("ki", "ka_row", "A KEY with teeth"),
            "く": ("ku", "ka_row", "A COOl beak"),
            "け": ("ke", "ka_row", "A KEg on its side"),
            "こ": ("ko", "ka_row", "Two KOi fish"),
            "さ": ("sa", "sa_row", "A SAd face"),
            "し": ("shi", "sa_row", "SHE has long hair"),
            "す": ("su", "sa_row", "A spiral SUshi roll"),
            "せ": ("se", "sa_row", "A SEt of stairs"),
            "そ": ("so", "sa_row", "One SO-so zigzag"),
            "た": ("ta", "ta_row", "TAlking mouth with 'ta'"),
            "ち": ("chi", "ta_row", "CHEerleader with pom-poms"),
            "つ": ("tsu", "ta_row", "TSUnami wave"),
            "て": ("te", "ta_row", "A TElephone pole"),
            "と": ("to", "ta_row", "TOe with a nail"),
            "な": ("na", "na_row", "A kNOt tied"),
            "に": ("ni", "na_row", "Two NEedles"),
            "ぬ": ("nu", "na_row", "NUdles swirling"),
            "ね": ("ne", "na_row", "A NEst with an egg"),
            "の": ("no", "na_row", "NO entry sign"),
            "は": ("ha", "ha_row", "Person going HAha laughing"),
            "ひ": ("hi", "ha_row", "HEel of a shoe"),
            "ふ": ("fu", "ha_row", "Mount FUji"),
            "へ": ("he", "ha_row", "Going up a HEll"),
            "ほ": ("ho", "ha_row", "Two HOuses side by side"),
            "ま": ("ma", "ma_row", "MAsk on a face"),
            "み": ("mi", "ma_row", "Musical note MI"),
            "む": ("mu", "ma_row", "MOO says the cow"),
            "め": ("me", "ma_row", "MEssy noodles"),
            "も": ("mo", "ma_row", "MOre fish hooks"),
            "や": ("ya", "ya_row", "YAk with horns"),
            "ゆ": ("yu", "ya_row", "YUletide ornament"),
            "よ": ("yo", "ya_row", "YOyo string"),
            "ら": ("ra", "ra_row", "RAce track spiral"),
            "り": ("ri", "ra_row", "RIver flowing"),
            "る": ("ru", "ra_row", "RUby with a tail"),
            "れ": ("re", "ra_row", "REindeer antler"),
            "ろ": ("ro", "ra_row", "ROlling square"),
            "わ": ("wa", "wa_row", "WAve pattern"),
            "を": ("wo", "wa_row", "Person bowing WOw"),
            "ん": ("n", "wa_row", "Nose for N sound"),
        }

        characters: Dict[str, Character] = {}
        for char, (romaji, row, mnemonic) in hiragana_data.items():
            characters[char] = Character(
                id=f"hiragana_{char}",
                character=char,
                unicode=f"U+{ord(char):04X}",
                romaji=romaji,
                type="hiragana",
                row=row,
                mnemonic=mnemonic,
                example_words=self._get_example_words(char),
            )
        return characters

    def _organize_by_rows(self) -> Dict[str, List[str]]:
        return {
            "a_row": ["あ", "い", "う", "え", "お"],
            "ka_row": ["か", "き", "く", "け", "こ"],
            "sa_row": ["さ", "し", "す", "せ", "そ"],
            "ta_row": ["た", "ち", "つ", "て", "と"],
            "na_row": ["な", "に", "ぬ", "ね", "の"],
            "ha_row": ["は", "ひ", "ふ", "へ", "ほ"],
            "ma_row": ["ま", "み", "む", "め", "も"],
            "ya_row": ["や", "ゆ", "よ"],
            "ra_row": ["ら", "り", "る", "れ", "ろ"],
            "wa_row": ["わ", "を", "ん"],
        }

    def _get_example_words(self, character: str) -> List[Dict[str, str]]:
        examples = {
            "あ": [
                {"word": "あさ", "romaji": "asa", "meaning": "morning"},
                {"word": "あめ", "romaji": "ame", "meaning": "rain"},
            ],
            "い": [
                {"word": "いえ", "romaji": "ie", "meaning": "house"},
            ],
        }
        return examples.get(character, [])

    def get_lesson(self, row: str) -> HiraganaLesson:
        if row not in self.rows:
            raise ValueError(f"Unknown row: {row}")
        chars = self.rows[row]
        mnemonics = {c: self.characters[c].mnemonic or "" for c in chars}
        return HiraganaLesson(row=row, characters=chars, mnemonics=mnemonics)

    def get_mnemonic(self, character: str) -> Optional[str]:
        char = self.characters.get(character)
        return char.mnemonic if char else None
