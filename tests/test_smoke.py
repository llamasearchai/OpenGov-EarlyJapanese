from opengov_earlyjapanese.core.hiragana import HiraganaTeacher
from opengov_earlyjapanese.core.kanji import KanjiMaster


def test_hiragana_lesson():
    t = HiraganaTeacher()
    lesson = t.get_lesson("a_row")
    assert lesson.characters[:3] == ["あ", "い", "う"]


def test_kanji_analysis():
    km = KanjiMaster()
    a = km.analyze("愛")
    assert "love" in a.meanings


def test_models_work():
    # Simple sanity check across modules remains
    assert hasattr(HiraganaTeacher, "get_lesson")
