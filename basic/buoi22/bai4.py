'''
### Bài tập 4: Quản lý danh sách học sinh và điểm số nâng cao

#### Yêu cầu:

1. Tạo một từ điển lưu trữ danh sách học sinh và danh sách điểm số của họ cho từng môn học.
2. Viết chức năng để tính điểm trung bình của mỗi học sinh.
3. Viết chức năng để xếp hạng các học sinh dựa trên điểm trung bình từ cao đến thấp.
4. Viết chức năng để tìm học sinh có điểm trung bình cao nhất và thấp nhất.

#### Ví dụ:

```python
# Input: {"John": {"Toán": 85, "Lý": 78, "Hóa": 92}, "Alice": {"Toán": 88, "Lý": 95, "Hóa": 80}}
# Output:
# Điểm trung bình của mỗi học sinh: {"John": 85.0, "Alice": 87.67}
# Xếp hạng học sinh: [("Alice", 87.67), ("John", 85.0)]
# Học sinh có điểm trung bình cao nhất: Alice
# Học sinh có điểm trung bình thấp nhất: John
```
'''
# 2. Hàm tính điểm trung bình của mooxi học sinh
def calculate_average_scores(students_scores):
    average_scores = {}
    for student, scores in students_scores.items():
        total_score = sum(scores.values())
        num_subjects = len(scores)
        average_scores[student] = round(total_score / num_subjects, 2)
    return average_scores

# 3. Hàm xếp hạng học sinh dựa trên điểm trung bình từ cao đến thấp
def rank_students(average_scores):
    ranked_students = list(average_scores.items())
    
    # Sử dụng vòng lặp for để sắp xếp danh sách học sinh dựa trên điểm trung bình
    for i in range(len(ranked_students)):
        for j in range(i + 1, len(ranked_students)):
            if ranked_students[i][1] < ranked_students[j][1]:
                # Đổi chỗ nếu học sinh sau có điểm cao hơn
                # Hoán đổi vị trí hai phần tử ranked_students[i] và ranked_students[j]
                temp = ranked_students[i]   # Lưu tạm giá trị của phần tử i
                ranked_students[i] = ranked_students[j]  # Gán giá trị của phần tử j cho i
                ranked_students[j] = temp  # Gán giá trị tạm của i cho phần tử j
    
    return ranked_students
# 4. Hàm tìm học sinh có điểm trung bình cao nhất và thấp nhất
def find_extreme_students(average_scores):
    highest_student = None
    lowest_student = None
    highest_score = float('-inf')
    lowest_score = float('inf')
    
    # Sử dụng vòng lặp for để tìm học sinh có điểm cao nhất và thấp nhất
    for student, score in average_scores.items():
        if score > highest_score:
            highest_score = score
            highest_student = student
        if score < lowest_score:
            lowest_score = score
            lowest_student = student
    
    return highest_student, lowest_student

# 1. Danh sách học sinh
students_scores = {
    "John": {"Toán": 85, "Lý": 78, "Học": 92},
    "Alice": {"Toán": 88, "Lý": 95, "Học": 80}
}

# Điểm trung bình của mỗi học sinh
average_scores = calculate_average_scores(students_scores)
print("Điểm trung bình của mỗi học sinh:", average_scores)

# Xếp hạng học sinh
ranked_students = rank_students(average_scores)
print("Xếp hạng học sinh:", ranked_students)

# Học sinh có điểm trung bình cao nhất và thấp nhất
highest_student, lowest_student = find_extreme_students(average_scores)
print(f"Học sinh có điểm trung bình cao nhất: {highest_student}")
print(f"Học sinh có điểm trung bình thấp nhất: {lowest_student}")