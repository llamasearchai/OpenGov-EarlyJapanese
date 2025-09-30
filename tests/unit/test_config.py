"""Tests for configuration module."""

import pytest
from opengov_earlyjapanese.config import Settings, get_settings


class TestConfig:
    """Test suite for configuration."""

    def test_settings_initialization(self):
        """Test that settings initializes with defaults."""
        settings = Settings()
        assert settings.api_host == "0.0.0.0"
        assert settings.api_port == 8000
        assert settings.api_version == "0.2.0"

    def test_get_settings_cached(self):
        """Test that get_settings returns cached instance."""
        settings1 = get_settings()
        settings2 = get_settings()
        assert settings1 is settings2

    def test_cors_origins_string_parsing(self):
        """Test that CORS origins can be parsed from string."""
        settings = Settings(cors_origins="http://localhost:3000,http://localhost:8501")
        assert isinstance(settings.cors_origins, list)
        assert len(settings.cors_origins) == 2

    def test_cors_origins_list(self):
        """Test that CORS origins can be provided as list."""
        origins = ["http://localhost:3000", "http://localhost:8501"]
        settings = Settings(cors_origins=origins)
        assert settings.cors_origins == origins

    def test_directories_creation(self):
        """Test that directories are created on initialization."""
        settings = Settings()
        assert settings.model_path.exists()
        assert settings.media_storage_path.exists()

    def test_jlpt_levels_default(self):
        """Test default JLPT levels."""
        settings = Settings()
        assert "N5" in settings.jlpt_levels
        assert "N1" in settings.jlpt_levels
        assert len(settings.jlpt_levels) == 5

    def test_srs_settings(self):
        """Test SRS algorithm settings."""
        settings = Settings()
        assert settings.srs_initial_interval == 1
        assert settings.srs_easy_multiplier == 2.5
        assert settings.srs_normal_multiplier == 2.0
        assert settings.srs_hard_multiplier == 1.3
        assert settings.srs_fail_multiplier == 0.5

    def test_learning_limits(self):
        """Test learning limit settings."""
        settings = Settings()
        assert settings.max_daily_reviews == 100
        assert settings.max_daily_new_items == 20

    def test_extra_fields_ignored(self):
        """Test that extra fields in environment are ignored."""
        # This should not raise an error due to extra="ignore"
        settings = Settings(extra_field="should_be_ignored")
        assert settings.api_host == "0.0.0.0"

