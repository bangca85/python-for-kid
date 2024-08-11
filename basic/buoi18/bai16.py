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

def merge_dictionaries(dict1, dict2):
    merged_dict = {} 
    
    for key in dict1:
        merged_dict[key] = dict1[key]

    # Thêm tất cả các cặp key-value từ dict2 vào merged_dict
    # Nếu key đã tồn tại, giá trị của dict2 sẽ ghi đè giá trị của dict1
    for key in dict2:
        merged_dict[key] = dict2[key]

    return merged_dict


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = merge_dictionaries(dict1, dict2)
print(f"Dictionary sau khi gộp: {merged_dict}")
