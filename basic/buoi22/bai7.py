'''
Bài tập 7: Quản lý và phân tích đơn hàng

#### Yêu cầu:

1. Nhập vào danh sách các đơn hàng, mỗi đơn hàng bao gồm mã đơn hàng, tên khách hàng, sản phẩm, số lượng và giá.
2. Viết chức năng để tính tổng doanh thu từ tất cả các đơn hàng.
3. Viết chức năng để tìm đơn hàng có giá trị cao nhất.
4. Viết chức năng để sắp xếp và in ra danh sách đơn hàng theo giá trị từ cao đến thấp.

#### Ví dụ:

```python
# Input: [{"mã": "A1", "khách hàng": "John", "sản phẩm": "Laptop", "số lượng": 1, "giá": 1000}, {"mã": "A2", "khách hàng": "Alice", "sản phẩm": "Phone", "số lượng": 2, "giá": 600}]
# Output:
# Tổng doanh thu: 2200
# Đơn hàng có giá trị cao nhất: A1 - 1000
# Danh sách đơn hàng sắp xếp: [{"mã": "A1", "khách hàng": "John", "sản phẩm": "Laptop", "số lượng": 1, "giá": 1000}, {"mã": "A2", "khách hàng": "Alice", "sản phẩm": "Phone", "số lượng": 2, "giá": 600}]
```

---
'''

# Chức năng để tính tổng doanh thu từ tất cả các đơn hàng
def calculate_total_revenue(orders):
    total_revenue = 0
    for order in orders:
        total_revenue += order["số lượng"] * order["giá"]
    return total_revenue

# Chức năng để tìm đơn hàng có giá trị cao nhất
def find_highest_value_order(orders):
    highest_order = None
    highest_value = float('-inf')
    
    for order in orders:
        order_value = order["số lượng"] * order["giá"]
        if order_value > highest_value:
            highest_value = order_value
            highest_order = order
    
    return highest_order

# Chức năng để sắp xếp và in ra danh sách đơn hàng theo giá trị từ cao đến thấp
def sort_orders_by_value(orders):
    for i in range(len(orders)):
        for j in range(i + 1, len(orders)):
            if orders[i]["số lượng"] * orders[i]["giá"] < orders[j]["số lượng"] * orders[j]["giá"]:
                orders[i], orders[j] = orders[j], orders[i]
    return orders

# Chạy chương trình với dữ liệu mẫu
orders = [
    {"mã": "A1", "khách hàng": "John", "sản phẩm": "Laptop", "số lượng": 1, "giá": 1000},
    {"mã": "A2", "khách hàng": "Alice", "sản phẩm": "Phone", "số lượng": 2, "giá": 600}
]

# Tính tổng doanh thu từ tất cả các đơn hàng
total_revenue = calculate_total_revenue(orders)
print(f"Tổng doanh thu: {total_revenue}")

# Tìm đơn hàng có giá trị cao nhất
highest_value_order = find_highest_value_order(orders)
print(f"Đơn hàng có giá trị cao nhất: {highest_value_order['mã']} - {highest_value_order['giá'] * highest_value_order['số lượng']}")

# Sắp xếp và in ra danh sách đơn hàng theo giá trị từ cao đến thấp
sorted_orders = sort_orders_by_value(orders)
print(f"Danh sách đơn hàng sắp xếp: {sorted_orders}")
