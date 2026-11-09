import pytest

from week01.toolkit.stats import mean, median, mode, top_n


def test_mean():
    assert mean([10, 20, 30]) == 20


def test_mean_empty():
    with pytest.raises(ValueError):
        mean([])


def test_median_odd():
    assert median([3, 1, 2]) == 2


def test_median_even():
    assert median([1, 2, 3, 4]) == 2.5


def test_mode():
    assert mode(["cat", "dog", "cat"]) == "cat"


def test_top_n():
    assert top_n({"apple": 5, "banana": 2, "orange": 3}, 2) == [
        ("apple", 5),
        ("orange", 3),
    ]
