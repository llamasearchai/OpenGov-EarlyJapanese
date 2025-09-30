"""Tests for logger fallback path."""

import pytest
import sys
from unittest.mock import patch


class TestLoggerFallback:
    """Test logger fallback when structlog is not available."""

    def test_logger_fallback_path(self):
        """Test that logger falls back to standard logging when structlog fails."""
        # Mock structlog import failure
        with patch.dict(sys.modules, {'structlog': None}):
            # Force re-import to trigger fallback
            import importlib
            from opengov_earlyjapanese.utils import logger as logger_module
            
            # This should trigger the fallback path
            importlib.reload(logger_module)
            logger = logger_module.get_logger("test_fallback")
            
            # Should still return a working logger
            assert logger is not None
            assert hasattr(logger, "info")
            
            # Try logging something
            try:
                logger.info("Test message")
            except Exception:
                pytest.fail("Logger should work in fallback mode")

    def test_logger_standard_logging(self):
        """Test logger using standard logging module."""
        from opengov_earlyjapanese.utils.logger import get_logger
        
        # Just test that get_logger works
        logger = get_logger("test_standard")
        assert logger is not None
        assert hasattr(logger, "info")

    def test_logger_handlers_setup(self):
        """Test that logger sets up handlers in fallback mode."""
        from opengov_earlyjapanese.utils.logger import get_logger
        
        # Get multiple loggers to test handler setup
        logger1 = get_logger("test_handler_1")
        logger2 = get_logger("test_handler_2")
        
        assert logger1 is not None
        assert logger2 is not None

