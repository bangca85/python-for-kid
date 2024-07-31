'''
Bài 13:
str = "7,14,21,28,35,42,49,56,63,70,77,84,91,98,105"
1. In ra màn hình các phần tử là số nguyên tố.
2. Sắp xếp mảng theo thứ tự giảm dần và in ra màn hình.
3. Tìm phần tử có giá trị trung bình trong mảng.
4. Tính tổng bình phương của tất cả các phần tử.
'''
# Chuỗi đầu vào
str_data = "7,14,21,28,35,42,49,56,63,70,77,84,91,98,105"

# Tách chuỗi thành danh sách các số
numbers = list(map(int, str_data.split(',')))

# 1. In ra màn hình các phần tử là số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = []
for num in numbers:
    if is_prime(num):
        prime_numbers.append(num)
print("Các phần tử là số nguyên tố:", prime_numbers)

# 2. Sắp xếp mảng theo thứ tự giảm dần và in ra màn hình
sorted_numbers_desc = sorted(numbers, reverse=True)
print("Mảng sau khi sắp xếp giảm dần:", sorted_numbers_desc)

# 3. Tìm phần tử có giá trị trung bình trong mảng
total = 0
for num in numbers:
    total += num
average_value = total / len(numbers)

closest_to_average = numbers[0]
min_diff = abs(numbers[0] - average_value)
for num in numbers:
    diff = abs(num - average_value)
    if diff < min_diff:
        min_diff = diff
        closest_to_average = num
print("Phần tử có giá trị trung bình trong mảng:", closest_to_average)

# 4. Tính tổng bình phương của tất cả các phần tử
sum_of_squares = 0
for num in numbers:
    sum_of_squares += num ** 2
print("Tổng bình phương của tất cả các phần tử:", sum_of_squares)
