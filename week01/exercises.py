import csv
import json
from collections import Counter, defaultdict
from collections.abc import Iterator


def reverse_string(text: str) -> str:
    """Return the string in reverse order."""
    return text[::-1]


print(reverse_string("Luqman"))


def count_vowels(sentence: str) -> int:
    """Count vowels in a sentence."""
    vowels = "aeiou"
    count = 0

    for letter in sentence.lower():
        if letter in vowels:
            count += 1

    return count


print(count_vowels("Hello World"))


def unique_words(sentence: str) -> list[str]:
    """Return sorted unique words in lowercase."""
    words = sentence.lower().split()
    return sorted(set(words))


print(unique_words("Apple banana apple Mango"))


def word_frequency(sentence: str) -> list[tuple[str, int]]:
    """Return the frequency of each word."""
    words = sentence.lower().split()
    return Counter(words).most_common(5)


print(word_frequency("cat cat dog cat dog"))


def flatten_list(nested_list: list[list[int]]) -> list[int]:
    """Return a single list from a nested list."""
    return [item for sublist in nested_list for item in sublist]


print(flatten_list([[1, 2], [3, 4], [5, 6]]))


def even_squares() -> list[int]:
    """Return squares of even numbers from 1 to 20."""
    return [number**2 for number in range(1, 21) if number % 2 == 0]


print(even_squares())


def create_age_dict(names: list[str], ages: list[int]) -> dict[str, int]:
    """Create a dictionary of names and ages."""
    return {name: age for name, age in zip(names, ages)}


names = ["Ali", "Sara", "Luqman"]
ages = [20, 22, 21]

print(create_age_dict(names, ages))


def compare_ips(
    first: list[str], second: list[str]
) -> tuple[set[str], set[str], set[str]]:
    """Compare two IP lists and return their differences."""
    first_set = set(first)
    second_set = set(second)

    common = first_set & second_set
    only_first = first_set - second_set
    only_second = second_set - first_set

    return common, only_first, only_second


ips1 = ["192.168.1.1", "10.0.0.1", "172.16.0.1"]
ips2 = ["192.168.1.1", "10.0.0.2", "172.16.0.1"]

print(compare_ips(ips1, ips2))


def count_non_empty_lines(file_path: str) -> int:
    """Count non-empty lines in a text file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return sum(1 for line in file if line.strip())


print(count_non_empty_lines("week01/sample.txt"))


def department_averages(file_path: str) -> dict[str, float]:
    """Calculate average score for each department."""
    department_scores: dict[str, list[int]] = {}

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            department = row["department"]
            score = int(row["score"])

            if department not in department_scores:
                department_scores[department] = []

            department_scores[department].append(score)

    averages = {}

    for department, scores in department_scores.items():
        averages[department] = sum(scores) / len(scores)

    return averages


print(department_averages("week01/data/sample.csv"))


def save_and_read_json(data: dict[str, object], file_path: str) -> dict[str, object]:
    """Save dictionary to JSON and read it back."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


student = {"name": "Luqman", "age": 21, "course": "AI/ML"}

result = save_and_read_json(student, "week01/data/student.json")

print(result)
print(result == student)


def safe_int(text: str) -> int | None:
    """Convert text to integer or return None."""
    try:
        return int(text)
    except ValueError:
        return None


print(safe_int("42"))
print(safe_int("hello"))


def lines_containing(file_path: str, word: str) -> Iterator[str]:
    """Yield lines that contain a specific word."""
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if word.lower() in line.lower():
                yield line.strip()


for line in lines_containing("week01/sample.txt", "Python"):
    print(line)


def group_words(words: list[str]) -> dict[str, list[str]]:
    """Group words by their first letter."""
    groups = defaultdict(list)

    for word in words:
        groups[word[0]].append(word)

    return dict(groups)


print(group_words(["apple", "ant", "banana", "ball", "cat"]))


assert reverse_string("Luqman") == "namquL"
assert count_vowels("Hello World") == 3
assert unique_words("apple banana apple") == ["apple", "banana"]
assert word_frequency("cat cat dog") == [("cat", 2), ("dog", 1)]
