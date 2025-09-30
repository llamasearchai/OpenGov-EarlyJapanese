"""Kanji learning utilities (offline sample data)."""

from typing import Dict, List

from pydantic import BaseModel

from opengov_earlyjapanese.core.models import JLPTLevel


class KanjiAnalysis(BaseModel):
    character: str
    meanings: List[str]
    on_reading: List[str]
    kun_reading: List[str]
    radicals: List[str]
    mnemonic: str


class KanjiMaster:
    def analyze(self, ch: str) -> KanjiAnalysis:
        # Minimal demo data
        data: Dict[str, Dict] = {
            "愛": {
                "meanings": ["love", "affection"],
                "on": ["アイ"],
                "kun": ["いと(しい)"],
                "radicals": ["爫", "冖", "心"],
                "mnemonic": "Claw hand over a cover with heart: love protects.",
            }
        }
        d = data.get(ch, {
            "meanings": ["unknown"],
            "on": [],
            "kun": [],
            "radicals": [],
            "mnemonic": "",
        })
        return KanjiAnalysis(
            character=ch,
            meanings=d["meanings"],
            on_reading=d["on"],
            kun_reading=d["kun"],
            radicals=d["radicals"],
            mnemonic=d["mnemonic"],
        )

    def generate_sentences(self, ch: str, level: str = "N5") -> List[str]:
        lvl = level if level in {"N5", "N4", "N3", "N2", "N1"} else JLPTLevel.N5.value
        base = {
            "N5": [f"{ch} が すきです。"],
            "N4": [f"{ch} は とても たいせつ です。"],
            "N3": [f"{ch} の きもち を つたえる。"],
            "N2": [f"{ch} を もとに かんがえを のべた。"],
            "N1": [f"{ch} に まつわる じじつ を ふまえて ろんじる。"],
        }
        return base[lvl]
