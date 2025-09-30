"""Configuration management for OpenGov-EarlyJapanese."""

from functools import lru_cache
import secrets
from pathlib import Path
from typing import List, Optional

from pydantic import Field, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # API Configuration
    api_host: str = Field(default="0.0.0.0")
    api_port: int = Field(default=8000)
    api_prefix: str = Field(default="/api/v1")
    api_title: str = Field(default="OpenGov-EarlyJapanese API")
    api_version: str = Field(default="0.2.0")

    # Security
    secret_key: SecretStr = Field(default_factory=lambda: SecretStr(secrets.token_urlsafe(32)))
    jwt_secret: SecretStr = Field(default_factory=lambda: SecretStr(secrets.token_urlsafe(32)))
    jwt_algorithm: str = Field(default="HS256")
    jwt_expiration_hours: int = Field(default=24)

    # Database
    database_url: Optional[str] = Field(default=None)
    redis_url: Optional[str] = Field(default=None)

    # AI Services (not used in this build)

    # Japanese NLP Settings
    mecab_dict_path: Optional[Path] = Field(default=None)
    use_sudachi: bool = Field(default=True)
    sudachi_mode: str = Field(default="C")  # A, B, or C

    # Learning Settings
    srs_initial_interval: int = Field(default=1)  # days
    srs_easy_multiplier: float = Field(default=2.5)
    srs_normal_multiplier: float = Field(default=2.0)
    srs_hard_multiplier: float = Field(default=1.3)
    srs_fail_multiplier: float = Field(default=0.5)

    max_daily_reviews: int = Field(default=100)
    max_daily_new_items: int = Field(default=20)
    session_time_limit: int = Field(default=60)  # minutes

    min_accuracy_for_advancement: float = Field(default=0.8)
    streak_bonus_threshold: int = Field(default=7)  # days

    # JLPT Levels
    jlpt_levels: List[str] = Field(default=["N5", "N4", "N3", "N2", "N1"])

    # Content Settings
    furigana_default: bool = Field(default=True)
    romaji_default: bool = Field(default=False)
    english_translations: bool = Field(default=True)

    # Speech Settings
    speech_recognition_language: str = Field(default="ja-JP")
    tts_speed: float = Field(default=1.0)
    pitch_accent_notation: bool = Field(default=True)

    # Gamification
    enable_gamification: bool = Field(default=True)
    xp_per_correct: int = Field(default=10)
    xp_per_streak_day: int = Field(default=50)
    achievement_system: bool = Field(default=True)

    # Community Features
    enable_forums: bool = Field(default=True)
    enable_language_exchange: bool = Field(default=True)
    enable_study_groups: bool = Field(default=True)

    # Media Storage
    media_storage_path: Path = Field(default=Path("media"))
    audio_format: str = Field(default="mp3")
    max_audio_length: int = Field(default=300)  # seconds

    # Cache Settings
    cache_ttl: int = Field(default=3600)  # seconds
    enable_caching: bool = Field(default=True)

    # Model Settings
    model_path: Path = Field(default=Path("models"))
    kanji_recognition_model: str = Field(default="kanji_cnn_v1")

    # Logging
    log_level: str = Field(default="INFO")
    log_format: str = Field(default="json")
    enable_metrics: bool = Field(default=True)

    # CORS
    cors_origins: List[str] = Field(default=["http://localhost:3000", "http://localhost:8501"])

    @field_validator("model_path", "media_storage_path")
    @classmethod
    def create_directories(cls, v: Path) -> Path:
        v.mkdir(parents=True, exist_ok=True)
        return v

    @field_validator("cors_origins", mode="before")
    @classmethod
    def parse_cors_origins(cls, v):
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
