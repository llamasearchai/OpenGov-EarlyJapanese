"""Tests for the __main__ module."""

import pytest
from unittest.mock import patch, MagicMock


class TestMainModule:
    """Test suite for __main__ module."""

    @patch('opengov_earlyjapanese.__main__.app')
    def test_main_calls_app(self, mock_app):
        """Test that main() calls the app."""
        from opengov_earlyjapanese.__main__ import main
        
        main()
        mock_app.assert_called_once()

    @patch('opengov_earlyjapanese.__main__.app')
    def test_main_module_execution(self, mock_app):
        """Test that the module can be executed."""
        from opengov_earlyjapanese import __main__
        
        # Test that main function exists
        assert hasattr(__main__, 'main')
        assert callable(__main__.main)
        
        # Test calling main
        __main__.main()
        mock_app.assert_called_once()

    def test_main_function_exists(self):
        """Test that main function is defined."""
        from opengov_earlyjapanese.__main__ import main
        assert callable(main)

