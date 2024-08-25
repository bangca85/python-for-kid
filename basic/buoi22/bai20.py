'''
### Bài tập 20: Quản lý và phân tích danh sách đơn hàng

#### Yêu cầu:

1. Nhập vào danh sách các đơn hàng, mỗi đơn hàng bao gồm mã đơn hàng, tên sản phẩm, số lượng, giá tiền, và trạng thái đơn hàng (đã giao hoặc chưa giao).
2. Viết chức năng để tính tổng số lượng đơn hàng đã giao và chưa giao.
3. Viết chức năng để tính tổng doanh thu từ các đơn hàng đã giao.
4. Viết chức năng để tìm và in ra danh sách các đơn hàng chưa giao.

#### Ví dụ:

```python
# Input: [{"mã": "DH01", "sản phẩm": "Laptop", "số lượng": 1, "giá": 1000, "trạng thái": "Đã giao"}, {"mã": "DH02", "sản phẩm": "Phone", "số lượng": 2, "giá": 600, "trạng thái": "Chưa giao"}]
# Output:
# Tổng số đơn hàng đã giao: 1
# Tổng số đơn hàng chưa giao: 1
# Tổng doanh thu từ các đơn hàng đã giao: 1000
# Danh sách đơn hàng chưa giao: [{"mã": "DH02", "sản phẩm": "Phone", "số lượng": 2, "giá": 600, "trạng thái": "Chưa giao"}]
```

'''
# 1. Nhập vào danh sách các đơn hàng
orders = [
    {"mã": "DH01", "sản phẩm": "Laptop", "số lượng": 1, "giá": 1000, "trạng thái": "Đã giao"},
    {"mã": "DH02", "sản phẩm": "Phone", "số lượng": 2, "giá": 600, "trạng thái": "Chưa giao"},
    {"mã": "DH03", "sản phẩm": "Tablet", "số lượng": 3, "giá": 300, "trạng thái": "Đã giao"},
    {"mã": "DH04", "sản phẩm": "Monitor", "số lượng": 1, "giá": 200, "trạng thái": "Chưa giao"}
]

# 2. Chức năng tính tổng số lượng đơn hàng đã giao và chưa giao
def count_orders(orders):
    delivered_count = 0
    undelivered_count = 0
    for order in orders:
        if order["trạng thái"] == "Đã giao":
            delivered_count += 1
        elif order["trạng thái"] == "Chưa giao":
            undelivered_count += 1
    return delivered_count, undelivered_count

# 3. Chức năng tính tổng doanh thu từ các đơn hàng đã giao
def calculate_total_revenue(orders):
    total_revenue = 0
    for order in orders:
        if order["trạng thái"] == "Đã giao":
            total_revenue += order["số lượng"] * order["giá"]
    return total_revenue

# 4. Chức năng tìm danh sách các đơn hàng chưa giao
def find_undelivered_orders(orders):
    undelivered_orders = []
    for order in orders:
        if order["trạng thái"] == "Chưa giao":
            undelivered_orders.append(order)
    return undelivered_orders

# Chạy các chức năng và in kết quả

# Tính tổng số lượng đơn hàng đã giao và chưa giao
delivered_count, undelivered_count = count_orders(orders)
print(f"Tổng số đơn hàng đã giao: {delivered_count}")
print(f"Tổng số đơn hàng chưa giao: {undelivered_count}")

# Tính tổng doanh thu từ các đơn hàng đã giao
total_revenue = calculate_total_revenue(orders)
print(f"Tổng doanh thu từ các đơn hàng đã giao: {total_revenue}")

# Tìm và in danh sách các đơn hàng chưa giao
undelivered_orders = find_undelivered_orders(orders)
print(f"Danh sách đơn hàng chưa giao: {undelivered_orders}")
