'''

### Bài tập 1: Quản lý kho hàng

#### Yêu cầu:

1. Tạo một từ điển để lưu trữ thông tin sản phẩm trong kho, bao gồm tên sản phẩm, số lượng và giá mỗi đơn vị.
2. Viết chức năng cho phép thêm mới hoặc cập nhật sản phẩm trong kho (nếu sản phẩm đã tồn tại, chỉ cập nhật số lượng và giá).
3. Viết chức năng để tính tổng giá trị của kho hàng.
4. Viết chức năng để tìm và in ra sản phẩm có giá trị cao nhất trong kho (tính bằng giá mỗi đơn vị * số lượng).

#### Ví dụ:

```python
# Input: {"Sản phẩm A": {"số lượng": 10, "giá": 50}, "Sản phẩm B": {"số lượng": 5, "giá": 100}}
# Output:
# Cập nhật kho hàng: {"Sản phẩm A": {"số lượng": 10, "giá": 50}, "Sản phẩm B": {"số lượng": 8, "giá": 100}}
# Tổng giá trị kho hàng: 1600
# Sản phẩm có giá trị cao nhất: Sản phẩm B với giá trị 800
```
'''

# 1. Tạo một kho hàng ban đầu
inventory = {
    "Product A": {"quantity": 10, "price": 50},
    "Product B": {"quantity": 5, "price": 100}
}


# 2. Cấp nhật số lần và giá của sản phẩm trong kho
def update_product(inventory, product_name, quantity, price):
    if product_name in inventory:
        # Nếu sản phẩm đã tồn tại, cập nhật số lượng và giá
        inventory[product_name]["quantity"] += quantity
        inventory[product_name]["price"] = price
    else:
        # Nếu sản phẩm mới, thêm sản phẩm vào kho
        inventory[product_name] = {"quantity": quantity, "price": price}
    return inventory

# 3. Tổng giá trị kho hàng
def calculate_total_inventory_value(inventory):
    total_value = 0
    for product, details in inventory.items():
        total_value += details["quantity"] * details["price"]
    return total_value

# 4. Tìm và in ra sản phẩm có giá trị cao nhất
def find_most_valuable_product(inventory):
    most_valuable_product = None
    max_value = 0
    for product, details in inventory.items():
        value = details["quantity"] * details["price"]
        if value > max_value:
            max_value = value
            most_valuable_product = product
    return most_valuable_product, max_value


# chạy chương trình chính
# Cập nhật kho hàng
inventory = update_product(inventory, "Product B", 3, 100)
inventory = update_product(inventory, "Product C", 7, 150)
print("Cập nhật kho hàng:", inventory)

# Tính tổng giá trị kho hàng
total_value = calculate_total_inventory_value(inventory)
print("Tổng giá trị kho hàng:", total_value)

# Tìm sản phẩm có giá trị cao nhất
most_valuable_product, max_value = find_most_valuable_product(inventory)
print(f"Sản phẩm có giá trị cao nhất: {most_valuable_product} với giá trị {max_value}")