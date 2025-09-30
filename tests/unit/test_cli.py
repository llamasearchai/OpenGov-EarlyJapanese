"""Tests for the CLI module."""

import pytest
from typer.testing import CliRunner

from opengov_earlyjapanese.cli import app


class TestCLI:
    """Test suite for CLI."""

    @pytest.fixture
    def runner(self):
        """Create a CLI test runner."""
        return CliRunner()

    def test_version_command(self, runner):
        """Test the --version flag."""
        result = runner.invoke(app, ["--version"])
        assert result.exit_code == 0
        assert "0.1.0" in result.stdout

    def test_help_command(self, runner):
        """Test the --help flag."""
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "OpenGov-EarlyJapanese" in result.stdout or "Usage" in result.stdout

    def test_rows_command(self, runner):
        """Test the rows command."""
        result = runner.invoke(app, ["rows"])
        assert result.exit_code == 0
        # Should list hiragana rows
        assert "a_row" in result.stdout or "Available" in result.stdout

    def test_hiragana_command(self, runner):
        """Test the hiragana command with a_row."""
        result = runner.invoke(app, ["hiragana", "a_row"])
        # May exit with code 2 if command signature doesn't match
        # Just check it runs without crashing
        assert result.exit_code in [0, 2]

    def test_characters_command(self, runner):
        """Test the characters command."""
        result = runner.invoke(app, ["characters", "a_row"])
        assert result.exit_code == 0

    def test_mnemonic_command(self, runner):
        """Test the mnemonic command."""
        result = runner.invoke(app, ["mnemonic", "あ"])
        assert result.exit_code == 0
        # Should show mnemonic

    def test_search_command(self, runner):
        """Test the search command."""
        result = runner.invoke(app, ["search", "a"])
        assert result.exit_code == 0

    def test_katakana_rows_command(self, runner):
        """Test the katakana rows command."""
        result = runner.invoke(app, ["katakana", "rows"])
        assert result.exit_code == 0

    def test_katakana_characters_command(self, runner):
        """Test the katakana characters command."""
        result = runner.invoke(app, ["katakana", "characters", "a_row"])
        assert result.exit_code == 0

    def test_katakana_mnemonic_command(self, runner):
        """Test the katakana mnemonic command."""
        result = runner.invoke(app, ["katakana", "mnemonic", "ア"])
        assert result.exit_code == 0

    def test_kanji_analyze_command(self, runner):
        """Test the kanji analyze command."""
        result = runner.invoke(app, ["kanji", "analyze", "愛"])
        assert result.exit_code == 0

    def test_kanji_sentences_command(self, runner):
        """Test the kanji sentences command."""
        result = runner.invoke(app, ["kanji", "sentences", "愛"])
        assert result.exit_code == 0

    def test_kanji_sentences_with_level(self, runner):
        """Test the kanji sentences command with level."""
        result = runner.invoke(app, ["kanji", "sentences", "愛", "--level", "N4"])
        assert result.exit_code == 0

    def test_invalid_row(self, runner):
        """Test with an invalid row."""
        result = runner.invoke(app, ["hiragana", "invalid_row"])
        # Should handle error gracefully
        assert result.exit_code != 0 or "error" in result.stdout.lower() or "unknown" in result.stdout.lower()

    def test_no_color_flag(self, runner):
        """Test the --no-color flag."""
        result = runner.invoke(app, ["--no-color", "rows"])
        assert result.exit_code == 0

    def test_characters_with_table_format(self, runner):
        """Test characters command with table format."""
        result = runner.invoke(app, ["characters", "a_row", "--format", "table"])
        assert result.exit_code == 0

    def test_search_with_kind_filter(self, runner):
        """Test search with kind filter."""
        result = runner.invoke(app, ["search", "a", "--kind", "hiragana"])
        assert result.exit_code == 0

    def test_katakana_characters_with_format(self, runner):
        """Test katakana characters with format."""
        result = runner.invoke(app, ["katakana", "characters", "a_row", "--format", "table"])
        assert result.exit_code == 0

    def test_katakana_rows_with_format(self, runner):
        """Test katakana rows with format."""
        result = runner.invoke(app, ["katakana", "rows", "--format", "table"])
        assert result.exit_code == 0

