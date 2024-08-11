'''
#### Bài tập 3: Tìm các phần tử chung của hai tuple

**Yêu cầu:** Viết chương trình tìm các phần tử chung của hai tuple.

**Input:**

```python
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
```

**Output:**

```python
Các phần tử chung là: (4, 5)
```
'''

def find_common_elements(tuple1, tuple2):
    # chuyển tuple1, tuple2 thành set (tập hơp), sau đó dùng intersection nối hai tập hơp
    return tuple(set(tuple1).intersection(set(tuple2)))

def find_common_elements(tuple1, tuple2):
    common_elements = [] 

    for item in tuple1:
        if item in tuple2: 
            common_elements.append(item) 
    return tuple(common_elements) 


tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

common_elements = find_common_elements(tuple1, tuple2)
print(f"Các phần tử chung là: {common_elements}")
