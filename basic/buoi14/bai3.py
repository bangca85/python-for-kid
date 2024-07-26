'''
Bài 3: 
str ="3,6,9,12,15,18,21,24,27,30,33,36,39,42"
1. In ra màn hình các phần tử nằm trong khoảng từ 10 đến 30 (bao gồm 10 và 30).
2. Sắp xếp mảng theo thứ tự tăng dần sau đó in mảng ra màn hình.
3. Tính tổng các phần tử lẻ.
'''
str_in = "3,6,9,12,15,18,21,24,27,30,33,36,39,42"

# Chuyển chuỗi thành mảng các số nguyên
numbers = list(map(int, str_in.split(',')))

# 1. In ra màn hình các phần tử nằm trong khoảng từ 10 đến 30 (bao gồm 10 và 30)
in_range_10_30 = []
for num in numbers:
    if 10 <= num <= 30:
        in_range_10_30.append(num)
print("Các phần tử nằm trong khoảng từ 10 đến 30:", in_range_10_30)

# 2. Sắp xếp mảng theo thứ tự tăng dần sau đó in mảng ra màn hình
numbers.sort()
print("Mảng sắp xếp tăng dần:", numbers)

# 3. Tính tổng các phần tử lẻ
sum_of_odd_numbers = 0
for num in numbers:
    if num % 2 != 0:
        sum_of_odd_numbers += num
print("Tổng các phần tử lẻ:", sum_of_odd_numbers)

