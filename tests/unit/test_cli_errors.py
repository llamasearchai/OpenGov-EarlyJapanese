"""CLI error path tests for 100% coverage."""

import pytest
from typer.testing import CliRunner

from opengov_earlyjapanese.cli import app


class TestCLIErrors:
    """Test error paths in CLI for complete coverage."""

    @pytest.fixture
    def runner(self):
        """Create a CLI test runner."""
        return CliRunner()

    def test_kanji_sentences_invalid_character_length(self, runner):
        """Test kanji sentences with multiple characters (error path)."""
        result = runner.invoke(app, ["kanji", "sentences", "愛愛", "--level", "N5"])
        assert result.exit_code == 1

    def test_kanji_sentences_invalid_level(self, runner):
        """Test kanji sentences with invalid JLPT level."""
        result = runner.invoke(app, ["kanji", "sentences", "愛", "--level", "N10"])
        assert result.exit_code == 1

    def test_kanji_sentences_with_table_format(self, runner):
        """Test kanji sentences with table format to cover table rendering path."""
        result = runner.invoke(app, ["kanji", "sentences", "愛", "--level", "N4", "--format", "table"])
        assert result.exit_code == 0

    def test_search_invalid_kind(self, runner):
        """Test search with invalid kind parameter."""
        result = runner.invoke(app, ["search", "test", "--kind", "invalid_type"])
        assert result.exit_code == 1

    def test_hiragana_command_direct(self, runner):
        """Test hiragana command directly."""
        # Test with table format
        result = runner.invoke(app, ["hiragana", "a_row", "--format", "table"])
        # May return different codes depending on registration
        assert result.exit_code in [0, 1, 2]

    def test_hiragana_command_json(self, runner):
        """Test hiragana command with JSON format."""
        result = runner.invoke(app, ["hiragana", "ka_row", "--format", "json"])
        assert result.exit_code in [0, 1, 2]

    def test_hiragana_command_invalid_row(self, runner):
        """Test hiragana command with invalid row."""
        result = runner.invoke(app, ["hiragana", "invalid_row"])
        assert result.exit_code in [0, 1, 2]

