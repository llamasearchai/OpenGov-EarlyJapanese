"""Tests for the Katakana teaching module."""

import pytest

from opengov_earlyjapanese.core.katakana import KatakanaTeacher


class TestKatakanaTeacher:
    """Test suite for KatakanaTeacher."""

    @pytest.fixture
    def teacher(self):
        """Create a KatakanaTeacher instance."""
        return KatakanaTeacher()

    def test_initialization(self, teacher):
        """Test that KatakanaTeacher initializes correctly."""
        assert teacher is not None
        assert hasattr(teacher, "characters")
        assert hasattr(teacher, "rows")
        assert len(teacher.characters) > 0
        assert len(teacher.rows) > 0

    def test_get_lesson_a_row(self, teacher):
        """Test getting the a_row lesson."""
        lesson = teacher.get_lesson("a_row")
        assert lesson.row == "a_row"
        assert len(lesson.characters) == 5
        assert "ア" in lesson.characters
        assert "イ" in lesson.characters
        assert "ウ" in lesson.characters
        assert "エ" in lesson.characters
        assert "オ" in lesson.characters

    def test_get_lesson_ka_row(self, teacher):
        """Test getting the ka_row lesson."""
        lesson = teacher.get_lesson("ka_row")
        assert lesson.row == "ka_row"
        assert len(lesson.characters) == 5
        assert "カ" in lesson.characters

    def test_get_lesson_sa_row(self, teacher):
        """Test getting the sa_row lesson."""
        lesson = teacher.get_lesson("sa_row")
        assert lesson.row == "sa_row"
        assert len(lesson.characters) == 5
        assert "サ" in lesson.characters

    def test_get_lesson_ta_row(self, teacher):
        """Test getting the ta_row lesson."""
        lesson = teacher.get_lesson("ta_row")
        assert lesson.row == "ta_row"
        assert len(lesson.characters) == 5

    def test_get_lesson_na_row(self, teacher):
        """Test getting the na_row lesson."""
        lesson = teacher.get_lesson("na_row")
        assert lesson.row == "na_row"
        assert len(lesson.characters) == 5

    def test_get_lesson_ha_row(self, teacher):
        """Test getting the ha_row lesson."""
        lesson = teacher.get_lesson("ha_row")
        assert lesson.row == "ha_row"
        assert len(lesson.characters) == 5

    def test_get_lesson_ma_row(self, teacher):
        """Test getting the ma_row lesson."""
        lesson = teacher.get_lesson("ma_row")
        assert lesson.row == "ma_row"
        assert len(lesson.characters) == 5

    def test_get_lesson_ya_row(self, teacher):
        """Test getting the ya_row lesson."""
        lesson = teacher.get_lesson("ya_row")
        assert lesson.row == "ya_row"
        assert len(lesson.characters) == 3

    def test_get_lesson_ra_row(self, teacher):
        """Test getting the ra_row lesson."""
        lesson = teacher.get_lesson("ra_row")
        assert lesson.row == "ra_row"
        assert len(lesson.characters) == 5

    def test_get_lesson_wa_row(self, teacher):
        """Test getting the wa_row lesson."""
        lesson = teacher.get_lesson("wa_row")
        assert lesson.row == "wa_row"
        assert len(lesson.characters) == 3

    def test_get_lesson_invalid_row(self, teacher):
        """Test getting an invalid row raises ValueError."""
        with pytest.raises(ValueError, match="Unknown row"):
            teacher.get_lesson("invalid_row")

    def test_get_mnemonic_valid(self, teacher):
        """Test getting a mnemonic for a valid character."""
        mnemonic = teacher.get_mnemonic("ア")
        assert mnemonic is not None
        assert isinstance(mnemonic, str)
        assert len(mnemonic) > 0

    def test_get_mnemonic_invalid(self, teacher):
        """Test getting a mnemonic for an invalid character."""
        mnemonic = teacher.get_mnemonic("invalid")
        assert mnemonic is None

    def test_all_rows_have_characters(self, teacher):
        """Test that all rows have characters."""
        for row_name in teacher.rows.keys():
            lesson = teacher.get_lesson(row_name)
            assert len(lesson.characters) > 0
            assert len(lesson.mnemonics) > 0

    def test_characters_have_attributes(self, teacher):
        """Test that characters have proper attributes."""
        for char_obj in teacher.characters.values():
            assert char_obj.character
            assert char_obj.romaji
            assert char_obj.type == "katakana"
            assert char_obj.unicode
            assert char_obj.mnemonic is not None

    def test_lesson_mnemonics_match_characters(self, teacher):
        """Test that lesson mnemonics match the characters in the lesson."""
        lesson = teacher.get_lesson("a_row")
        for char in lesson.characters:
            assert char in lesson.mnemonics
            assert isinstance(lesson.mnemonics[char], str)

