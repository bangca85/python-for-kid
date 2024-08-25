'''
### Bài tập 13: Quản lý ngân sách chi tiêu cá nhân

#### Yêu cầu:

1. Tạo một từ điển để lưu trữ các hạng mục chi tiêu hàng tháng và số tiền đã chi tiêu cho mỗi hạng mục.
2. Viết chức năng để thêm hoặc cập nhật chi tiêu cho một hạng mục.
3. Viết chức năng để tính tổng số tiền đã chi tiêu trong tháng.
4. Viết chức năng để tìm và in ra hạng mục chi tiêu nhiều nhất và ít nhất.

#### Ví dụ:

```python
# Input: {"Ăn uống": 300, "Giải trí": 150, "Mua sắm": 200}
# Output:
# Cập nhật chi tiêu: {"Ăn uống": 300, "Giải trí": 150, "Mua sắm": 250}
# Tổng chi tiêu trong tháng: 700
# Hạng mục chi tiêu nhiều nhất: Ăn uống
# Hạng mục chi tiêu ít nhất: Giải trí
```

---
'''

# 2. Hàm để thêm hoặc cập nhật chi tiêu cho một hạng mục
def update_expense(expenses, category, amount):
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount
    return expenses

# 3. Hàm tính tổng số tiền chi tiêu trong  tháng
def total_expenses(expenses):
    total = 0
    for amount in expenses.values():
        total += amount
    return total

# 4. Tìm hạng mục chi tiêu nhiều nhất và ít nhất
def find_extreme_expenses(expenses):
    highest_category = None
    lowest_category = None
    highest_amount = float('-inf')
    lowest_amount = float('inf')

    for category, amount in expenses.items():
        if amount > highest_amount:
            highest_amount = amount
            highest_category = category
        if amount < lowest_amount:
            lowest_amount = amount
            lowest_category = category

    return highest_category, lowest_category


expenses = {"Ăn uống": 300, "Giải trí": 150, "Mua sắm": 200}
# Ví dụ cập nhật chi tiêu cho hạng mục "Mua sắm"
expenses = update_expense(expenses, "Mua sắm", 50)
print("Cập nhật chi tiêu:", expenses)

# Tính tổng chi tiêu trong tháng
total = total_expenses(expenses)
print("Tổng chi tiêu trong tháng:", total)

# Tìm hạng mục chi tiêu nhiều nhất và ít nhất
highest, lowest = find_extreme_expenses(expenses)
print(f"Hạng mục chi tiêu nhiều nhất: {highest}")
print(f"Hạng mục chi tiêu ít nhất: {lowest}")