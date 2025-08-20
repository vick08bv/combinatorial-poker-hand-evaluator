"""Evaluator for n-card hands.
"""

from typing import Any
from collections import Counter


def evaluate_hand(cards: list[tuple[int, Any]],
                  main_ace_value: int,
                  accept_royal_flush: bool = True,
                  allow_dual_ace: bool = True,
                  replace_value: bool = True,
                  alt_ace_value: int = 1) -> tuple[list[tuple[int, Any]], tuple[int, ...], bool, bool, bool]:
    """ Determines the type of src hand given a set of cards.
        First, it computes the frequency signature of the card values,
        Then, it checks for special hands like straights, flushes, high cards...
        When a value is repeated, hand type is inferred from the frequency signature.
        For instance, a signature of (3,2) (three cards of one value and two cards of a second value)
        corresponds to a full-house in standard src.

    Parameters
    ----------
    cards : list[tuple[int, Any]]
        Cards as tuples. First element is the value, second the suit.
    main_ace_value : int
        Numerical value of the aces, the best valued cards in the deck.
    accept_royal_flush : bool, default True
        Recognize a royal flush as a proper category in the ranking or as
        another straight flush.
    allow_dual_ace : bool default True
        Allow aces to be part of the lowest straight (wheel).
        Equivalently, determine if wheels are straight hands.
    replace_value : bool default True
        Change ace value in a wheel.
    alt_ace_value : int default 1
        Alternative ace value in wheels.

    Returns
    -------
    sorted_hand : list[tuple[int, Any]]
        Cards sorted in descending order, by value frequency and then by value.
    frequency_signature : tuple[int, ...]
        Frequency of each value in the hand. Sorted in descending order.
    is_straight : bool
        Hand is a straight.
    is_flush : bool
        Hand is a flush.
    is_royal_flush : bool
        Hand is a royal flush.

    Notes
    -----
    When both is_straight and is_flush are True, the hand is a straight flush.
    """
    sorted_hand = sorted(cards, key=lambda card: card[0], reverse=True)

    values = [card[0] for card in sorted_hand]
    value_frequencies = Counter(values)

    is_flush, is_straight, is_royal_flush = False, False, False
    frequency_signature = tuple(sorted(value_frequencies.values(), reverse=True))

    # special hand
    if frequency_signature[0] == 1:

        is_flush = len(set(card[1] for card in sorted_hand)) == 1
        is_straight = values[0] - values[-1] == len(cards) - 1

        # wheel hand
        if not is_straight and allow_dual_ace:
            if values[0] == main_ace_value and values[1] - values[-1] == len(cards) - 2:
                is_straight = values[-1] - alt_ace_value == 1
                if is_straight:
                    if replace_value:
                        sorted_hand = sorted_hand[1:] + [(alt_ace_value, sorted_hand[0][1])]
                    else:
                        sorted_hand = sorted_hand[1:] + sorted_hand[:1]

        # royal flush
        elif is_straight and values[0] == main_ace_value:
            is_royal_flush = is_flush and accept_royal_flush

    # repeated value hand
    else:
        sorted_hand.sort(key=lambda card: value_frequencies[card[0]], reverse=True)
    return sorted_hand, frequency_signature, is_straight, is_flush, is_royal_flush
