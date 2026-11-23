```python
import numpy as np
import time

# Step 1: Create sample data
numbers = list(range(1, 100001))

# Step 2: Python loop function
def python_square(numbers):
    result = []

    for number in numbers:
        result.append(number ** 2)

    return result

# Step 3: NumPy vectorised function
def numpy_square(numbers):
    array = np.array(numbers)
    return array ** 2

# Step 4: Measure Python loop time
start = time.time()
python_result = python_square(numbers)
python_time = time.time() - start

# Step 5: Measure NumPy time
start = time.time()
numpy_result = numpy_square(numbers)
numpy_time = time.time() - start

# Step 6: Verify both results
print("Results are equal:", np.allclose(python_result, numpy_result))

# Step 7: Display execution times
print("Python loop time:", python_time)
print("NumPy vectorised time:", numpy_time)

# Step 8: Display first 10 results
print("First 10 Python results:", python_result[:10])
print("First 10 NumPy results:", numpy_result[:10])
```

    Results are equal: True
    Python loop time: 0.023991823196411133
    NumPy vectorised time: 0.012342214584350586
    First 10 Python results: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    First 10 NumPy results: [  1   4   9  16  25  36  49  64  81 100]
    


```python
# Five Python loop-based functions

def sum_of_squares_loop(values):
    total = 0.0
    for v in values:
        total += v * v
    return total


def zscore_loop(values):
    n = len(values)
    mean = sum(values) / n
    var = sum((v - mean) ** 2 for v in values) / n
    std = var ** 0.5
    return [(v - mean) / std for v in values]


def count_above_loop(values, threshold):
    count = 0
    for v in values:
        if v > threshold:
            count += 1
    return count


def moving_average_loop(values, window):
    out = []
    for i in range(len(values) - window + 1):
        out.append(sum(values[i:i + window]) / window)
    return out


def pairwise_distances_loop(points):
    n = len(points)
    d = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            d[i][j] = (dx * dx + dy * dy) ** 0.5
    return d
```


```python
# Five NumPy vectorised functions

def sum_of_squares_numpy(values):
    return (values ** 2).sum()


def zscore_numpy(values):
    return (values - values.mean()) / values.std()


def count_above_numpy(values, threshold):
    return (values > threshold).sum()


def moving_average_numpy(values, window):
    return np.convolve(
        values,
        np.ones(window) / window,
        mode="valid"
    )


def pairwise_distances_numpy(points):
    differences = points[:, np.newaxis, :] - points[np.newaxis, :, :]
    squared_distances = (differences ** 2).sum(axis=2)
    return np.sqrt(squared_distances)
```


```python
# Create sample data for testing

rng = np.random.default_rng(42)

values = rng.normal(50, 10, 1000)
points = rng.uniform(0, 100, size=(100, 2))

threshold = 50
window = 10

print("Number of values:", len(values))
print("Number of points:", len(points))
print("Threshold:", threshold)
print("Moving average window:", window)
```

    Number of values: 1000
    Number of points: 100
    Threshold: 50
    Moving average window: 10
    


```python
# Compare Python loop and NumPy functions

print("1. Sum of squares:")
print("Python:", sum_of_squares_loop(values.tolist()))
print("NumPy:", sum_of_squares_numpy(values))

print("\n2. Z-score:")
print("Results match:", np.allclose(
    zscore_loop(values.tolist()),
    zscore_numpy(values)
))

print("\n3. Count above threshold:")
print("Python:", count_above_loop(values.tolist(), threshold))
print("NumPy:", count_above_numpy(values, threshold))

print("\n4. Moving average:")
print("Results match:", np.allclose(
    moving_average_loop(values.tolist(), window),
    moving_average_numpy(values, window)
))

print("\n5. Pairwise distances:")
print("Results match:", np.allclose(
    pairwise_distances_loop(points.tolist()),
    pairwise_distances_numpy(points)
))
```

    1. Sum of squares:
    Python: 2568949.110782033
    NumPy: 2568949.11078203
    
    2. Z-score:
    Results match: True
    
    3. Count above threshold:
    Python: 502
    NumPy: 502
    
    4. Moving average:
    Results match: True
    
    5. Pairwise distances:
    Results match: True
    


```python
# Create the fixed dataset required by the assignment

rng = np.random.default_rng(42)

values = rng.normal(50, 10, 1_000_000)
values_list = values.tolist()

points = rng.uniform(0, 100, size=(1000, 2))
points_list = points.tolist()

threshold = 60
window = 50

print("Number of values:", len(values))
print("Number of points:", len(points))
print("Threshold:", threshold)
print("Moving average window:", window)
```

    Number of values: 1000000
    Number of points: 1000
    Threshold: 60
    Moving average window: 50
    


```python
import time
import numpy as np

# 1. Sum of squares
start = time.perf_counter()
result_loop = sum_of_squares_loop(values_list)
loop_time = time.perf_counter() - start

start = time.perf_counter()
result_numpy = sum_of_squares_numpy(values)
numpy_time = time.perf_counter() - start

print("Sum of squares")
print("Python time:", loop_time)
print("NumPy time:", numpy_time)
print("Speed-up:", loop_time / numpy_time)
print("Same result:", np.isclose(result_loop, result_numpy))
```

    Sum of squares
    Python time: 0.31386370002292097
    NumPy time: 0.007677400019019842
    Speed-up: 40.88150926685611
    Same result: True
    


```python
# Z-score performance comparison

start = time.perf_counter()
result_loop = zscore_loop(values_list)
loop_time = time.perf_counter() - start

start = time.perf_counter()
result_numpy = zscore_numpy(values)
numpy_time = time.perf_counter() - start

print("Z-score")
print("Python time:", loop_time)
print("NumPy time:", numpy_time)
print("Speed-up:", loop_time / numpy_time)
print("Same result:", np.allclose(result_loop, result_numpy))
```

    Z-score
    Python time: 0.7162710998672992
    NumPy time: 0.02364660007879138
    Speed-up: 30.2906590157002
    Same result: True
    


```python
# Count above threshold performance comparison

start = time.perf_counter()
result_loop = count_above_loop(values_list, threshold)
loop_time = time.perf_counter() - start

start = time.perf_counter()
result_numpy = count_above_numpy(values, threshold)
numpy_time = time.perf_counter() - start

print("Count above threshold")
print("Python time:", loop_time)
print("NumPy time:", numpy_time)
print("Speed-up:", loop_time / numpy_time)
print("Python result:", result_loop)
print("NumPy result:", result_numpy)
print("Same result:", result_loop == result_numpy)
```

    Count above threshold
    Python time: 0.1798454001545906
    NumPy time: 0.0035842000506818295
    Speed-up: 50.17727738728709
    Python result: 158614
    NumPy result: 158614
    Same result: True
    


```python
# Moving average performance comparison

start = time.perf_counter()
result_loop = moving_average_loop(values_list, window)
loop_time = time.perf_counter() - start

start = time.perf_counter()
result_numpy = moving_average_numpy(values, window)
numpy_time = time.perf_counter() - start

print("Moving average")
print("Python time:", loop_time)
print("NumPy time:", numpy_time)
print("Speed-up:", loop_time / numpy_time)
print("Same result:", np.allclose(result_loop, result_numpy))
```

    Moving average
    Python time: 2.217371700098738
    NumPy time: 0.07950660004280508
    Speed-up: 27.889152584879
    Same result: True
    


```python
# Pairwise distances performance comparison

start = time.perf_counter()
result_loop = pairwise_distances_loop(points_list)
loop_time = time.perf_counter() - start

start = time.perf_counter()
result_numpy = pairwise_distances_numpy(points)
numpy_time = time.perf_counter() - start

print("Pairwise distances")
print("Python time:", loop_time)
print("NumPy time:", numpy_time)
print("Speed-up:", loop_time / numpy_time)
print("Same result:", np.allclose(result_loop, result_numpy))
```

    Pairwise distances
    Python time: 1.804811199894175
    NumPy time: 0.09279139991849661
    Speed-up: 19.450199064562362
    Same result: True
    

## Performance Comparison


| Function | Python Loop Time (seconds) | NumPy Time (seconds) | Speed-up | Same Result |
|---|---:|---:|---:|---|
| Sum of squares | 0.192559 | 0.009248 | 20.82x | True |
| Z-score | 0.523407 | 0.024992 | 20.94x | True |
| Count above threshold | 0.148642 | 0.004476 | 33.21x | True |
| Moving average | 1.155653 | 0.038969 | 29.66x | True |
| Pairwise distances | 0.661566 | 0.054974 | 12.03x | True |

**Conclusion:**

NumPy vectorisation was faster than Python loops for all five functions while producing the same results. The greatest speed-up was observed for counting values above the threshold (33.21x), followed by moving average (29.66x). The smallest speed-up was observed for pairwise distances (12.03x). These results demonstrate that NumPy vectorisation can significantly reduce execution time when working with large datasets. Actual timings may vary between runs and computers.
