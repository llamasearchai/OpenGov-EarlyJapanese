"""Tests for the Grammar module."""

import pytest

from opengov_earlyjapanese.core.grammar import GrammarTeacher, GrammarExplanation


class TestGrammarTeacher:
    """Test suite for GrammarTeacher."""

    @pytest.fixture
    def teacher(self):
        """Create a GrammarTeacher instance."""
        return GrammarTeacher()

    def test_initialization(self, teacher):
        """Test that GrammarTeacher initializes correctly."""
        assert teacher is not None
        assert hasattr(teacher, "explain")
        assert hasattr(teacher, "_db")

    def test_explain_known_pattern(self, teacher):
        """Test explaining a known grammar pattern."""
        explanation = teacher.explain("です")
        assert isinstance(explanation, GrammarExplanation)
        assert explanation.pattern == "です"
        assert explanation.meaning == "to be (polite copula)"
        assert len(explanation.examples) > 0

    def test_explain_unknown_pattern(self, teacher):
        """Test explaining an unknown grammar pattern."""
        explanation = teacher.explain("unknown_pattern")
        assert isinstance(explanation, GrammarExplanation)
        assert explanation.pattern == "unknown_pattern"
        assert explanation.meaning == "(unknown)"
        assert explanation.structure == ""
        assert len(explanation.examples) == 0

    def test_explanation_structure(self, teacher):
        """Test that explanation has proper structure."""
        explanation = teacher.explain("です")
        assert isinstance(explanation.pattern, str)
        assert isinstance(explanation.meaning, str)
        assert isinstance(explanation.structure, str)
        assert isinstance(explanation.examples, list)

    def test_examples_are_strings(self, teacher):
        """Test that examples are strings."""
        explanation = teacher.explain("です")
        assert all(isinstance(ex, str) for ex in explanation.examples)

    def test_database_access(self, teacher):
        """Test that grammar database is accessible."""
        assert isinstance(teacher._db, dict)
        assert "です" in teacher._db

