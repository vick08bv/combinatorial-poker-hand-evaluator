"""Base-n scoring system for poker hands,
designed for flexible and consistent hand rankings.
"""

from math import log


def hand_score(card_values: list[int], hand_rank: int, ace_value: int) -> int:
    """Calculate the score of a poker hand.
    The scoring system ensures that rarer hands receive higher scores.
    Within the same hand rank, the score correctly distinguishes stronger hands from weaker ones.
    The numerical base used is (ace_value + 1), which guarantees consistency in ranking.


    Parameters
    ----------
    card_values : list[int]
        Card values sorted by frequency and then by value, in descending order.

    hand_rank : int
        The hierarchical rank of the hand,
        where a higher value indicates a rarer and stronger hand.

    ace_value : int
        Numerical value of aces: the most valuated cards in the game.

    Returns
    -------
    score : int
        The computed score of the hand.
    """
    score = 0
    base = ace_value + 1
    exponent = len(card_values) + hand_rank - 1
    for k in range(len(card_values)):
        score += card_values[k] * (base ** (exponent - k))
    return score


def log_score(card_values: list[int], hand_rank: int, ace_value: int) -> float:
    """Calculate the logarithm of the score for a poker hand.
    The scoring system ensures that rarer hands receive higher scores.
    Within the same hand rank, the score correctly distinguishes stronger hands from weaker ones.
    The numerical base used is (ace_value + 1), which guarantees consistency in ranking.
    Uses logarithm to linearize the relation between rankings and scores.

    Parameters
    ----------
    card_values : list[int]
        Card values sorted by frequency and then by value, in descending order.

    hand_rank : int
        The hierarchical rank of the hand,
        where a higher value indicates a rarer and stronger hand.

    ace_value : int
        Numerical value of aces: the most valuated cards in the game.

    Returns
    -------
    score : float
        The computed positive alternative score of the hand.
    """
    score = 0
    base = ace_value + 1
    exponent = len(card_values) + hand_rank - 1
    for k in range(len(card_values)):
        score += card_values[k] * (base ** (exponent - k))
    return log(score, base)
