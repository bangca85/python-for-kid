'''
Bài 12:
str = "4,8,12,16,20,24,28,32,36,40,44"
1. In ra màn hình các phần tử là bội số của 4.
2. Sắp xếp mảng theo thứ tự tăng dần và in ra màn hình.
3. Tính trung bình cộng của các phần tử trong mảng.
4. Tìm phần tử lớn thứ ba trong mảng.
'''

# Chuỗi đầu vào
str_data = "4,8,12,16,20,24,28,32,36,40,44"

# Tách chuỗi thành danh sách các số
numbers = list(map(int, str_data.split(',')))

# 1. In ra màn hình các phần tử là bội số của 4
multiples_of_4 = []
for num in numbers:
    if num % 4 == 0:
        multiples_of_4.append(num)
print("Các phần tử là bội số của 4:", multiples_of_4)

# 2. Sắp xếp mảng theo thứ tự tăng dần và in ra màn hình
sorted_numbers = sorted(numbers)
print("Mảng sau khi sắp xếp tăng dần:", sorted_numbers)

# 3. Tính trung bình cộng của các phần tử trong mảng
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print("Trung bình cộng của các phần tử trong mảng:", average)

# 4. Tìm phần tử lớn thứ ba trong mảng
# Sắp xếp mảng theo thứ tự tăng dần
sorted_numbers = sorted(numbers)
third_largest = sorted_numbers[-3]
print("Phần tử lớn thứ ba trong mảng:", third_largest)
