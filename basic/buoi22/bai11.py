'''
Bài tập 11: Phân tích và xử lý dữ liệu bán hàng

#### Yêu cầu:

1. Nhập vào danh sách các giao dịch bán hàng, mỗi giao dịch bao gồm mã sản phẩm, số lượng bán, và giá bán.
2. Viết chức năng để tính tổng doanh thu từ tất cả các giao dịch.
3. Viết chức năng để tìm và in ra sản phẩm bán chạy nhất (sản phẩm có số lượng bán nhiều nhất).
4. Viết chức năng để sắp xếp và in ra danh sách sản phẩm theo tổng doanh thu từ cao đến thấp.

#### Ví dụ:

```python
# Input: [("SP01", 10, 100), ("SP02", 5, 200), ("SP01", 2, 100)]
# Output:
# Tổng doanh thu: 2400
# Sản phẩm bán chạy nhất: SP01
# Danh sách sản phẩm theo doanh thu: [("SP01", 1200), ("SP02", 1000)]
```

---
'''

# Chức năng tính tổng doanh thu từ tất cả các giao dịch
def calculate_total_revenue(transactions):
    total_revenue = 0
    
    for transaction in transactions:
        product_code = transaction[0]
        quantity = transaction[1]
        price = transaction[2]
        total_revenue += quantity * price
    
    return total_revenue

# Chức năng tìm sản phẩm bán chạy nhất (sản phẩm có số lượng bán nhiều nhất)
def find_best_selling_product(transactions):
    product_sales = {}
    
    for transaction in transactions:
        product_code, quantity, _ = transaction
        if product_code in product_sales:
            product_sales[product_code] += quantity
        else:
            product_sales[product_code] = quantity
    
    best_selling_product = None
    max_quantity = 0
    
    for product_code, total_quantity in product_sales.items():
        if total_quantity > max_quantity:
            max_quantity = total_quantity
            best_selling_product = product_code
    
    return best_selling_product

# Chức năng sắp xếp và in ra danh sách sản phẩm theo tổng doanh thu từ cao đến thấp
def sort_products_by_revenue(transactions):
    product_revenue = {}
    
    for transaction in transactions:
        product_code, quantity, price = transaction
        revenue = quantity * price
        if product_code in product_revenue:
            product_revenue[product_code] += revenue
        else:
            product_revenue[product_code] = revenue
     
    sorted_products = []
    product_revenue_items = list(product_revenue.items())  # Lấy danh sách các cặp (product_code, revenue)

    for i in range(len(product_revenue_items)):
        for j in range(i + 1, len(product_revenue_items)):
            if product_revenue_items[i][1] < product_revenue_items[j][1]:
                # Đổi chỗ nếu doanh thu của sản phẩm hiện tại nhỏ hơn sản phẩm tiếp theo
                product_revenue_items[i], product_revenue_items[j] = product_revenue_items[j], product_revenue_items[i]

    for product_code, revenue in product_revenue_items:
        sorted_products.append((product_code, revenue))

    
    return sorted_products

##### Chương trình chính #######

# Tạo danh sách giao dịch bán hàng
transactions = [("SP01", 10, 100), ("SP02", 5, 200), ("SP01", 2, 100)]

# Tính tổng doanh thu từ tất cả các giao dịch
total_revenue = calculate_total_revenue(transactions)
print(f"Tổng doanh thu: {total_revenue}")

# Tìm sản phẩm bán chạy nhất
best_selling_product = find_best_selling_product(transactions)
print(f"Sản phẩm bán chạy nhất: {best_selling_product}")

# Sắp xếp sản phẩm theo tổng doanh thu từ cao đến thấp
sorted_products = sort_products_by_revenue(transactions)
print(f"Danh sách sản phẩm theo doanh thu: {sorted_products}")
