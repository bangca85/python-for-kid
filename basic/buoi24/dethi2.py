'''
Bài tập 1: Quản lý thời gian biểu cá nhân (20 điểm)
Tạo một danh sách lưu trữ các hoạt động trong ngày.
Thêm một hoạt động mới vào thời gian biểu.
Xóa một hoạt động khỏi thời gian biểu.
Tính và in ra số lượng hoạt động trong thời gian biểu.
Ví dụ:

Input ban đầu: ["Thức dậy", "Ăn sáng", "Đi làm"]
Thêm hoạt động mới: "Học Python"
Output sau khi thêm: ["Thức dậy", "Ăn sáng", "Đi làm", "Học Python"]
Output sau khi xóa: ["Thức dậy", "Ăn sáng", "Học Python"]
Số lượng hoạt động: 3

'''
# 1. Tạo một danh sách lưu trữ các hoạt động trong ngày
schedule = ["Thức dậy", "Ăn sáng", "Đi làm"]

# 2. Thêm một hoạt động mới vào thời gian biểu
new_activity = "Học Python"
schedule.append(new_activity)
print(f"Thêm hoạt động mới: {schedule}")

# 3. Xóa một hoạt động khỏi thời gian biểu
activity_to_remove = "Đi làm"
if activity_to_remove in schedule:
    schedule.remove(activity_to_remove)
print(f"Thời gian biểu sau khi xóa: {schedule}")

# 4. Tính và in ra số lượng hoạt động trong thời gian biểu
activity_count = len(schedule)
print(f"Số lượng hoạt động: {activity_count}")


'''
Bài tập 2: Phân tích chi tiêu cá nhân (25 điểm)
Tạo một từ điển lưu trữ các hạng mục chi tiêu và số tiền đã chi tiêu cho mỗi hạng mục.
Tính tổng số tiền đã chi tiêu.
Tìm hạng mục chi tiêu lớn nhất.
Sắp xếp các hạng mục chi tiêu từ cao đến thấp.
Ví dụ:

Input ban đầu: {"Ăn uống": 300, "Giải trí": 150, "Mua sắm": 200}
Output tổng chi tiêu: 650
Hạng mục chi tiêu lớn nhất: "Ăn uống"
Danh sách sắp xếp: [("Ăn uống", 300), ("Mua sắm", 200), ("Giải trí", 150)]
'''
# 1. Tạo một từ điển lưu trữ các hạng mục chi tiêu và số tiền đã chi tiêu cho mỗi hạng mục
expenses = {
    "Ăn uống": 300,
    "Giải trí": 150,
    "Mua sắm": 200
}

# 2. Tính tổng số tiền đã chi tiêu
total_expense = sum(expenses.values())
print(f"Tổng chi tiêu: {total_expense}")

# 3. Tìm hạng mục chi tiêu lớn nhất
max_expense = max(expenses, key=expenses.get)
print(f"Hạng mục chi tiêu lớn nhất: {max_expense}")

# 4. Sắp xếp các hạng mục chi tiêu từ cao đến thấp
sorted_expenses = []
for category in sorted(expenses, key=expenses.get, reverse=True):
    sorted_expenses.append((category, expenses[category]))
print(f"Danh sách sắp xếp: {sorted_expenses}")


'''
---
#### Bài tập 3: Phân tích dữ liệu tiêu thụ điện năng (25 điểm)
1. Nhập vào danh sách các khu vực, mỗi khu vực bao gồm tên khu vực, số hộ dân, và mức tiêu thụ điện năng.
2. Tính tổng mức tiêu thụ điện năng của tất cả các khu vực.
3. Tìm khu vực có mức tiêu thụ điện năng cao nhất.
4. Sắp xếp danh sách các khu vực theo mức tiêu thụ điện năng từ cao đến thấp.
**Ví dụ**:
- **Input ban đầu**: `[{"khu vực": "Quận 1", "hộ dân": 10000, "điện năng": 5000}, {"khu vực": "Quận 2", "hộ dân": 8000, "điện năng": 4000}]`
- **Tổng mức tiêu thụ điện năng**: `9000`
- **Khu vực có mức tiêu thụ điện năng cao nhất**: `"Quận 1"`
- **Danh sách sắp xếp**: `[{"Quận 1": 5000}, {"Quận 2": 4000}]`
'''
# 1. Nhập vào danh sách các khu vực, mỗi khu vực bao gồm tên khu vực, số hộ dân, và mức tiêu thụ điện năng
areas = [
    {"khu vực": "Quận 1", "hộ dân": 10000, "điện năng": 5000},
    {"khu vực": "Quận 2", "hộ dân": 8000, "điện năng": 4000}
]

# 2. Tính tổng mức tiêu thụ điện năng của tất cả các khu vực
total_consumption = 0
for area in areas:
    total_consumption += area["điện năng"]
print(f"Tổng mức tiêu thụ điện năng: {total_consumption}")

# 3. Tìm khu vực có mức tiêu thụ điện năng cao nhất
highest_consumption_area = None
highest_consumption = 0
for area in areas:
    if area["điện năng"] > highest_consumption:
        highest_consumption = area["điện năng"]
        highest_consumption_area = area["khu vực"]
print(f"Khu vực có mức tiêu thụ điện năng cao nhất: {highest_consumption_area}")

# 4. Sắp xếp danh sách các khu vực theo mức tiêu thụ điện năng từ cao đến thấp
sorted_areas = []
for i in range(len(areas)):
    for j in range(i + 1, len(areas)):
        if areas[i]["điện năng"] < areas[j]["điện năng"]:
            areas[i], areas[j] = areas[j], areas[i]
for area in areas:
    sorted_areas.append({area["khu vực"]: area["điện năng"]})
print(f"Danh sách sắp xếp: {sorted_areas}")
