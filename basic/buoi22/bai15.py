'''
### Bài tập 15: Phân tích dữ liệu điểm thi đại học

#### Yêu cầu:

1. Nhập vào danh sách các thí sinh, mỗi thí sinh bao gồm tên, điểm của các môn thi.
2. Viết chức năng để tính điểm trung bình của mỗi thí sinh.
3. Viết chức năng để xếp hạng các thí sinh dựa trên điểm trung bình từ cao đến thấp.
4. Viết chức năng để tìm và in ra danh sách các thí sinh đủ điều kiện đỗ đại học (điểm trung bình >= 5.0).

#### Ví dụ:

```python
# Input: [{"tên": "John", "Toán": 7.0, "Lý": 8.0, "Hóa": 6.5}, {"tên": "Alice", "Toán": 4.5, "Lý": 5.5, "Hóa": 4.0}]
# Output:
# Điểm trung bình của mỗi thí sinh: {"John": 7.17, "Alice": 4.67}
# Xếp hạng thí sinh: [{"tên": "John", "điểm trung bình": 7.17}, {"tên": "Alice", "điểm trung bình": 4.67}]
# Thí sinh đủ điều kiện đỗ đại học: ["John"]
```

---

'''

# 2. Hàm tính điểm trung bình của mỗi thí sinh.
def calculate_average_scores(students):
    average_scores = {}
    for student in students:
        total_score = sum([score for subject, score in student.items() if subject != "tên"])
        average_score = total_score / (len(student) - 1)  # Trừ 1 để không tính tên
        average_scores[student["tên"]] = round(average_score, 2)
    return average_scores


# 3. Hàm xếp hạng các thí sinh dựa trên điểm trung bình từ cao đến thấp.
def rank_students(average_scores):
    ranked_students = []
    for student in sorted(average_scores, key=average_scores.get, reverse=True):
        ranked_students.append({"tên": student, "điểm trung bình": average_scores[student]})
    return ranked_students

# 4. Hàm tìm và in ra danh sách các thí sinh đủ điều kiện đỗ đại học (điểm trung bình >= 5.0).
def find_passing_students(average_scores):
    passing_students = []
    for student, score in average_scores.items():
        if score >= 5.0:
            passing_students.append(student)
    return passing_students

### Chương trình chính ####
students = [
    {"tên": "John", "Toán": 7.0, "Lý": 8.0, "Hóa": 6.5},
    {"tên": "Alice", "Toán": 4.5, "Lý": 5.5, "Hóa": 4.0}
]

average_scores = calculate_average_scores(students)
print("Điểm trung bình của mỗi thí sinh:", average_scores)
ranked_students = rank_students(average_scores)
print("Xếp hạng thí sinh:", ranked_students)
passing_students = find_passing_students(average_scores)
print("Thí sinh đủ điều kiện đỗ đại học:", passing_students)