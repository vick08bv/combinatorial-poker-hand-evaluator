import pytest
from src.rank_generator import (
    royal_flushes,
    straight_flushes,
    flush_hands,
    straight_hands,
    repeated_value_hands,
    generate_ranking,
)


def test_royal_flushes_basic():
    # trivial example
    assert royal_flushes(5, 3, 5) == 3
    # standard poker
    assert royal_flushes(13, 4, 5) == 4
    # values < size returns 0
    assert royal_flushes(3, 4, 5) == 0


def test_royal_flushes_disabled():
    assert royal_flushes(10, 4, 5, royal_flush=False) == 0


def test_straight_flushes_basic():
    # some straights
    assert straight_flushes(10, 4, 5) > 0
    # not enough values for a straight
    assert straight_flushes(3, 4, 5) == 0
    # border case
    assert straight_flushes(5, 2, 5, royal_flush=False) == 2


def test_flush_hands_basic():
    val = flush_hands(10, 4, 5)
    assert val > 0
    # should exclude straight flushes and royal flushes
    total_flush = 4 * 252
    assert val < total_flush


def test_flush_hands_not_enough_values():
    assert flush_hands(3, 4, 5) == 0


def test_straight_hands_basic():
    val = straight_hands(10, 4, 5)
    assert val > 0
    # should be less than total possible hands
    assert val < 4**5 * (10 - 5 + 1 + 1)


def test_straight_hands_small_values():
    # impossible
    assert straight_hands(3, 4, 5) == 0


def test_repeated_value_hands_pair():
    # one pair in a 5-card hand (freq signature = (2,1,1,1))
    val = repeated_value_hands(13, 4, (2,1,1,1))
    assert val > 0


def test_repeated_value_hands_full_house():
    # full house: (3,2)
    val = repeated_value_hands(13, 4, (3,2))
    assert val > 0


def test_generate_ranking_basic():
    ranking, counts = generate_ranking(5, 2, 3)
    assert isinstance(ranking, dict)
    assert isinstance(counts, dict)
    # all counts should be non-negative
    assert all(v >= 0 for v in counts.values())
    # ranking keys are a subset of counts keys
    assert set(ranking.keys()).issubset(set(counts.keys()))


def test_generate_ranking_with_royal_flush_disabled():
    ranking, counts = generate_ranking(5, 2, 3, royal_flush=False)
    # no royal flush key present
    assert not any(k[-1] for k in counts.keys())
