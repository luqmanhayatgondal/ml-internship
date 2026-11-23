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
    Python loop time: 0.021825075149536133
    NumPy vectorised time: 0.006590127944946289
    First 10 Python results: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    First 10 NumPy results: [  1   4   9  16  25  36  49  64  81 100]
    
