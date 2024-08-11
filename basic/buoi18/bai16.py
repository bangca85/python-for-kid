'''
Bài tập 16: Gộp các dictionary

**Yêu cầu:** Viết chương trình gộp hai dictionary lại với nhau.

**Input:**

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
```

**Output:**

```python
Dictionary sau khi gộp: {'a': 1, 'b': 3, 'c': 4}
```
'''
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = merge_dictionaries(dict1, dict2)
print(f"Dictionary sau khi gộp: {merged_dict}")
