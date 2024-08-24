'''
 Bài tập 12: Quản lý dữ liệu học sinh

#### Yêu cầu:

1. Nhập vào danh sách các học sinh, mỗi học sinh bao gồm tên, lớp, và điểm số của từng môn học.
2. Viết chức năng để tính điểm trung bình của mỗi học sinh.
3. Viết chức năng để xếp hạng các học sinh dựa trên điểm trung bình từ cao đến thấp.
4. Viết chức năng để tìm và in ra học sinh có điểm trung bình cao nhất và thấp nhất trong mỗi lớp.

#### Ví dụ:

```python
# Input: [{"tên": "John", "lớp": "10A", "Toán": 85, "Lý": 78, "Hóa": 92}, {"tên": "Alice", "lớp": "10A", "Toán": 88, "Lý": 95, "Hóa": 80}]
# Output:
# Điểm trung bình của mỗi học sinh: {"John": 85.0, "Alice": 87.67}
# Xếp hạng học sinh: [{"tên": "Alice", "điểm trung bình": 87.67}, {"tên": "John", "điểm trung bình": 85.0}]
# Học sinh có điểm trung bình cao nhất lớp 10A: Alice
# Học sinh có điểm trung bình thấp nhất lớp 10A: John
```

---

'''

# 2. Hàm tính điểm trung bình của mỗi học sinh
def calculate_average_scores(students):
    averages = {}
    for student in students:
        total_score = 0
        subject_count = 0
        for key, value in student.items():
            if key not in ["tên", "lớp"]:
                total_score += value
                subject_count += 1
        average_score = total_score / subject_count
        averages[student["tên"]] = average_score
    return averages


# 3. Hàm xếp hạng học sinh dựa trên điểm trung bình
def rank_students(average_scores):
    ranked_students = []
    scores_items = list(average_scores.items())

    for i in range(len(scores_items)):
        for j in range(i + 1, len(scores_items)):
            if scores_items[i][1] < scores_items[j][1]:
                scores_items[i], scores_items[j] = scores_items[j], scores_items[i]

    for name, avg_score in scores_items:
        ranked_students.append({"tên": name, "điểm trung bình": avg_score})
    
    return ranked_students

# 4. Hàm tìm và in ra học sinh có điểm trung bình cao nhất và thấp nhất
def find_extreme_students_by_class(students, average_scores):
    classes = {}
    for student in students:
        class_name = student["lớp"]
        if class_name not in classes:
            classes[class_name] = []
        classes[class_name].append(student["tên"])

    highest_students = {}
    lowest_students = {}

    for class_name, student_names in classes.items():
        highest_student = student_names[0]
        lowest_student = student_names[0]

        for name in student_names:
            if average_scores[name] > average_scores[highest_student]:
                highest_student = name
            if average_scores[name] < average_scores[lowest_student]:
                lowest_student = name

        highest_students[class_name] = highest_student
        lowest_students[class_name] = lowest_student

    return highest_students, lowest_students

### Chương trình chính ###
# danh sách học sinh mẫu
students = [
    {"tên": "John", "lớp": "10A", "Toán": 85, "Lý": 78, "Hóa": 92},
    {"tên": "Alice", "lớp": "10A", "Toán": 88, "Lý": 95, "Hóa": 80},
    {"tên": "Bob", "lớp": "10B", "Toán": 70, "Lý": 65, "Hóa": 75},
    {"tên": "Eve", "lớp": "10B", "Toán": 90, "Lý": 85, "Hóa": 88}
]


average_scores = calculate_average_scores(students)
print("Điểm trung bình của mỗi học sinh:", average_scores)

ranked_students = rank_students(average_scores)
print("Xếp hạng học sinh:", ranked_students)

highest_students, lowest_students = find_extreme_students_by_class(students, average_scores)

for class_name in highest_students:
    print(f"Học sinh có điểm trung bình cao nhất lớp {class_name}: {highest_students[class_name]}")
    print(f"Học sinh có điểm trung bình thấp nhất lớp {class_name}: {lowest_students[class_name]}")
