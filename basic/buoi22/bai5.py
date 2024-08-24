'''
### Bài tập 5: Quản lý thông tin nhân viên

#### Yêu cầu:

1. Tạo một từ điển lưu trữ thông tin nhân viên, bao gồm tên, tuổi, phòng ban, và mức lương.
2. Viết chức năng để thêm mới hoặc cập nhật thông tin nhân viên.
3. Viết chức năng để tìm và in ra nhân viên có mức lương cao nhất và thấp nhất.
4. Viết chức năng để tính tổng lương mà công ty phải chi trả cho tất cả nhân viên.

#### Ví dụ:

```python
# Input: {"John": {"Tuổi": 30, "Phòng ban": "IT", "Lương": 1500}, "Alice": {"Tuổi": 28, "Phòng ban": "HR", "Lương": 1300}}
# Output:
# Thêm hoặc cập nhật thông tin nhân viên: {"John": {"Tuổi": 30, "Phòng ban": "IT", "Lương": 1500}, "Alice": {"Tuổi": 28, "Phòng ban": "HR", "Lương": 1400}}
# Nhân viên có mức lương cao nhất: John - 1500
# Nhân viên có mức lương thấp nhất: Alice - 1400
# Tổng lương của công ty: 2900
```

---
'''
# Tạo từ điển lưu trữ thông tin nhân viên
employees = {
    "John": {"Age": 30, "Department": "IT", "Salary": 1500},
    "Alice": {"Age": 28, "Department": "HR", "Salary": 1300}
}

# Chức năng để thêm mới hoặc cập nhật thông tin nhân viên
def add_or_update_employee(name, age, department, salary):
    employees[name] = {"Age": age, "Department": department, "Salary": salary}
    return employees

# Chức năng để tìm và trả về nhân viên có mức lương cao nhất và thấp nhất
def find_extreme_salaries():
    highest_employee = None
    lowest_employee = None
    highest_salary = float('-inf')
    lowest_salary = float('inf')

    for name, info in employees.items():
        if info["Salary"] > highest_salary:
            highest_salary = info["Salary"]
            highest_employee = name
        if info["Salary"] < lowest_salary:
            lowest_salary = info["Salary"]
            lowest_employee = name

    return highest_employee, highest_salary, lowest_employee, lowest_salary

# Chức năng để tính và trả về tổng lương mà công ty phải chi trả cho tất cả nhân viên
def calculate_total_salary():
    total_salary = 0
    for info in employees.values():
        total_salary += info["Salary"]
    return total_salary

# Chạy chương trình

# Thêm hoặc cập nhật thông tin nhân viên
updated_employees = add_or_update_employee("Alice", 28, "HR", 1400)
print(f"Thông tin nhân viên đã được thêm hoặc cập nhật: {updated_employees}")

# Tìm và in ra nhân viên có mức lương cao nhất và thấp nhất
highest_employee, highest_salary, lowest_employee, lowest_salary = find_extreme_salaries()
print(f"Nhân viên có mức lương cao nhất: {highest_employee} - {highest_salary}")
print(f"Nhân viên có mức lương thấp nhất: {lowest_employee} - {lowest_salary}")

# Tính và in ra tổng lương của công ty
total_salary = calculate_total_salary()
print(f"Tổng lương của công ty: {total_salary}")
