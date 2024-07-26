'''
Bài 1:
str = "12,34,23,45,67,89,100,45,67,23,34,12"
1. In ra màn hình các phần tử xuất hiện nhiều hơn 1 lần.
2. Sắp xếp mảng giảm dần và in ra màn hình.
3. Tính trung bình cộng của các phần tử lớn hơn 50.
'''
str_in = "12,34,23,45,67,89,100,45,67,23,34,12"

# Chuyển chuỗi thành mảng các số nguyên
numbers = list(map(int, str_in.split(',')))

# 1. In ra màn hình các phần tử xuất hiện nhiều hơn 1 lần
duplicate_numbers = []
for number in numbers:
    if numbers.count(number) > 1:
        duplicate_numbers.append(number)
print("Phần tử xuất hiện nhiều hơn 1 lần:", duplicate_numbers)


# 2. Sắp xếp mảng giảm dần và in ra màn hình
numbers.sort(reverse=True)
print("Mảng sắp xếp giảm dần:", numbers)

# 3. Tính trung bình cộng của các phần tử lớn hơn 50
greater_than_50 = []
for num in numbers:
    if num > 50:
        greater_than_50.append(num)

if greater_than_50:
    average_greater_than_50 = sum(greater_than_50) / len(greater_than_50)
else:
    average_greater_than_50 = 0
print("Trung bình cộng của các phần tử lớn hơn 50:", average_greater_than_50)
