import pytest
from src.hand_evaluator import evaluate_hand


def test_evaluate_royal_flush():
    # Royal Flush example: Ace-high straight flush
    cards = [(14, 'hearts'), (13, 'hearts'), (12, 'hearts'), (11, 'hearts'), (10, 'hearts')]
    main_ace_value = 14
    sorted_hand, freq_sig, is_straight, is_flush, is_royal_flush = evaluate_hand(
        cards, main_ace_value
    )

    # Check types
    assert isinstance(sorted_hand, list)
    assert isinstance(freq_sig, tuple)
    assert isinstance(is_straight, bool)
    assert isinstance(is_flush, bool)
    assert isinstance(is_royal_flush, bool)

    # Check hand classification
    assert is_straight is True
    assert is_flush is True
    assert is_royal_flush is True
    # Frequency signature should be all ones
    assert freq_sig == (1, 1, 1, 1, 1)


def test_evaluate_worst_high_card():
    # Worst high card example: no pairs, no straight, no flush
    cards = [(2, 'hearts'), (3, 'clubs'), (4, 'diamonds'), (5, 'spades'), (7, 'hearts')]
    main_ace_value = 14
    sorted_hand, freq_sig, is_straight, is_flush, is_royal_flush = evaluate_hand(
        cards, main_ace_value
    )

    # Check hand classification
    assert is_straight is False
    assert is_flush is False
    assert is_royal_flush is False
    # Frequency signature should be all ones
    assert freq_sig == (1, 1, 1, 1, 1)


def test_evaluate_full_house():
    # Full House example: three of one value, two of another
    cards = [(10, 'hearts'), (10, 'spades'), (10, 'clubs'), (8, 'hearts'), (8, 'diamonds')]
    main_ace_value = 14
    sorted_hand, freq_sig, is_straight, is_flush, is_royal_flush = evaluate_hand(
        cards, main_ace_value
    )

    # Full house should not be straight or flush or royal flush
    assert is_straight is False
    assert is_flush is False
    assert is_royal_flush is False
    # Frequency signature should reflect three of a kind and a pair
    assert freq_sig == (3, 2)
