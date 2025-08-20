import pytest
from src.combinatorial_utils import (
    n_choose_k,
    k_subsets,
    k_integer_partitions,
    integer_partitions,
)


def test_n_choose_k_basic():
    assert n_choose_k(5, 2) == 10
    assert n_choose_k(6, 3) == 20


def test_n_choose_k_edges():
    # choosing zero elements
    assert n_choose_k(5, 0) == 1
    # choosing all elements
    assert n_choose_k(5, 5) == 1
    # larger k should return 1
    assert n_choose_k(5, 6) == 1


def test_k_subsets_basic():
    # subsets of size 2 from {0,1,2,3}
    result = k_subsets(4, 2)
    expected = {
        frozenset({0, 1}),
        frozenset({0, 2}),
        frozenset({0, 3}),
        frozenset({1, 2}),
        frozenset({1, 3}),
        frozenset({2, 3}),
    }
    assert result == expected


def test_k_subsets_edge_cases():
    assert k_subsets(4, 1) == {frozenset({0}), frozenset({1}), frozenset({2}), frozenset({3})}
    assert k_subsets(4, 4) == {frozenset({0, 1, 2, 3})}


def test_k_integer_partitions_basic():
    # partitions of 5 into 2 numbers -> (4,1), (3,2)
    result = k_integer_partitions(5, 2)
    expected = {(4, 1), (3, 2)}
    assert result == expected


def test_k_integer_partitions_trivial():
    assert k_integer_partitions(5, 1) == {(5,)}
    assert k_integer_partitions(5, 5) == {(1, 1, 1, 1, 1)}


def test_integer_partitions_basic():
    result = integer_partitions(4)
    expected = {
        (4,),
        (3, 1),
        (2, 2),
        (2, 1, 1),
        (1, 1, 1, 1),
    }
    assert result == expected


def test_integer_partitions_contains_k_parts():
    # all partitions of 6 should include the size-3 partition (4,1,1)
    result = integer_partitions(6)
    assert (4, 1, 1) in result
    assert (2, 2, 2) in result
    assert (1, 1, 1, 1, 1, 1) in result
