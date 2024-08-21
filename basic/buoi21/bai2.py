'''
Bài tập 2: Quản lý từ điển sản phẩm

#### Yêu cầu:

1. Tạo một từ điển lưu trữ thông tin sản phẩm, bao gồm tên sản phẩm và giá cả.
2. Cho phép người dùng thêm một sản phẩm mới vào từ điển.
3. Tìm và in ra sản phẩm có giá cao nhất.
4. In ra tất cả các sản phẩm có giá dưới một mức cho trước.

#### Ví dụ:


# Input: {"Sản phẩm A": 100, "Sản phẩm B": 200, "Sản phẩm C": 150}
# Output:
# Sản phẩm có giá cao nhất: Sản phẩm B - 200
# Sản phẩm có giá dưới 180: {"Sản phẩm A": 100, "Sản phẩm C": 150}

'''

# 1. Tạo từ điển lưu trữ thông tin sản phẩm
products = {"Sản phẩm A": 100, "Sản phẩm B": 200, "Sản phẩm C": 150}

# 2. Cho phép người dùng thêm sản phẩm mới vào từ điển
product_name = input("Nhập tên sản phẩm mới: ")
product_price = int(input("Nhập giá sản phẩm: "))
products[product_name] = product_price

# 3. Tìm và in ra sản phẩm có giá cao nhất
max_price_product = None
max_price = float('-inf')
for product, price in products.items():
    if price > max_price:
        max_price = price
        max_price_product = product
print(f"Sản phẩm có giá cao nhất: {max_price_product} - {max_price}")

# 4. In ra tất cả các sản phẩm có giá dưới mức cho trước
limit = int(input("Nhập mức giá: "))
filtered_products = {}
for product, price in products.items():
    if price < limit:
        filtered_products[product] = price
print(f"Sản phẩm có giá dưới {limit}: {filtered_products}")
