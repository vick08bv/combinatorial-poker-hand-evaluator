import pytest
from src.score_system import hand_score, log_score


def test_hand_score_royal_flush():
    # Royal flush
    values = [14, 13, 12, 11, 10]
    hand_rank = 9
    ace_value = 14
    score = hand_score(values, hand_rank, ace_value)
    assert isinstance(score, int)
    # highest score in standard poker
    assert score == 29043958007812500


def test_hand_score_high_card():
    # Worst high card
    values = [5, 4, 3, 2, 14]
    hand_rank = 0
    ace_value = 14
    score = hand_score(values, hand_rank, ace_value)
    assert isinstance(score, int)
    # lowest score in standard poker
    assert score == 267344


def test_log_score_royal_flush():
    # Royal flush
    values = [14, 13, 12, 11, 10]
    hand_rank = 9
    ace_value = 14
    score = log_score(values, hand_rank, ace_value)
    assert isinstance(score, float)
    assert score > 0


def test_log_score_high_card():
    # Worst high card
    values = [5, 4, 3, 2, 14]
    hand_rank = 0
    ace_value = 14
    score = log_score(values, hand_rank, ace_value)
    assert isinstance(score, float)
    assert score > 0
