'''
 Bài tập 18: Tạo danh sách các tuple từ dictionary

**Yêu cầu:** Viết chương trình tạo danh sách các tuple từ một dictionary.

**Input:**

```python
data = {"name": "John", "age": 20, "major": "Computer Science"}
```

**Output:**

```python
Danh sách các tuple: [('name', 'John'), ('age', 20), ('major', 'Computer Science')]
```

'''
def dict_to_list_of_tuples(data):
    return list(data.items())

data = {"name": "John", "age": 20, "major": "Computer Science"}
list_of_tuples = dict_to_list_of_tuples(data)
print(f"Danh sách các tuple: {list_of_tuples}")
