'''
Bài 11:
str = "1,3,5,7,9,11,13,15,17,19,21"
1. In ra màn hình các phần tử là số lẻ.
2. Sắp xếp mảng theo thứ tự giảm dần và in ra màn hình.
3. Tính tổng các phần tử lớn hơn 10.
4. Tìm phần tử nhỏ nhất và lớn nhất trong mảng.
'''
# Chuỗi đầu vào
str_data = "1,3,5,7,9,11,13,15,17,19,21"

# Tách chuỗi thành danh sách các số
numbers = list(map(int, str_data.split(',')))

# 1. In ra màn hình các phần tử là số lẻ
odd_numbers = []
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)
print("Các phần tử là số lẻ:", odd_numbers)

# 2. Sắp xếp mảng theo thứ tự giảm dần và in ra màn hình
sorted_numbers_desc = sorted(numbers, reverse=True)
print("Mảng sau khi sắp xếp giảm dần:", sorted_numbers_desc)

# 3. Tính tổng các phần tử lớn hơn 10
sum_greater_than_10 = 0
for num in numbers:
    if num > 10:
        sum_greater_than_10 += num
print("Tổng các phần tử lớn hơn 10:", sum_greater_than_10)

# 4. Tìm phần tử nhỏ nhất và lớn nhất trong mảng
min_number = numbers[0]
max_number = numbers[0]
for num in numbers:
    if num < min_number:
        min_number = num
    if num > max_number:
        max_number = num
print("Phần tử nhỏ nhất:", min_number)
print("Phần tử lớn nhất:", max_number)
