"""Complete CLI tests to reach 100% coverage."""

import pytest
from typer.testing import CliRunner

from opengov_earlyjapanese.cli import app


class TestCLIComplete:
    """Comprehensive CLI tests for complete coverage."""

    @pytest.fixture
    def runner(self):
        """Create a CLI test runner."""
        return CliRunner()

    def test_hiragana_table_format_complete(self, runner):
        """Test hiragana with table format to cover all table rendering."""
        # This should trigger the table rendering path including the _print_table function
        result = runner.invoke(app, ["characters", "ka_row", "--format", "table"])
        assert result.exit_code == 0

    def test_hiragana_json_format(self, runner):
        """Test hiragana with JSON format."""
        result = runner.invoke(app, ["characters", "sa_row", "--format", "json"])
        assert result.exit_code == 0

    def test_katakana_table_rendering_paths(self, runner):
        """Test katakana table rendering."""
        result = runner.invoke(app, ["katakana", "rows", "--format", "table"])
        assert result.exit_code == 0
        
        result2 = runner.invoke(app, ["--no-color", "katakana", "rows", "--format", "table"])
        assert result2.exit_code == 0

    def test_search_hiragana_table(self, runner):
        """Test search with hiragana kind and table format."""
        result = runner.invoke(app, ["search", "ka", "--kind", "hiragana", "--format", "table"])
        assert result.exit_code == 0

    def test_search_katakana_json(self, runner):
        """Test search with katakana kind and JSON format."""
        result = runner.invoke(app, ["search", "ka", "--kind", "katakana", "--format", "json"])
        assert result.exit_code == 0

    def test_all_kanji_sentence_levels_with_format(self, runner):
        """Test kanji sentences for all levels."""
        for level in ["N5", "N4", "N3", "N2", "N1"]:
            result = runner.invoke(app, ["kanji", "sentences", "愛", "--level", level])
            assert result.exit_code == 0

    def test_kanji_analyze_table_complete(self, runner):
        """Test kanji analyze with table format."""
        result = runner.invoke(app, ["kanji", "analyze", "愛", "-f", "table"])
        assert result.exit_code == 0

    def test_katakana_mnemonic_valid(self, runner):
        """Test katakana mnemonic with valid character."""
        result = runner.invoke(app, ["katakana", "mnemonic", "カ"])
        assert result.exit_code == 0

    def test_characters_all_rows(self, runner):
        """Test characters command for multiple rows."""
        for row in ["a_row", "ka_row", "sa_row"]:
            result = runner.invoke(app, ["characters", row])
            assert result.exit_code == 0

    def test_color_flag_combinations(self, runner):
        """Test various color flag combinations."""
        # With color
        result1 = runner.invoke(app, ["rows"])
        assert result1.exit_code == 0
        
        # Without color
        result2 = runner.invoke(app, ["--no-color", "rows"])
        assert result2.exit_code == 0

