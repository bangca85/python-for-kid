'''
Bài tập 5: Quản lý danh sách học sinh và điểm số

#### Yêu cầu:

1. Tạo một từ điển lưu trữ danh sách học sinh và điểm số của họ.
2. Cho phép người dùng thêm một học sinh mới cùng với điểm số của họ.
3. Tìm và in ra học sinh có điểm số cao nhất.
4. Tính và in ra điểm trung bình của tất cả học sinh.

#### Ví dụ:

# Input: {"John": 85, "Alice": 92, "Bob": 78}
# Output:
# Điểm trung bình: 85
# Học sinh có điểm cao nhất: Alice - 92
# Danh sách học sinh và điểm số sau khi thêm: {"John": 85, "Alice": 92, "Bob": 78, "Mary": 88}
'''
# 1. Tạo một từ điển lưu trữ danh sách học sinh và điểm số của họ
students = {"John": 85, "Alice": 92, "Bob": 78}

# 2. Cho phép người dùng thêm một học sinh mới cùng với điểm số của họ
new_name = input("Nhập tên học sinh mới: ")
new_score = int(input("Nhập điểm số của học sinh: "))
students[new_name] = new_score

# 3. Tìm và in ra học sinh có điểm số cao nhất
top_student = max(students, key=students.get)
print(f"Học sinh có điểm cao nhất: {top_student} - {students[top_student]}")

# 4. Tính và in ra điểm trung bình của tất cả học sinh
average_score = sum(students.values()) / len(students)
print(f"Điểm trung bình: {average_score:.1f}")
