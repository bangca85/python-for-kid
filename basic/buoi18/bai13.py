'''
Bài tập 13: Tính tổng các giá trị trong dictionary

**Yêu cầu:** Viết chương trình tính tổng các giá trị trong một dictionary.

**Input:**

```python
data = {"a": 10, "b": 20, "c": 30}
```

**Output:**

```python
Tổng các giá trị: 60
```
'''
def sum_dict_values(data):
    return sum(data.values())

data = {"a": 10, "b": 20, "c": 30}
total = sum_dict_values(data)
print(f"Tổng các giá trị: {total}")
