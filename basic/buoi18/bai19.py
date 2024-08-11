'''
Bài tập 19: Tính tổng giá trị của các phần tử trong danh sách tuple

**Yêu cầu:** Viết chương trình tính tổng giá trị của các phần tử trong danh sách các tuple chứa số nguyên.

**Input:**

```python
tuples = [(1, 2), (3, 4), (5, 6)]
```

**Output:**

```python
Tổng giá trị: 21
```
'''
def sum_of_tuple_elements(tuples):
    return sum(sum(t) for t in tuples)

def sum_of_tuple_elements_simple(tuples):
    total = 0  
    for t in tuples:
        for num in t:
            total += num
    return total


tuples = [(1, 2), (3, 4), (5, 6)]
total_sum = sum_of_tuple_elements(tuples)
print(f"Tổng giá trị: {total_sum}")
