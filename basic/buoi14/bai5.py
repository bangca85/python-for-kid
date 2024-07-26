'''
Bài 5:
str = "3,6,9,12,15,18,21,24,27,30,33,36,39,42"
1. In ra màn hình các phần tử là bội số của cả 3 và 4.
2. Sắp xếp mảng theo thứ tự tăng dần và in ra màn hình.
3. Tìm giá trị trung bình của mảng.
'''
str_in = "3,6,9,12,15,18,21,24,27,30,33,36,39,42"

# Chuyển chuỗi thành mảng các số nguyên
numbers = list(map(int, str_in.split(',')))

# 1. In ra màn hình các phần tử là bội số của cả 3 và 4
multiples_of_3_and_4 = []
for num in numbers:
    if num % 3 == 0 and num % 4 == 0:
        multiples_of_3_and_4.append(num)
print("Các phần tử là bội số của cả 3 và 4:", multiples_of_3_and_4)

# 2. Sắp xếp mảng theo thứ tự tăng dần và in ra màn hình
numbers.sort()
print("Mảng sắp xếp tăng dần:", numbers)

# 3. Tìm giá trị trung bình của mảng
average_value = sum(numbers) / len(numbers)
print("Giá trị trung bình của mảng:", average_value)
