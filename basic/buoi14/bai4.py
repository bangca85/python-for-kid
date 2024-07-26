'''
Bài 4: 
str = "2,5,8,13,21,34,55,89,144,233,377,610"
1. In ra màn hình các phần tử là số nguyên tố.
2. Sắp xếp mảng theo thứ tự tăng dần sau đó in mảng ra màn hình.
3. Tính tích của 3 số lớn nhất.

'''
str_in = "2,5,8,13,21,34,55,89,144,233,377,610"

# Chuyển chuỗi thành mảng các số nguyên
numbers = list(map(int, str_in.split(',')))

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 1. In ra màn hình các phần tử là số nguyên tố
prime_numbers = []
for num in numbers:
    if is_prime(num):
        prime_numbers.append(num)
print("Các phần tử là số nguyên tố:", prime_numbers)

# 2. Sắp xếp mảng theo thứ tự tăng dần sau đó in mảng ra màn hình
numbers.sort()
print("Mảng sắp xếp tăng dần:", numbers)

# 3. Tính tích của 3 số lớn nhất
product_of_largest_three = numbers[-1] * numbers[-2] * numbers[-3]
print("Tích của 3 số lớn nhất:", product_of_largest_three)
