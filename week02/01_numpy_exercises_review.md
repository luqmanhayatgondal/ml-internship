```python
import numpy as np

numbers = np.arange(1, 21)

print(numbers)
matrix = numbers.reshape(5, 4)

print(matrix)

print(matrix.shape)
```

    [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]
    [[ 1  2  3  4]
     [ 5  6  7  8]
     [ 9 10 11 12]
     [13 14 15 16]
     [17 18 19 20]]
    (5, 4)
    


```python
print("Dimensions:", matrix.ndim)
print("Total elements:", matrix.size)
print("Data type:", matrix.dtype)
```

    Dimensions: 2
    Total elements: 20
    Data type: int64
    


```python
middle = matrix[1:4, 1:3]

print(middle)
```

    [[ 6  7]
     [10 11]
     [14 15]]
    


```python
filtered = matrix[(matrix > 10) & (matrix % 3 == 0)]

print(filtered)
```

    [12 15 18]
    


```python
result = np.where(matrix % 2 != 0, -1, matrix)

print(result)
```

    [[-1  2 -1  4]
     [-1  6 -1  8]
     [-1 10 -1 12]
     [-1 14 -1 16]
     [-1 18 -1 20]]
    


```python
row_sum = matrix.sum(axis=1)
column_mean = matrix.mean(axis=0)

print("Row sums:", row_sum)
print("Column means:", column_mean)
```

    Row sums: [10 26 42 58 74]
    Column means: [ 9. 10. 11. 12.]
    


```python
column_means = matrix.mean(axis=0)

centered = matrix - column_means

print(centered)
```

    [[-8. -8. -8. -8.]
     [-4. -4. -4. -4.]
     [ 0.  0.  0.  0.]
     [ 4.  4.  4.  4.]
     [ 8.  8.  8.  8.]]
    


```python
a = np.arange(1, 10)
b = np.arange(1, 10)

table = a.reshape(9, 1) * b.reshape(1, 9)

print(table)
```

    [[ 1  2  3  4  5  6  7  8  9]
     [ 2  4  6  8 10 12 14 16 18]
     [ 3  6  9 12 15 18 21 24 27]
     [ 4  8 12 16 20 24 28 32 36]
     [ 5 10 15 20 25 30 35 40 45]
     [ 6 12 18 24 30 36 42 48 54]
     [ 7 14 21 28 35 42 49 56 63]
     [ 8 16 24 32 40 48 56 64 72]
     [ 9 18 27 36 45 54 63 72 81]]
    


```python
# Exercise 10: View vs Copy

demo_matrix = matrix.copy()

view = demo_matrix[0:2, 0:2]
copy_array = demo_matrix[0:2, 0:2].copy()

view[0, 0] = 999
copy_array[0, 1] = 888

print("Original demo matrix:")
print(demo_matrix)

print("View:")
print(view)

print("Copy:")
print(copy_array)
```

    Original demo matrix:
    [[999   2   3   4]
     [  5   6   7   8]
     [  9  10  11  12]
     [ 13  14  15  16]
     [ 17  18  19  20]]
    View:
    [[999   2]
     [  5   6]]
    Copy:
    [[  1 888]
     [  5   6]]
    


```python

```
