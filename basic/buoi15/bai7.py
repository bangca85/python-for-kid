'''
str = "50,60,70,80,90,100,110,120,130,140,150"
1. In ra màn hình các phần tử là số chẵn.
2. Sắp xếp mảng theo thứ tự tăng dần và in ra màn hình.
3. Tính tổng các phần tử nhỏ hơn 100.
4. Tìm phần tử lớn nhất và nhỏ nhất trong mảng.
'''
# Chuỗi đầu vào
str_data = "50,60,70,80,90,100,110,120,130,140,150"

# Tách chuỗi thành danh sách các số
numbers = list(map(int, str_data.split(',')))

# 1. In ra màn hình các phần tử là số chẵn
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print("Các phần tử là số chẵn:", even_numbers)

# 2. Sắp xếp mảng theo thứ tự tăng dần và in ra màn hình
sorted_numbers = sorted(numbers)
print("Mảng sau khi sắp xếp tăng dần:", sorted_numbers)

# 3. Tính tổng các phần tử nhỏ hơn 100
sum_less_than_100 = 0
for num in numbers:
    if num < 100:
        sum_less_than_100 += num
print("Tổng các phần tử nhỏ hơn 100:", sum_less_than_100)

# 4. Tìm phần tử lớn nhất và nhỏ nhất trong mảng
max_number = numbers[0]
min_number = numbers[0]
for num in numbers:
    if num > max_number:
        max_number = num
    if num < min_number:
        min_number = num
print("Phần tử lớn nhất:", max_number)
print("Phần tử nhỏ nhất:", min_number)
