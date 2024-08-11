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
    # nếu chăc chắn đầu vào thì không cần kiểm tra này
    # Kiểm tra xem tất cả các phần tử trong danh sách có phải là tuple và có đúng 2 phần tử không
    for item in list_of_tuples:
        # Hàm isinstance() tích hợp sẵn trong Python kiểm tra xem môt đối tượng (tham số thứ nhất) là một instance hay là một lớp con của Classinfo (tham số thứ hai).
        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError(f"Phần tử {item} không hợp lệ. Tất cả các phần tử phải là tuple với 2 phần tử.")

    return dict(list_of_tuples)

# Ví dụ sử dụng
list_of_tuples = [("name", "John"), ("age", 20), ("major", "Computer Science")]
dictionary = convert_to_dict(list_of_tuples)
print(f"Dictionary: {dictionary}")

