'''

#### Bài tập 4: Đảo ngược tuple

**Yêu cầu:** Viết chương trình đảo ngược thứ tự các phần tử trong một tuple.

**Input:**

```python
numbers = (1, 2, 3, 4, 5)
```

**Output:**

```python
Tuple sau khi đảo ngược: (5, 4, 3, 2, 1)
```
'''

def reverse_tuple(t):
    return t[::-1]

numbers = (1, 2, 3, 4, 5)
reversed_numbers = reverse_tuple(numbers)
print(f"Tuple sau khi đảo ngược: {reversed_numbers}")
