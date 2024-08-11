'''
Bài tập 10: Chuyển đổi danh sách các tuple thành dictionary

**Yêu cầu:** Viết chương trình chuyển đổi danh sách các tuple thành một dictionary.

**Input:**

```python
list_of_tuples = [("name", "John"), ("age", 20), ("major", "Computer Science")]
```

**Output:**

```python
Dictionary: {'name': 'John', 'age': 20, 'major': 'Computer Science'}
```
'''
def convert_to_dict(list_of_tuples):
    return dict(list_of_tuples)

list_of_tuples = [("name", "John"), ("age", 20), ("major", "Computer Science")]
dictionary = convert_to_dict(list_of_tuples)
print(f"Dictionary: {dictionary}")
