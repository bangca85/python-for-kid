'''
 Bài tập 6: Phân tích dữ liệu tiêu dùng của khách hàng

#### Yêu cầu:

1. Nhập vào một danh sách các giao dịch của khách hàng, mỗi giao dịch bao gồm tên khách hàng, số lượng hàng hóa và giá trị giao dịch.
2. Viết chức năng để tính tổng số tiền mà mỗi khách hàng đã chi tiêu.
3. Viết chức năng để tìm và in ra khách hàng chi tiêu nhiều nhất.
4. Viết chức năng để tìm tất cả các khách hàng có tổng chi tiêu trên mức trung bình.

#### Ví dụ:

```python
# Input: [("John", 2, 100), ("Alice", 3, 150), ("John", 1, 50), ("Bob", 5, 200)]
# Output:
# Tổng chi tiêu của mỗi khách hàng: {"John": 250, "Alice": 150, "Bob": 200}
# Khách hàng chi tiêu nhiều nhất: John
# Khách hàng có chi tiêu trên mức trung bình: {"John": 250, "Bob": 200}
```

---
'''

# Chức năng để tính tổng số tiền mà mỗi khách hàng đã chi tiêu
def calculate_total_spent(transactions):
    total_spent = {}
    for transaction in transactions:
        name, quantity, value = transaction
        if name in total_spent:
            total_spent[name] += quantity * value
        else:
            total_spent[name] = quantity * value
    return total_spent

# Chức năng để tìm và trả về khách hàng chi tiêu nhiều nhất
def find_highest_spender(total_spent):
    highest_spender = None
    highest_amount = float('-inf')

    for name, amount in total_spent.items():
        if amount > highest_amount:
            highest_amount = amount
            highest_spender = name

    return highest_spender

# Chức năng để tìm và trả về tất cả các khách hàng có tổng chi tiêu trên mức trung bình
def find_above_average_spenders(total_spent):
    average_spent = sum(total_spent.values()) / len(total_spent)
    above_average_spenders = {}

    for name, amount in total_spent.items():
        if amount > average_spent:
            above_average_spenders[name] = amount

    return above_average_spenders

# Chạy chương trình với dữ liệu mẫu
transactions = [("John", 2, 100), ("Alice", 3, 150), ("John", 1, 50), ("Bob", 5, 200)]

# Tính tổng số tiền mà mỗi khách hàng đã chi tiêu
total_spent = calculate_total_spent(transactions)
print(f"Tổng chi tiêu của mỗi khách hàng: {total_spent}")

# Tìm và in ra khách hàng chi tiêu nhiều nhất
highest_spender = find_highest_spender(total_spent)
print(f"Khách hàng chi tiêu nhiều nhất: {highest_spender}")

# Tìm tất cả các khách hàng có tổng chi tiêu trên mức trung bình
above_average_spenders = find_above_average_spenders(total_spent)
print(f"Khách hàng có chi tiêu trên mức trung bình: {above_average_spenders}")
