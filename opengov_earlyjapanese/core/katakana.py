"""Katakana teaching module (simplified)."""

from typing import Dict, List

from opengov_earlyjapanese.core.models import Character


class KatakanaTeacher:
    def __init__(self) -> None:
        self.characters = self._initialize_katakana()
        self.rows = self._organize_by_rows()

    def _initialize_katakana(self) -> Dict[str, Character]:
        data = {
            # a-row
            "ア": ("a", "a_row", "Angled shape like the letter 'A'"),
            "イ": ("i", "a_row", "Straight and simple like 'I'"),
            "ウ": ("u", "a_row", "Looks like a 'U' hook on top"),
            "エ": ("e", "a_row", "Three lines like 'E'"),
            "オ": ("o", "a_row", "Circle idea with an extra line: 'O'"),
            # ka-row
            "カ": ("ka", "ka_row", "KAtana blade angle"),
            "キ": ("ki", "ka_row", "Key-like three strokes"),
            "ク": ("ku", "ka_row", "Sharp beak KUrvature"),
            "ケ": ("ke", "ka_row", "KEttle handle"),
            "コ": ("ko", "ka_row", "Two KOorners"),
            # sa-row
            "サ": ("sa", "sa_row", "SAil with a mast"),
            "シ": ("shi", "sa_row", "SHImmery three dots"),
            "ス": ("su", "sa_row", "SUrfing curve"),
            "セ": ("se", "sa_row", "SEat and back"),
            "ソ": ("so", "sa_row", "SOaring two ticks"),
            # ta-row
            "タ": ("ta", "ta_row", "TAll and cross"),
            "チ": ("chi", "ta_row", "CHIsel shape"),
            "ツ": ("tsu", "ta_row", "TSUnami three dots"),
            "テ": ("te", "ta_row", "TEe with a line"),
            "ト": ("to", "ta_row", "TOoth corner"),
            # na-row
            "ナ": ("na", "na_row", "NAil and line"),
            "ニ": ("ni", "na_row", "Two NIce lines"),
            "ヌ": ("nu", "na_row", "NOOdle loop"),
            "ネ": ("ne", "na_row", "NEedle and hook"),
            "ノ": ("no", "na_row", "NO slash"),
            # ha-row
            "ハ": ("ha", "ha_row", "HA-shaped fork"),
            "ヒ": ("hi", "ha_row", "HIke trail turn"),
            "フ": ("fu", "ha_row", "FUji silhouette"),
            "ヘ": ("he", "ha_row", "HEdge up"),
            "ホ": ("ho", "ha_row", "HOtel sign"),
            # ma-row
            "マ": ("ma", "ma_row", "MArk with a tail"),
            "ミ": ("mi", "ma_row", "MId three lines"),
            "ム": ("mu", "ma_row", "MUsic note angle"),
            "メ": ("me", "ma_row", "MErging lines"),
            "モ": ("mo", "ma_row", "MOoring hook"),
            # ya-row
            "ヤ": ("ya", "ya_row", "YAcht mast"),
            "ユ": ("yu", "ya_row", "YU-shaped box"),
            "ヨ": ("yo", "ya_row", "YO-yo three lines"),
            # ra-row
            "ラ": ("ra", "ra_row", "RAil corner"),
            "リ": ("ri", "ra_row", "RIce shoots"),
            "ル": ("ru", "ra_row", "RUby tail"),
            "レ": ("re", "ra_row", "REed line"),
            "ロ": ("ro", "ra_row", "ROunded square"),
            # wa-row
            "ワ": ("wa", "wa_row", "WAve crest"),
            "ヲ": ("wo", "wa_row", "WOok mark"),
            "ン": ("n", "wa_row", "N zigzag"),
        }
        chars: Dict[str, Character] = {}
        for ch, (romaji, row, mnemonic) in data.items():
            chars[ch] = Character(
                id=f"katakana_{ch}",
                character=ch,
                unicode=f"U+{ord(ch):04X}",
                romaji=romaji,
                type="katakana",
                row=row,
                mnemonic=mnemonic,
            )
        return chars

    def _organize_by_rows(self) -> Dict[str, List[str]]:
        return {
            "a_row": ["ア", "イ", "ウ", "エ", "オ"],
            "ka_row": ["カ", "キ", "ク", "ケ", "コ"],
            "sa_row": ["サ", "シ", "ス", "セ", "ソ"],
            "ta_row": ["タ", "チ", "ツ", "テ", "ト"],
            "na_row": ["ナ", "ニ", "ヌ", "ネ", "ノ"],
            "ha_row": ["ハ", "ヒ", "フ", "ヘ", "ホ"],
            "ma_row": ["マ", "ミ", "ム", "メ", "モ"],
            "ya_row": ["ヤ", "ユ", "ヨ"],
            "ra_row": ["ラ", "リ", "ル", "レ", "ロ"],
            "wa_row": ["ワ", "ヲ", "ン"],
        }
