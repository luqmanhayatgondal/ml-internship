from collections import Counter


def mean(numbers: list[float]) -> float:
    """Return the average of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(numbers) / len(numbers)


def median(numbers: list[float]) -> float:
    """Return the middle value of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")

    sorted_numbers = sorted(numbers)
    middle = len(sorted_numbers) // 2

    if len(sorted_numbers) % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2

    return sorted_numbers[middle]


def mode(items: list) -> object:
    """Return the most common item."""
    if not items:
        raise ValueError("Cannot calculate mode of empty list")

    return Counter(items).most_common(1)[0][0]


def count_by(items: list, key: str) -> dict:
    """Count items using a dictionary key."""
    return dict(Counter(item[key] for item in items))


def top_n(counts: dict, n: int = 3) -> list:
    """Return the top N items by count."""
    return Counter(counts).most_common(n)
