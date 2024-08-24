'''
Bài tập 10: Quản lý đơn đặt hàng của khách hàng

#### Yêu cầu:

1. Tạo một danh sách chứa các đơn đặt hàng, mỗi đơn đặt hàng bao gồm tên khách hàng, sản phẩm, số lượng, và giá.
2. Viết chức năng để tính tổng số tiền mà mỗi khách hàng phải trả.
3. Viết chức năng để tìm và in ra khách hàng có tổng số tiền phải trả cao nhất.
4. Viết chức năng để tìm tất cả các khách hàng có tổng số tiền phải trả trên mức trung bình.

#### Ví dụ:

```python
# Input: [("John", "Laptop", 1, 1000), ("Alice", "Phone", 2, 600), ("Bob", "Tablet", 1, 300)]
# Output:
# Tổng số tiền của mỗi khách hàng: {"John": 1000, "Alice": 1200, "Bob": 300}
# Khách hàng có tổng số tiền cao nhất: Alice
# Khách hàng có tổng số tiền trên mức trung bình: {"Alice": 1200}
```

---
'''
# Chức năng tính tổng số tiền mà mỗi khách hàng phải trả
def calculate_total_amount(orders):
    customer_totals = {}
    
    for order in orders:
        customer, product, quantity, price = order
        total = quantity * price
        if customer in customer_totals:
            customer_totals[customer] += total
        else:
            customer_totals[customer] = total
    
    return customer_totals

# Chức năng tìm và in ra khách hàng có tổng số tiền phải trả cao nhất
def find_highest_payer(customer_totals):
    highest_customer = None
    highest_total = 0
    
    for customer, total in customer_totals.items():
        if total > highest_total:
            highest_total = total
            highest_customer = customer
    
    return highest_customer

# Chức năng tìm tất cả các khách hàng có tổng số tiền phải trả trên mức trung bình
def find_above_average_customers(customer_totals):
    total_sum = sum(customer_totals.values())
    average_total = total_sum / len(customer_totals)
    
    above_average_customers = {}
    
    for customer, total in customer_totals.items():
        if total > average_total:
            above_average_customers[customer] = total
    
    return above_average_customers

####### Chương trình chính ######

# Tạo danh sách đơn đặt hàng
orders = [("John", "Laptop", 1, 1000), ("Alice", "Phone", 2, 600), ("Bob", "Tablet", 1, 300)]

# Tính tổng số tiền của mỗi khách hàng
customer_totals = calculate_total_amount(orders)
print(f"Tổng số tiền của mỗi khách hàng: {customer_totals}")

# Tìm khách hàng có tổng số tiền phải trả cao nhất
highest_payer = find_highest_payer(customer_totals)
print(f"Khách hàng có tổng số tiền cao nhất: {highest_payer}")

# Tìm khách hàng có tổng số tiền trên mức trung bình
above_average_customers = find_above_average_customers(customer_totals)
print(f"Khách hàng có tổng số tiền trên mức trung bình: {above_average_customers}")
