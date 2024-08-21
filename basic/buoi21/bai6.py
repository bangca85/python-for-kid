'''
Bài tập 6: Phân tích và xử lý dữ liệu sản phẩm

#### Yêu cầu:

1. Nhập vào danh sách sản phẩm và giá tương ứng từ bàn phím.
2. Tìm và in ra sản phẩm có giá thấp nhất và cao nhất.
3. Tính và in ra tổng giá trị của tất cả các sản phẩm.
4. Tạo và in ra một danh sách các sản phẩm có giá trên mức trung bình.

#### Ví dụ:

# Input: {"Sản phẩm A": 100, "Sản phẩm B": 150, "Sản phẩm C": 200}
# Output:
# Sản phẩm có giá thấp nhất: Sản phẩm A - 100
# Sản phẩm có giá cao nhất: Sản phẩm C - 200
# Tổng giá trị: 450
# Sản phẩm có giá trên mức trung bình: ["Sản phẩm B", "Sản phẩm C"]
'''
# 1. Nhập vào danh sách sản phẩm và giá tương ứng từ bàn phím
products = {}
while True:
    product = input("Nhập tên sản phẩm (hoặc 'done' để kết thúc): ")
    if product == "done":
        break
    price = int(input("Nhập giá sản phẩm: "))
    products[product] = price

# 2. Tìm và in ra sản phẩm có giá thấp nhất và cao nhất
min_price_product = min(products, key=products.get)
max_price_product = max(products, key=products.get)
print(f"Sản phẩm có giá thấp nhất: {min_price_product} - {products[min_price_product]}")
print(f"Sản phẩm có giá cao nhất: {max_price_product} - {products[max_price_product]}")

# 3. Tính và in ra tổng giá trị của tất cả các sản phẩm
total_value = sum(products.values())
print(f"Tổng giá trị: {total_value}")

# 4. Tạo và in ra một danh sách các sản phẩm có giá trên mức trung bình
average_price = total_value / len(products)

# Tạo danh sách các sản phẩm có giá trên mức trung bình
above_average_products = []
for product, price in products.items():
    if price > average_price:
        above_average_products.append(product)

# In ra các sản phẩm có giá trên mức trung bình
print(f"Sản phẩm có giá trên mức trung bình: {above_average_products}")
