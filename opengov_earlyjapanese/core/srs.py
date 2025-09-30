"""Simple spaced repetition system implementation."""

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Literal

from opengov_earlyjapanese.config import settings


Rating = Literal["again", "hard", "good", "easy"]


@dataclass
class SRSState:
    interval: int
    ease_factor: float
    repetitions: int
    next_review: datetime


class SpacedRepetitionSystem:
    def schedule(self, state: SRSState, rating: Rating) -> SRSState:
        ef = state.ease_factor
        reps = state.repetitions
        interval = state.interval

        if rating == "again":
            ef = max(1.3, ef - 0.2)
            interval = max(1, int(interval * settings.srs_fail_multiplier))
            reps = 0
        elif rating == "hard":
            ef = max(1.3, ef - 0.05)
            interval = max(1, int(interval * settings.srs_hard_multiplier))
            reps += 1
        elif rating == "good":
            interval = max(1, int(interval * settings.srs_normal_multiplier))
            reps += 1
        elif rating == "easy":
            ef = min(3.0, ef + 0.05)
            interval = max(1, int(interval * settings.srs_easy_multiplier))
            reps += 1

        next_review = datetime.utcnow() + timedelta(days=interval)
        return SRSState(interval=interval, ease_factor=ef, repetitions=reps, next_review=next_review)

