'''
Bài 10:
str = "3,6,9,12,15,18,21,24,27,30,33,36,39,42"
1. In ra màn hình các phần tử nằm trong khoảng từ 20 đến 40 (bao gồm 20 và 40).
2. Sắp xếp mảng theo thứ tự tăng dần và in ra màn hình.
3. Tính tích của tất cả các phần tử trong mảng.
4. Đếm số phần tử là số chẵn trong mảng.
'''

# Chuỗi đầu vào
str_data = "3,6,9,12,15,18,21,24,27,30,33,36,39,42"

# Tách chuỗi thành danh sách các số
numbers = list(map(int, str_data.split(',')))

# 1. In ra màn hình các phần tử nằm trong khoảng từ 20 đến 40 (bao gồm 20 và 40)
within_range = []
for num in numbers:
    if 20 <= num <= 40:
        within_range.append(num)
print("Các phần tử nằm trong khoảng từ 20 đến 40:", within_range)

# 2. Sắp xếp mảng theo thứ tự tăng dần và in ra màn hình
sorted_numbers = sorted(numbers)
print("Mảng sau khi sắp xếp tăng dần:", sorted_numbers)

# 3. Tính tích của tất cả các phần tử trong mảng
product = 1
for num in numbers:
    product *= num
print("Tích của tất cả các phần tử trong mảng:", product)

# 4. Đếm số phần tử là số chẵn trong mảng
even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
print("Số phần tử là số chẵn trong mảng:", even_count)
