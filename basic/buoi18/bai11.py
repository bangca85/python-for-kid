'''
Bài tập 11: Tìm các phần tử không xuất hiện trong cả hai tuple

**Yêu cầu:** Viết chương trình tìm các phần tử không xuất hiện trong cả hai tuple.

**Input:**

```python
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)
```

**Output:**

```python
Các phần tử duy nhất: (1, 2, 5, 6)
```
'''
def find_unique_elements(tuple1, tuple2):
    return tuple(set(tuple1).symmetric_difference(set(tuple2)))

tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)

unique_elements = find_unique_elements(tuple1, tuple2)
print(f"Các phần tử duy nhất: {unique_elements}")
