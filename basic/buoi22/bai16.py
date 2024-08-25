'''
### Bài tập 16: Phân tích và xử lý dữ liệu bán lẻ

#### Yêu cầu:

1. Nhập vào danh sách các giao dịch bán lẻ, mỗi giao dịch bao gồm mã sản phẩm, số lượng bán và giá bán.
2. Viết chức năng để tính tổng doanh thu từ tất cả các giao dịch.
3. Viết chức năng để tìm sản phẩm có doanh thu cao nhất.
4. Viết chức năng để tạo và in ra báo cáo doanh thu chi tiết cho từng sản phẩm.

#### Ví dụ:

```python
# Input: [("SP01", 10, 100), ("SP02", 5, 200), ("SP01", 2, 100)]
# Output:
# Tổng doanh thu: 2400
# Sản phẩm có doanh thu cao nhất: SP01
# Báo cáo doanh thu: {"SP01": {"số lượng": 12, "doanh thu": 1200}, {"SP02": {"số lượng": 5, "doanh thu": 1000}}
```

---

'''


# 2. Tính tổng doanh thu từ tất cả các giao dịch
def calculate_total_revenue(transactions):
    total_revenue = 0
    for _, quantity, price in transactions:
        total_revenue += quantity * price
    return total_revenue

# 3. Tìm sản phẩm có doanh thu cao nhất
def find_best_selling_product(transactions):
    product_revenue = {}
    for product_code, quantity, price in transactions:
        if product_code in product_revenue:
            product_revenue[product_code] += quantity * price
        else:
            product_revenue[product_code] = quantity * price
    best_selling_product = max(product_revenue, key=product_revenue.get)
    return best_selling_product

# 4. Tạo và in ra báo cáo doanh thu chi tiết cho từng sản phẩm
def generate_sales_report(transactions):
    sales_report = {}
    for product_code, quantity, price in transactions:
        if product_code in sales_report:
            sales_report[product_code]["số lượng"] += quantity
            sales_report[product_code]["doanh thu"] += quantity * price
        else:
            sales_report[product_code] = {"số lượng": quantity, "doanh thu": quantity * price}
    return sales_report

# Chạy các chức năng và in kết quả
# Danh sách các giao dịch bán lẻ
transactions = [("SP01", 10, 100), ("SP02", 5, 200), ("SP01", 2, 100)]

total_revenue = calculate_total_revenue(transactions)
print(f"Tổng doanh thu: {total_revenue}")

best_selling_product = find_best_selling_product(transactions)
print(f"Sản phẩm có doanh thu cao nhất: {best_selling_product}")

sales_report = generate_sales_report(transactions)
print(f"Báo cáo doanh thu: {sales_report}")
