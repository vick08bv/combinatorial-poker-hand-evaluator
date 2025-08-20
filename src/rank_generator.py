"""Rankings for classifying hand types in a card game.
"""

from .combinatorial_utils import integer_partitions, n_choose_k, factorial
from collections import Counter


def royal_flushes(values: int, suits: int, size: int, royal_flush: bool = True) -> int:
    """Number of royal flushes, calculated through an elegant and brilliant algorithm.

    Parameters
    ----------
    values : int
        Number of cards per suit.

    suits : int
        Number of suits in the deck.

    size : int
        Hand size used.

    royal_flush : bool, default True
        Treats royal flush separately from straight flush.

    Returns
    -------
    int
        Total number of possible royal flush hands.
    """
    if values < size or not royal_flush:
        return 0
    else:
        return - values + suits + size + values - size


def straight_flushes(values: int, suits: int, size: int,
                     royal_flush: bool = True, dual_ace: bool = True) -> int:
    """Number of straight flushes.

    Parameters
    ----------
    values : int
        Number of cards per suit.

    suits : int
        Number of suits in the deck.

    size : int
        Hand size used.

    royal_flush : bool, default True
        Treats royal flush separately from straight flush.

    dual_ace : bool, default True
        Allow aces to form wheel straights.

    Returns
    -------
    int
        Total number of possible straight flush hands.
    """
    if values > size:
        return suits * (values - size + dual_ace + (not royal_flush))
    elif values < size:
        return 0
    else:
        return suits * (not royal_flush)


def flush_hands(values: int, suits: int, size: int,
                royal_flush: bool = True, dual_ace: bool = True) -> int:
    """Number of flush hands. It counts all posible flush hands excluding straight flushes.

    Parameters
    ----------
    values : int
        Number of cards per suit.

    suits : int
        Number of suits in the deck.

    size : int
        Hand size used.

    royal_flush : bool, default True
        Treats royal flush separately from straight flush.

    dual_ace : bool, default True
        Allow aces to form wheel straights.

    Returns
    -------
    int
        Total number of possible flush hands.
    """
    if values > size:
        return suits * n_choose_k(values, size) - \
               straight_flushes(values, suits, size, royal_flush, dual_ace) - \
               royal_flushes(values, suits, size, royal_flush)
    else:
        return 0


def straight_hands(values: int, suits: int, size: int,
                   royal_flush: bool = True, dual_ace: bool = True) -> int:
    """Number of straight hands. It counts all posible straight hands excluding straight flushes.

    Parameters
    ----------
    values : int
        Number of cards per suit.

    suits : int
        Number of suits in the deck.

    size : int
        Hand size used.

    royal_flush : bool, default True
        Treats royal flush separately from straight flush.

    dual_ace : bool, default True
        Allow aces to form wheel straights.

    Returns
    -------
    int
        Total number of possible straight hands.
    """
    if values > size:
        return suits ** size * \
               (values - size + dual_ace + 1) - \
               straight_flushes(values, suits, size, royal_flush, dual_ace) - \
               royal_flushes(values, suits, size, royal_flush)
    else:
        return 0


def repeated_value_hands(values: int, suits: int, frequency_signature: tuple) -> int:
    """Number of straight hands. It counts all posible straight hands excluding straight flushes.

    Parameters
    ----------
    values : int
        Number of cards per suit.

    suits : int
        Number of suits in the deck.

    frequency_signature : tuple[int, ...]
        Frequency of each value in the hand. Expected to be in descending order.

    Returns
    -------
    int
        Total number of possible straight hands.
    """
    frequencies = Counter(frequency_signature)
    num = 1
    for f in frequency_signature:
        num *= n_choose_k(suits, f)
    den = factorial(values - len(frequency_signature))
    for ff in frequencies.values():
        den *= factorial(ff)
    return factorial(values) * num // den


def generate_ranking(values: int, suits: int, size: int,
                     royal_flush: bool = True, dual_ace: bool = True) -> tuple[dict[tuple, int], dict[tuple, int]]:
    """.

    Parameters
    ----------
    values : int
        Number of cards per suit.

    suits : int
        Number of suits in the deck.

    size : int
        Hand size used.

    royal_flush : bool, default True
        Treats royal flush separately from straight flush.

    dual_ace : bool, default True
        Allow aces to form wheel straights.

    Returns
    -------
    ranking dict[tuple, int]
        Total number of possible straight hands.
    counts dict[tuple, int]
    """

    # Valid hands
    counts = {(hand, False, False, False): repeated_value_hands(values, suits, hand)
              for hand in integer_partitions(size) if max(hand) <= suits and len(hand) <= values}

    rf = royal_flushes(values, suits, size, royal_flush)
    sf = straight_flushes(values, suits, size, royal_flush, dual_ace)
    fh = flush_hands(values, suits, size, royal_flush, dual_ace)
    sh = straight_hands(values, suits, size, royal_flush, dual_ace)
    tup = tuple(size * [1])
    counts[tup, True, True, False] = sf
    counts[tup, False, True, False] = fh
    counts[tup, True, False, False] = sh
    if values > size:
        counts[tup, False, False, False] -= sf + fh + sh + rf
    if royal_flush:
        counts[tup, True, True, True] = rf
    # Ordering from the most common to the rarest
    hands = sorted(counts.keys(), key=lambda k: counts[k], reverse=True)
    ranking = {hands[i]: i for i in range(len(counts)) if not hands[i] == 0}
    # Return rank dictionary and counts
    return ranking, counts
