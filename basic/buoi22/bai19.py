'''
### Bài tập 19: Phân tích kết quả học tập của sinh viên

#### Yêu cầu:

1. Tạo một từ điển lưu trữ kết quả học tập của sinh viên, mỗi sinh viên bao gồm các môn học và điểm số tương ứng.
2. Viết chức năng để tính điểm trung bình của mỗi sinh viên.
3. Viết chức năng để tìm và in ra sinh viên có điểm trung bình cao nhất và thấp nhất.
4. Viết chức năng để xác định và in ra những sinh viên có điểm trung bình dưới 5 (yếu).

#### Ví dụ:

```python
# Input: {"John": {"Toán": 4, "Lý": 6, "Hóa": 5}, "Alice": {"Toán": 8, "Lý": 7, "Hóa": 9}}
# Output:
# Điểm trung bình của mỗi sinh viên: {"John": 5.0, "Alice": 8.0}
# Sinh viên có điểm trung bình cao nhất: Alice
# Sinh viên có điểm trung bình thấp nhất: John
# Sinh viên có điểm trung bình dưới 5: ["John"]
```

---

'''
# 1. Tạo từ điển lưu trữ kết quả học tập của sinh viên
students = {
    "John": {"Toán": 4, "Lý": 6, "Hóa": 5},
    "Alice": {"Toán": 8, "Lý": 7, "Hóa": 9},
    "Bob": {"Toán": 3, "Lý": 4, "Hóa": 5}
}

# 2. Chức năng tính điểm trung bình của mỗi sinh viên
def calculate_average_scores(students):
    average_scores = {}
    for student, subjects in students.items():
        total_score = sum(subjects.values())
        subject_count = len(subjects)
        average_scores[student] = total_score / subject_count
    return average_scores

# 3. Chức năng tìm sinh viên có điểm trung bình cao nhất và thấp nhất
def find_extreme_students(average_scores):
    highest_student = max(average_scores, key=average_scores.get)
    lowest_student = min(average_scores, key=average_scores.get)
    return highest_student, lowest_student

# 4. Chức năng tìm sinh viên có điểm trung bình dưới 5
def find_weak_students(average_scores):
    weak_students = []
    for student, avg_score in average_scores.items():
        if avg_score < 5:
            weak_students.append(student)
    return weak_students

# Chạy các chức năng và in kết quả

# Tính điểm trung bình của mỗi sinh viên
average_scores = calculate_average_scores(students)
print(f"Điểm trung bình của mỗi sinh viên: {average_scores}")

# Tìm sinh viên có điểm trung bình cao nhất và thấp nhất
highest_student, lowest_student = find_extreme_students(average_scores)
print(f"Sinh viên có điểm trung bình cao nhất: {highest_student}")
print(f"Sinh viên có điểm trung bình thấp nhất: {lowest_student}")

# Tìm sinh viên có điểm trung bình dưới 5
weak_students = find_weak_students(average_scores)
print(f"Sinh viên có điểm trung bình dưới 5: {weak_students}")
