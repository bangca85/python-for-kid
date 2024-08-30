### Bài số 1:
'''
#### Bài tập 1: Quản lý danh sách mua sắm (20 điểm)

1. Tạo một danh sách các món đồ cần mua.
2. Thêm một món đồ mới vào danh sách.
3. Xóa món đồ cuối cùng trong danh sách.
4. Tính tổng số món đồ trong danh sách.

**Ví dụ**:
- **Input ban đầu**: `["sữa", "bánh mì", "trứng"]`
- **Thêm món đồ mới**: `"nước ngọt"`
- **Output sau khi thêm**: `["sữa", "bánh mì", "trứng", "nước ngọt"]`
- **Output sau khi xóa món cuối**: `["sữa", "bánh mì", "trứng"]`
- **Tổng số món đồ**: `3`
'''
# 1. Tạo một danh sách các món đồ cần mua
shopping_list = ["sữa", "bánh mì", "trứng"]

# 2. Thêm một món đồ mới vào danh sách
new_item = "nước ngọt"
shopping_list.append(new_item)
print(f"Danh sách sau khi thêm: {shopping_list}")

# 3. Xóa món đồ cuối cùng trong danh sách
shopping_list.pop()
print(f"Danh sách sau khi xóa món cuối: {shopping_list}")

# 4. Tính tổng số món đồ trong danh sách
total_items = len(shopping_list)
print(f"Tổng số món đồ: {total_items}")


#########################
'''
#### Bài tập 2: Phân tích điểm số học sinh (25 điểm)
1. Tạo một từ điển lưu trữ tên học sinh và điểm số của họ.
2. Tính điểm trung bình của mỗi học sinh.
3. Tìm học sinh có điểm trung bình cao nhất.
4. Sắp xếp danh sách học sinh theo điểm trung bình từ cao đến thấp.

**Ví dụ**:
- **Input ban đầu**: `{"John": 85, "Alice": 90, "Bob": 78}`
- **Output điểm trung bình**: `{"John": 85.0, "Alice": 90.0, "Bob": 78.0}`
- **Học sinh có điểm trung bình cao nhất**: `"Alice"`
- **Danh sách sắp xếp**: `[("Alice", 90), ("John", 85), ("Bob", 78)]`
'''
# 1. Tạo một từ điển lưu trữ tên học sinh và điểm số của họ
student_scores = {"John": 85, "Alice": 90, "Bob": 78}

# 2. Tính điểm trung bình của mỗi học sinh
average_scores = {}
for student, score in student_scores.items():
    average_scores[student] = score

print(f"Điểm trung bình của mỗi học sinh: {average_scores}")

# 3. Tìm học sinh có điểm trung bình cao nhất
highest_student = max(average_scores, key=average_scores.get)
print(f"Học sinh có điểm trung bình cao nhất: {highest_student}")

# 4. Sắp xếp danh sách học sinh theo điểm trung bình từ cao đến thấp (chỉ dùng vòng lặp for)
sorted_students = list(average_scores.items())

# Sắp xếp thủ công bằng cách sử dụng vòng lặp for
for i in range(len(sorted_students)):
    for j in range(i + 1, len(sorted_students)):
        if sorted_students[i][1] < sorted_students[j][1]:
            sorted_students[i], sorted_students[j] = sorted_students[j], sorted_students[i]

print(f"Danh sách sắp xếp: {sorted_students}")

################################
'''
#### Bài tập 3: Xử lý dữ liệu đơn hàng (25 điểm)
1. Nhập vào danh sách các đơn hàng, mỗi đơn hàng bao gồm tên sản phẩm, số lượng và giá.
2. Tính tổng giá trị của tất cả các đơn hàng.
3. Tìm sản phẩm có tổng giá trị cao nhất.
4. Sắp xếp danh sách các đơn hàng theo giá trị từ cao đến thấp.
**Ví dụ**:
- **Input ban đầu**: `[("Laptop", 2, 1000), ("Phone", 3, 600), ("Tablet", 1, 300)]`
- **Tổng giá trị đơn hàng**: `4500`
- **Sản phẩm có giá trị cao nhất**: `"Laptop"`
- **Danh sách sắp xếp**: `[("Laptop", 2000), ("Phone", 1800), ("Tablet", 300)]`

'''

# 1. Nhập vào danh sách các đơn hàng
orders = [("Laptop", 2, 1000), ("Phone", 3, 600), ("Tablet", 1, 300)]

# 2. Tính tổng giá trị của tất cả các đơn hàng
total_value = 0
for product, quantity, price in orders:
    total_value += quantity * price
print(f"Tổng giá trị đơn hàng: {total_value}")

# 3. Tìm sản phẩm có tổng giá trị cao nhất
max_value = 0
max_product = ""
for product, quantity, price in orders:
    value = quantity * price
    if value > max_value:
        max_value = value
        max_product = product
print(f"Sản phẩm có giá trị cao nhất: {max_product}")

# 4. Sắp xếp danh sách các đơn hàng theo giá trị từ cao đến thấp
sorted_orders = []
for i in range(len(orders)):
    for j in range(i + 1, len(orders)):
        if orders[i][1] * orders[i][2] < orders[j][1] * orders[j][2]:
            orders[i], orders[j] = orders[j], orders[i]

print(f"Danh sách sắp xếp: {[(order[0], order[1] * order[2]) for order in orders]}")


