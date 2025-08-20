"""Utilities for hand evaluation, using combinatorics.
"""

from math import factorial


def n_choose_k(n: int, k: int) -> int:
    """Number of ways of choosing k elements from a set with n elements.
    """
    if k <= 0 or k >= n:
        return 1
    else:
        r = 1
        d = min(k, n-k)
        for i in range(d):
            r *= n - i
        return r // factorial(d)


def k_subsets(n: int, k: int) -> set[frozenset]:
    """Subsets of size k from a set of size n.

    Parameters
    ----------
    n : int
        Size of the original set.

    k : int
        Size of each subset.

    Returns
    -------
    set[frozenset]
        k_subsets from the set {0, 1, ..., n-1}
    """
    if k <= 1:
        return {frozenset([i]) for i in range(n)}
    if k >= n:
        return {frozenset(range(n))}
    else:
        sets_with_n = [subset.union([n-1]) for subset in k_subsets(n-1, k-1)]
        return k_subsets(n-1, k).union(sets_with_n)


def k_integer_partitions(n: int, k: int) -> set[tuple]:
    """Ways of writing n as a sum of k positive integers.
    Order doesn't matter, although every partition is sorted in descending order.

    Based on the combinations with replacement problem:
    Given n and k, n-k 1's are separated into k groups to solve
    x1, ..., xk = n - k where x1, ..., xk are non negative integers.

    Parameters
    ----------
    n : int
        Sum of integers in each partition.
    k : int
        Size of every partition

    Returns
    -------
    partitions : set[tuple]
        Partitions with a fixed size k.
    """
    if k >= n:
        return {tuple(n * [1])}
    if k <= 1:
        return {(n, )}
    else:
        partitions = set()
        for subset in k_subsets(n-1, k-1):
            separators = [-1] + sorted(subset) + [n-k+len(subset)]
            solution = [separators[i+1] - separators[i] for i in range(len(separators) - 1)]
            partitions.add(tuple(sorted(solution, reverse=True)))
    return partitions


def integer_partitions(n: int) -> set[tuple]:
    """Ways of writing n as a sum of positive integers.
    Order don't matters, altough every partition is sorted in descending order.

    Parameters
    ----------
    n : int
        Sum of integers in any partition.

    Returns
    -------
    partitions : set[tuple]
        Partitions from size 1 to size n.
    """
    partitions = set()
    for k in range(1, n + 1):
        partitions.update(k_integer_partitions(n, k))
    return partitions
