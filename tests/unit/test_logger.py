"""Tests for the logging utilities."""

import logging
import pytest

from opengov_earlyjapanese.utils.logger import get_logger


class TestLogger:
    """Test suite for logging utilities."""

    def test_get_logger_returns_logger(self):
        """Test that get_logger returns a logger instance."""
        logger = get_logger(__name__)
        assert logger is not None
        assert hasattr(logger, "info")
        assert hasattr(logger, "error")
        assert hasattr(logger, "debug")
        assert hasattr(logger, "warning")

    def test_get_logger_with_name(self):
        """Test that logger is created with a name parameter."""
        logger_name = "test_module"
        logger = get_logger(logger_name)
        assert logger is not None

    def test_logger_returns_something(self):
        """Test that logger returns a usable object."""
        logger = get_logger(__name__)
        # Logger should be usable
        assert logger is not None

    def test_multiple_loggers(self):
        """Test creating multiple loggers."""
        logger1 = get_logger("module1")
        logger2 = get_logger("module2")
        assert logger1 is not None
        assert logger2 is not None

    def test_logger_methods_exist(self):
        """Test that logger has all standard methods."""
        logger = get_logger(__name__)
        assert hasattr(logger, "debug")
        assert hasattr(logger, "info")
        assert hasattr(logger, "warning")
        assert hasattr(logger, "error")
        assert hasattr(logger, "critical")

    def test_logger_callable_methods(self):
        """Test that logger methods are callable."""
        logger = get_logger(__name__)
        assert callable(logger.debug)
        assert callable(logger.info)
        assert callable(logger.warning)
        assert callable(logger.error)
        assert callable(logger.critical)

    def test_logging_does_not_raise(self):
        """Test that logging calls don't raise exceptions."""
        logger = get_logger(__name__)
        try:
            logger.info("Test info message")
            logger.debug("Test debug message")
            logger.warning("Test warning message")
            logger.error("Test error message")
        except Exception as e:
            pytest.fail(f"Logging raised an exception: {e}")

