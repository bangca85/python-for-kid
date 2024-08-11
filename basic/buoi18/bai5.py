'''
Bài tập 5: Ghép các phần tử của hai tuple thành các cặp

**Yêu cầu:** Viết chương trình ghép các phần tử của hai tuple thành các cặp.

**Input:**

```python
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
```

**Output:**

```python
Các cặp phần tử: ((1, 'a'), (2, 'b'), (3, 'c'))
```
'''
def pair_elements(tuple1, tuple2):
    #Hàm zip() nhận vào hai hoặc nhiều iterable (ở đây là các tuple) và kết hợp các phần tử tương ứng từ mỗi iterable lại thành một tuple mới.
    return tuple(zip(tuple1, tuple2))

def pair_elements(tuple1, tuple2):
    paired_elements = []  
    length = min(len(tuple1), len(tuple2)) 

    for i in range(length): 
        paired_elements.append((tuple1[i], tuple2[i])) 

    return tuple(paired_elements) 


tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')

paired_elements = pair_elements(tuple1, tuple2)
print(f"Các cặp phần tử: {paired_elements}")
