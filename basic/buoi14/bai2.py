'''
Bài 2: 
str = "5,10,15,20,25,30,35,40,45,50,55,60"
1. In ra màn hình các phần tử là số lẻ.
2. Sắp xếp mảng theo thứ tự giảm dần sau đó in mảng ra màn hình.
3. Tìm số lớn thứ hai trong mảng.
'''
str_in = "5,10,15,20,25,30,35,40,45,50,55,60"

# Chuyển chuỗi thành mảng các số nguyên
numbers = list(map(int, str_in.split(',')))

# 1. In ra màn hình các phần tử là số lẻ
odd_numbers = []
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)
print("Các phần tử là số lẻ:", odd_numbers)

# 2. Sắp xếp mảng theo thứ tự giảm dần sau đó in mảng ra màn hình
numbers.sort(reverse=True)
print("Mảng sắp xếp giảm dần:", numbers)

# 3. Tìm số lớn thứ hai trong mảng
largest = numbers[0]
second_largest = None
for num in numbers:
    if num != largest:
        second_largest = num
        break
print("Số lớn thứ hai trong mảng:", second_largest)
# hoặc 1 cách đơn giản hơn

print("Số lớn thứ hai trong mảng:", numbers[2])