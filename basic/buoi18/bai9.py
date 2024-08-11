'''
Bài tập 9: Thêm và xóa khóa trong dictionary

**Yêu cầu:** Viết chương trình cho phép thêm và xóa khóa trong dictionary.

**Input:**

```python
grades = {"Math": 85, "Science": 90}
```

**Output:**

```python
Sau khi thêm môn English: {'Math': 85, 'Science': 90, 'English': 78}
Sau khi xóa môn Math: {'Science': 90, 'English': 78}
```

'''
def add_subject(grades, subject, score):
    grades[subject] = score
    return grades

def remove_subject(grades, subject):
    if subject in grades:
        del grades[subject]
    return grades

grades = {"Math": 85, "Science": 90}

grades = add_subject(grades, "English", 78)
print(f"Sau khi thêm môn English: {grades}")

grades = remove_subject(grades, "Math")
print(f"Sau khi xóa môn Math: {grades}")
