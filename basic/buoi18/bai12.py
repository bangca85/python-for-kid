'''
Bài tập 12: Lưu trữ và tra cứu thông tin học sinh

**Yêu cầu:** Viết chương trình lưu trữ thông tin học sinh và cho phép tra cứu thông tin theo tên.

**Input:**

```python
students = {
    "John": {"age": 20, "major": "Computer Science"},
    "Jane": {"age": 22, "major": "Mathematics"}
}
name = "John"
```

**Output:**

```python
Thông tin của John: {'age': 20, 'major': 'Computer Science'}
```
'''

def lookup_student_info(students, name):
    return students.get(name, "Không tìm thấy thông tin học sinh")

students = {
    "John": {"age": 20, "major": "Computer Science"},
    "Jane": {"age": 22, "major": "Mathematics"}
}
name = "John"
student_info = lookup_student_info(students, name)
print(f"Thông tin của {name}: {student_info}")
