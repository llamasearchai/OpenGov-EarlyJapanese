"""Tests for the Spaced Repetition System."""

import pytest
from datetime import datetime, timedelta

from opengov_earlyjapanese.core.srs import SpacedRepetitionSystem, SRSState


class TestSpacedRepetitionSystem:
    """Test suite for SpacedRepetitionSystem."""

    @pytest.fixture
    def srs(self):
        """Create an SRS instance."""
        return SpacedRepetitionSystem()

    @pytest.fixture
    def initial_state(self):
        """Create an initial SRS state."""
        return SRSState(
            interval=1,
            ease_factor=2.5,
            repetitions=0,
            next_review=datetime.utcnow() + timedelta(days=1)
        )

    def test_schedule_again_rating(self, srs, initial_state):
        """Test scheduling with 'again' rating."""
        new_state = srs.schedule(initial_state, "again")
        assert new_state.ease_factor < initial_state.ease_factor
        assert new_state.ease_factor >= 1.3
        assert new_state.repetitions == 0
        assert new_state.interval >= 1

    def test_schedule_hard_rating(self, srs, initial_state):
        """Test scheduling with 'hard' rating."""
        new_state = srs.schedule(initial_state, "hard")
        assert new_state.ease_factor < initial_state.ease_factor
        assert new_state.ease_factor >= 1.3
        assert new_state.repetitions == initial_state.repetitions + 1
        assert new_state.interval >= 1

    def test_schedule_good_rating(self, srs, initial_state):
        """Test scheduling with 'good' rating."""
        new_state = srs.schedule(initial_state, "good")
        assert new_state.ease_factor == initial_state.ease_factor
        assert new_state.repetitions == initial_state.repetitions + 1
        assert new_state.interval >= initial_state.interval

    def test_schedule_easy_rating(self, srs, initial_state):
        """Test scheduling with 'easy' rating."""
        new_state = srs.schedule(initial_state, "easy")
        assert new_state.ease_factor > initial_state.ease_factor
        assert new_state.ease_factor <= 3.0
        assert new_state.repetitions == initial_state.repetitions + 1
        assert new_state.interval > initial_state.interval

    def test_ease_factor_minimum(self, srs):
        """Test that ease factor doesn't go below minimum."""
        state = SRSState(
            interval=1,
            ease_factor=1.3,
            repetitions=0,
            next_review=datetime.utcnow()
        )
        new_state = srs.schedule(state, "again")
        assert new_state.ease_factor == 1.3

    def test_ease_factor_maximum(self, srs):
        """Test that ease factor doesn't go above maximum."""
        state = SRSState(
            interval=1,
            ease_factor=3.0,
            repetitions=5,
            next_review=datetime.utcnow()
        )
        new_state = srs.schedule(state, "easy")
        assert new_state.ease_factor == 3.0

    def test_interval_minimum(self, srs):
        """Test that interval doesn't go below 1 day."""
        state = SRSState(
            interval=1,
            ease_factor=2.5,
            repetitions=0,
            next_review=datetime.utcnow()
        )
        new_state = srs.schedule(state, "again")
        assert new_state.interval >= 1

    def test_next_review_date_updated(self, srs, initial_state):
        """Test that next review date is properly updated."""
        before = datetime.utcnow()
        new_state = srs.schedule(initial_state, "good")
        after = datetime.utcnow()
        
        # Next review should be in the future
        assert new_state.next_review > before
        # And should be at least interval days from now
        expected_min = after + timedelta(days=new_state.interval - 1)
        assert new_state.next_review >= expected_min

    def test_repetitions_reset_on_again(self, srs):
        """Test that repetitions reset to 0 on 'again' rating."""
        state = SRSState(
            interval=7,
            ease_factor=2.5,
            repetitions=5,
            next_review=datetime.utcnow()
        )
        new_state = srs.schedule(state, "again")
        assert new_state.repetitions == 0

    def test_repetitions_increment_on_success(self, srs, initial_state):
        """Test that repetitions increment on successful ratings."""
        for rating in ["hard", "good", "easy"]:
            state = SRSState(
                interval=1,
                ease_factor=2.5,
                repetitions=3,
                next_review=datetime.utcnow()
            )
            new_state = srs.schedule(state, rating)
            assert new_state.repetitions == 4

    def test_interval_increases_with_good_ratings(self, srs):
        """Test that intervals increase with repeated good ratings."""
        state = SRSState(
            interval=1,
            ease_factor=2.5,
            repetitions=0,
            next_review=datetime.utcnow()
        )
        
        # Simulate multiple good ratings
        for _ in range(5):
            state = srs.schedule(state, "good")
        
        # Interval should have increased significantly
        assert state.interval > 5
        assert state.repetitions == 5

