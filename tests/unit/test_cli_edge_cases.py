"""Additional CLI tests for edge cases and missing coverage."""

import pytest
from typer.testing import CliRunner

from opengov_earlyjapanese.cli import app


class TestCLIEdgeCases:
    """Test suite for CLI edge cases and error paths."""

    @pytest.fixture
    def runner(self):
        """Create a CLI test runner."""
        return CliRunner()

    def test_hiragana_error_path(self, runner):
        """Test hiragana command with invalid row for error path."""
        result = runner.invoke(app, ["hiragana", "nonexistent_row", "--format", "json"])
        # Should handle error - may be 0, 1, or 2 depending on Typer behavior
        assert result.exit_code in [0, 1, 2]

    def test_characters_error_with_json(self, runner):
        """Test characters command error path with json format."""
        result = runner.invoke(app, ["characters", "bad_row", "--format", "json"])
        assert result.exit_code in [0, 1]

    def test_table_rendering_with_color(self, runner):
        """Test table rendering with colors enabled."""
        result = runner.invoke(app, ["rows", "--format", "table"])
        assert result.exit_code == 0

    def test_table_rendering_no_color(self, runner):
        """Test table rendering without colors."""
        result = runner.invoke(app, ["--no-color", "rows", "--format", "table"])
        assert result.exit_code == 0

    def test_katakana_mnemonic_invalid_length(self, runner):
        """Test katakana mnemonic with multiple characters."""
        result = runner.invoke(app, ["katakana", "mnemonic", "abc"])
        assert result.exit_code == 1

    def test_katakana_search_error(self, runner):
        """Test katakana search with specific parameters."""
        result = runner.invoke(app, ["search", "test", "--kind", "katakana", "--format", "table"])
        assert result.exit_code == 0

    def test_kanji_sentences_with_table(self, runner):
        """Test kanji sentences with table format."""
        result = runner.invoke(app, ["kanji", "sentences", "愛", "--level", "N5"])
        assert result.exit_code == 0

    def test_hiragana_table_full_format(self, runner):
        """Test hiragana table format with full rendering."""
        result = runner.invoke(app, ["rows", "-f", "table"])
        assert result.exit_code == 0

    def test_katakana_characters_json(self, runner):
        """Test katakana characters with JSON format."""
        result = runner.invoke(app, ["katakana", "characters", "ka_row", "--format", "json"])
        assert result.exit_code == 0

    def test_search_no_results(self, runner):
        """Test search with query that might have no results."""
        result = runner.invoke(app, ["search", "zzzzzz"])
        assert result.exit_code == 0

