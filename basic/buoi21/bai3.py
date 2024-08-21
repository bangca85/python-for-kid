'''
Bài tập 3: Xử lý dữ liệu về nhân viên

#### Yêu cầu:

1. Nhập danh sách các nhân viên bao gồm tên và tuổi từ bàn phím.
2. Tính và in ra độ tuổi trung bình của các nhân viên.
3. Tìm và in ra nhân viên có độ tuổi lớn nhất và nhỏ nhất.
4. Sắp xếp danh sách nhân viên theo tuổi và in ra danh sách này.

#### Ví dụ:

# Input: {"John": 28, "Alice": 34, "Bob": 25}
# Output:
# Độ tuổi trung bình: 29
# Nhân viên trẻ nhất: Bob - 25
# Nhân viên lớn tuổi nhất: Alice - 34
# Danh sách sắp xếp: {"Bob": 25, "John": 28, "Alice": 34}
'''
# 1. Nhập danh sách các nhân viên bao gồm tên và tuổi từ bàn phím
employees = {}
while True:
    name = input("Nhập tên nhân viên (hoặc 'done' để kết thúc): ")
    if name == "done":
        break
    age = int(input("Nhập tuổi: "))
    employees[name] = age

# 2. Tính và in ra độ tuổi trung bình của các nhân viên
total_age = 0
for age in employees.values():
    total_age += age
average_age = total_age / len(employees)
print(f"Độ tuổi trung bình: {average_age:.1f}")

# 3. Tìm và in ra nhân viên có độ tuổi lớn nhất và nhỏ nhất

# cách đơn giản là dùng max and min
#oldest_employee = max(employees, key=employees.get)
#youngest_employee = min(employees, key=employees.get)
oldest_employee = None
youngest_employee = None
max_age = float('-inf')
min_age = float('inf')

for name, age in employees.items():
    if age > max_age:
        max_age = age
        oldest_employee = name
    if age < min_age:
        min_age = age
        youngest_employee = name

print(f"Nhân viên trẻ nhất: {youngest_employee} - {min_age}")
print(f"Nhân viên lớn tuổi nhất: {oldest_employee} - {max_age}")

# 4. Sắp xếp danh sách nhân viên theo tuổi và in ra danh sách này
sorted_employees = {}
while employees:
    min_name = None
    min_age = float('inf')
    for name, age in employees.items():
        if age < min_age:
            min_age = age
            min_name = name
    sorted_employees[min_name] = min_age
    del employees[min_name]

print(f"Danh sách sắp xếp: {sorted_employees}")
