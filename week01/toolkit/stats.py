from collections import Counter
from typing import Hashable, Mapping, TypeVar

T = TypeVar("T", bound=Hashable)


def mean(numbers: list[float]) -> float:
    """Calculate and return the average of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(numbers) / len(numbers)


def median(numbers: list[float]) -> float:
    """Calculate and return the middle value."""
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")

    sorted_numbers = sorted(numbers)
    middle = len(sorted_numbers) // 2

    if len(sorted_numbers) % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2

    return sorted_numbers[middle]


def mode(items: list[T]) -> T:
    """Return the most frequently occurring item."""
    if not items:
        raise ValueError("Cannot calculate mode of empty list")
    return Counter(items).most_common(1)[0][0]


def count_by(items: list[dict[str, T]], key: str) -> dict[T, int]:
    """Count how often each value appears under a dictionary key."""
    return dict(Counter(item[key] for item in items))


def top_n(counts: Mapping[T, int], n: int = 3) -> list[tuple[T, int]]:
    """Return the N most common items in descending order."""
    return Counter(counts).most_common(n)
