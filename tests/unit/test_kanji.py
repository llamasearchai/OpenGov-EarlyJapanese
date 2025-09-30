"""Tests for the Kanji module."""

import pytest

from opengov_earlyjapanese.core.kanji import KanjiMaster, KanjiAnalysis


class TestKanjiMaster:
    """Test suite for KanjiMaster."""

    @pytest.fixture
    def master(self):
        """Create a KanjiMaster instance."""
        return KanjiMaster()

    def test_analyze_love_kanji(self, master):
        """Test analyzing the kanji for 'love' (愛)."""
        result = master.analyze("愛")
        assert result is not None
        assert result.character == "愛"
        assert "love" in [m.lower() for m in result.meanings]
        assert len(result.on_reading) > 0
        assert len(result.kun_reading) > 0

    def test_analyze_kanji_structure(self, master):
        """Test that analysis returns proper structure."""
        result = master.analyze("愛")
        assert isinstance(result, KanjiAnalysis)
        assert isinstance(result.meanings, list)
        assert isinstance(result.on_reading, list)
        assert isinstance(result.kun_reading, list)
        assert isinstance(result.radicals, list)
        assert isinstance(result.mnemonic, str)

    def test_analyze_unknown_kanji(self, master):
        """Test analyzing an unknown kanji."""
        result = master.analyze("不")
        assert result.character == "不"
        assert "unknown" in result.meanings

    def test_generate_sentences_basic(self, master):
        """Test generating example sentences."""
        sentences = master.generate_sentences("愛", "N4")
        assert isinstance(sentences, list)
        assert len(sentences) >= 1
        for sentence in sentences:
            assert "愛" in sentence

    def test_generate_sentences_different_levels(self, master):
        """Test generating sentences for different JLPT levels."""
        for level in ["N5", "N4", "N3", "N2", "N1"]:
            sentences = master.generate_sentences("愛", level)
            assert len(sentences) >= 1
            assert all("愛" in s for s in sentences)

    def test_generate_sentences_invalid_level(self, master):
        """Test generating sentences with invalid level falls back to N5."""
        sentences = master.generate_sentences("愛", "INVALID")
        assert isinstance(sentences, list)
        assert len(sentences) >= 1

    def test_multiple_analyses(self, master):
        """Test analyzing multiple kanji."""
        kanji_list = ["愛", "愛", "愛"]
        results = [master.analyze(k) for k in kanji_list]
        assert len(results) == 3
        assert all(r.character == "愛" for r in results)

    def test_radicals_present(self, master):
        """Test that radicals are present in analysis."""
        result = master.analyze("愛")
        assert len(result.radicals) > 0
        assert all(isinstance(r, str) for r in result.radicals)

    def test_mnemonic_present(self, master):
        """Test that mnemonic is present."""
        result = master.analyze("愛")
        assert result.mnemonic
        assert len(result.mnemonic) > 0

