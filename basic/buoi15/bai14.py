'''
Bài 14:
str = "101,102,103,104,105,106,107,108,109,110"
1. In ra màn hình các phần tử có tổng các chữ số bằng 5.
2. Sắp xếp mảng theo thứ tự tăng dần và in ra màn hình.
3. Tìm phần tử lớn thứ hai và phần tử nhỏ thứ hai trong mảng.
4. Tính tích của tất cả các phần tử lẻ trong mảng.
'''
# Chuỗi đầu vào
str_data = "101,102,103,104,105,106,107,108,109,110"

# Tách chuỗi thành danh sách các số
numbers = list(map(int, str_data.split(',')))

# 1. In ra màn hình các phần tử có tổng các chữ số bằng 5
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

numbers_with_digit_sum_5 = []
for num in numbers:
    if sum_of_digits(num) == 5:
        numbers_with_digit_sum_5.append(num)
print("Các phần tử có tổng các chữ số bằng 5:", numbers_with_digit_sum_5)

# 2. Sắp xếp mảng theo thứ tự tăng dần và in ra màn hình
sorted_numbers = sorted(numbers)
print("Mảng sau khi sắp xếp tăng dần:", sorted_numbers)

# 3. Tìm phần tử lớn thứ hai và phần tử nhỏ thứ hai trong mảng
second_largest = sorted_numbers[-2]
second_smallest = sorted_numbers[1]
print("Phần tử lớn thứ hai:", second_largest)
print("Phần tử nhỏ thứ hai:", second_smallest)

# 4. Tính tích của tất cả các phần tử lẻ trong mảng
product_of_odds = 1
for num in numbers:
    if num % 2 != 0:
        product_of_odds *= num
print("Tích của tất cả các phần tử lẻ trong mảng:", product_of_odds)
git 