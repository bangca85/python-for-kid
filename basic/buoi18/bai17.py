'''
Bài tập 17: Sắp xếp dictionary theo giá trị

**Yêu cầu:** Viết chương trình sắp xếp dictionary theo giá trị.

**Input:**

```python
data = {"a": 3, "b": 1, "c": 2}
```

**Output:**

```python
Dictionary sau khi sắp xếp: {'b': 1, 'c': 2, 'a': 3}
```
'''
def sort_dict_by_value(data):
    # Tham số key=lambda item: item[1] chỉ định rằng quá trình sắp xếp sẽ dựa trên phần tử thứ hai của mỗi cặp (key, value) (tức là giá trị của từ điển).
    return dict(sorted(data.items(), key=lambda item: item[1]))

def sort_dict_by_value_manual(data):
    # Chuyển đổi từ điển thành danh sách các cặp (key, value)
    items = list(data.items())

    # Sắp xếp danh sách các cặp (key, value) theo giá trị
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i][1] > items[j][1]: 
                items[i], items[j] = items[j], items[i] 

    sorted_dict = {}
    for key, value in items:
        sorted_dict[key] = value

    return sorted_dict

data = {"a": 3, "b": 1, "c": 2}
sorted_data = sort_dict_by_value(data)
print(f"Dictionary sau khi sắp xếp: {sorted_data}")
