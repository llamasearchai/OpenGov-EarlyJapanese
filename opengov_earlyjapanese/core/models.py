"""Core data models for Japanese language learning."""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class JLPTLevel(str, Enum):
    N5 = "N5"
    N4 = "N4"
    N3 = "N3"
    N2 = "N2"
    N1 = "N1"


class LearningMode(str, Enum):
    RECOGNITION = "recognition"
    PRODUCTION = "production"
    LISTENING = "listening"
    SPEAKING = "speaking"


class ContentType(str, Enum):
    HIRAGANA = "hiragana"
    KATAKANA = "katakana"
    KANJI = "kanji"
    VOCABULARY = "vocabulary"
    GRAMMAR = "grammar"
    READING = "reading"
    LISTENING = "listening"
    CULTURE = "culture"
    BUSINESS = "business"


class Student(BaseModel):
    id: str
    username: str
    email: str
    native_language: str = "en"
    target_level: JLPTLevel = JLPTLevel.N5
    current_level: Optional[JLPTLevel] = None
    learning_goals: List[str] = []
    daily_goal_minutes: int = 30
    preferred_learning_time: Optional[str] = None

    total_study_time: int = 0
    current_streak: int = 0
    longest_streak: int = 0
    xp_points: int = 0
    achievements: List[str] = []

    hiragana_progress: float = 0.0
    katakana_progress: float = 0.0
    kanji_known: int = 0
    vocabulary_known: int = 0

    preferences: Dict[str, Any] = {}
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_study_date: Optional[datetime] = None


class Character(BaseModel):
    id: str
    character: str
    unicode: str
    romaji: str
    type: str
    row: str
    mnemonic: Optional[str] = None
    stroke_order: List[str] = []
    audio_url: Optional[str] = None
    example_words: List[Dict[str, str]] = []
    similar_characters: List[str] = []


class Kanji(BaseModel):
    id: str
    character: str
    unicode: str
    jlpt_level: JLPTLevel
    grade: int
    stroke_count: int

    meanings: List[str]
    on_readings: List[str] = []
    kun_readings: List[str] = []

    radicals: List[str] = []
    components: List[str] = []

    stroke_order: List[str] = []
    mnemonic: Optional[str] = None

    example_words: List[Dict[str, str]] = []
    example_sentences: List[Dict[str, str]] = []

    frequency_rank: Optional[int] = None
    similar_kanji: List[str] = []


class Vocabulary(BaseModel):
    id: str
    word: str
    reading: str
    meanings: List[str]
    part_of_speech: str
    jlpt_level: JLPTLevel

    kanji_breakdown: List[str] = []
    pitch_accent: Optional[str] = None
    audio_url: Optional[str] = None

    example_sentences: List[Dict[str, str]] = []
    synonyms: List[str] = []
    antonyms: List[str] = []

    categories: List[str] = []
    usage_notes: Optional[str] = None
    frequency_rank: Optional[int] = None


class GrammarPoint(BaseModel):
    id: str
    pattern: str
    meaning: str
    jlpt_level: JLPTLevel
    structure: str
    formation: List[str]
    example_sentences: List[Dict[str, str]] = []
    usage_notes: Optional[str] = None
    related_grammar: List[str] = []
    formal_level: str = "neutral"
    common_mistakes: List[str] = []


class Lesson(BaseModel):
    id: str
    title: str
    description: str
    type: ContentType
    level: JLPTLevel
    objectives: List[str]
    prerequisites: List[str] = []
    content_items: List[str]
    exercises: List[str] = []
    estimated_minutes: int
    order_index: int
    cultural_notes: Optional[str] = None
    teacher_notes: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class StudySession(BaseModel):
    id: str
    student_id: str
    start_time: datetime = Field(default_factory=datetime.utcnow)
    end_time: Optional[datetime] = None
    duration_minutes: int = 0
    content_type: ContentType
    items_studied: List[str] = []
    items_correct: int = 0
    items_incorrect: int = 0
    xp_earned: int = 0
    achievements_unlocked: List[str] = []
    performance_metrics: Dict[str, float] = {}
    feedback: Optional[str] = None


class ReviewItem(BaseModel):
    id: str
    student_id: str
    content_type: ContentType
    content_id: str
    interval: int = 1
    ease_factor: float = 2.5
    repetitions: int = 0
    last_review: Optional[datetime] = None
    next_review: datetime = Field(default_factory=datetime.utcnow)
    total_reviews: int = 0
    correct_reviews: int = 0
    accuracy: float = 0.0
    learning_mode: LearningMode = LearningMode.RECOGNITION


class ConversationMessage(BaseModel):
    id: str
    session_id: str
    speaker: str
    japanese: str
    romaji: Optional[str] = None
    english: Optional[str] = None
    audio_url: Optional[str] = None
    grammar_points: List[str] = []
    vocabulary: List[str] = []
    corrections: List[Dict[str, str]] = []
    feedback: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)

