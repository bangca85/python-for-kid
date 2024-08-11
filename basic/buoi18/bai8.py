'''
Bài tập 8: Tính điểm trung bình của học sinh

**Yêu cầu:** Viết chương trình tính điểm trung bình của một học sinh với điểm của các môn học được lưu trữ trong dictionary.

**Input:**

```python
grades = {"Math": 85, "Science": 90, "English": 78}
```

**Output:**

```python
Điểm trung bình: 84.33
```
'''
def calculate_average(grades):
    total = sum(grades.values())
    count = len(grades)
    return total / count

grades = {"Math": 85, "Science": 90, "English": 78}
average = calculate_average(grades)
print(f"Điểm trung bình: {average:.2f}")
