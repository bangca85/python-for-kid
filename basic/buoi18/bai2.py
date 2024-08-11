'''
#### Bài tập 2: Tìm phần tử lớn thứ hai trong tuple

**Yêu cầu:** Viết chương trình tìm phần tử lớn thứ hai trong một tuple các số nguyên.

**Input:**

```python
numbers = (5, 3, 9, 1, 10, 6, 8, 4, 7, 2)
```

**Output:**

```python
Phần tử lớn thứ hai là: 9
```
'''
def find_second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2]

numbers = (5, 3, 9, 1, 10, 6, 8, 4, 7, 2)
second_largest = find_second_largest(numbers)
print(f"Phần tử lớn thứ hai là: {second_largest}")
