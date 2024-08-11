'''
 Bài tập 15: Lưu trữ và hiển thị điểm số của học sinh theo môn học

**Yêu cầu:** Viết chương trình lưu trữ điểm số của học sinh theo môn học và hiển thị thông tin này.

**Input:**

```python
students = {
    "John": {"Math": 85, "Science": 90},
    "Jane": {"Math": 92, "Science": 88}
}
```

**Output:**

```python
Điểm của John:
  Math: 85
  Science: 90
Điểm của Jane:
  Math: 92
  Science: 88
```
'''
def display_student_scores(students):
    for student, subjects in students.items():
        print(f"Điểm của {student}:")
        for subject, score in subjects.items():
            print(f"  {subject}: {score}")

students = {
    "John": {"Math": 85, "Science": 90},
    "Jane": {"Math": 92, "Science": 88}
}

display_student_scores(students)
