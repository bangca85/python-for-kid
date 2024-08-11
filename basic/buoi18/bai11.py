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
    # Hàm symmetric_difference để tìm các phần tử duy nhất có trong một trong hai tuple
    return tuple(set(tuple1).symmetric_difference(set(tuple2)))

def find_unique_elements_manual(tuple1, tuple2):
    unique_elements = []

    for item in tuple1:
        if item not in tuple2:
            unique_elements.append(item)

    for item in tuple2:
        if item not in tuple1:
            unique_elements.append(item)

    return tuple(unique_elements)


tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)

unique_elements = find_unique_elements(tuple1, tuple2)
print(f"Các phần tử duy nhất: {unique_elements}")
