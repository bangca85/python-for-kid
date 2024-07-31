'''
Bài 8:
str = "5,15,25,35,45,55,65,75,85,95,105"
1. In ra màn hình các phần tử chia hết cho 5.
2. Sắp xếp mảng theo thứ tự giảm dần và in ra màn hình.
3. Tính trung bình cộng của các phần tử trong mảng.
4. Tìm phần tử nhỏ thứ hai trong mảng.

'''
# Chuỗi đầu vào
str_data = "5,15,25,35,45,55,65,75,85,95,105"

# Tách chuỗi thành danh sách các số
numbers = list(map(int, str_data.split(',')))

# 1. In ra màn hình các phần tử chia hết cho 5
divisible_by_5 = []
for num in numbers:
    if num % 5 == 0:
        divisible_by_5.append(num)
print("Các phần tử chia hết cho 5:", divisible_by_5)

# 2. Sắp xếp mảng theo thứ tự giảm dần và in ra màn hình
sorted_desc = sorted(numbers, reverse=True)
print("Mảng sau khi sắp xếp giảm dần:", sorted_desc)

# 3. Tính trung bình cộng của các phần tử trong mảng
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print("Trung bình cộng của các phần tử trong mảng:", average)

# 4. Tìm phần tử nhỏ thứ hai trong mảng
# Sắp xếp mảng theo thứ tự tăng dần
sorted_asc = sorted(numbers)
second_smallest = sorted_asc[1]
print("Phần tử nhỏ thứ hai trong mảng:", second_smallest)
