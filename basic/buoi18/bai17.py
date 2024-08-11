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
    return dict(sorted(data.items(), key=lambda item: item[1]))

data = {"a": 3, "b": 1, "c": 2}
sorted_data = sort_dict_by_value(data)
print(f"Dictionary sau khi sắp xếp: {sorted_data}")
