'''
Bài 16 
str = "9,18,27,36,45,54,63,72,81,90" 
1. In ra màn hình các phần tử là bội số của cả 3 và 9. 
2. Sắp xếp mảng theo thứ tự tăng dần và in ra màn hình. 
3. Tính trung bình cộng của các phần tử lớn hơn 50 và nhỏ hơn 80. 
4. Tìm phần tử lớn thứ ba và nhỏ thứ ba trong mảng.
'''
# Chuỗi đầu vào
str_in = "9,18,27,36,45,54,63,72,81,90"
# Tách chuỗi sang danh sách các số
numbers = list(map(int, str_in.split(',')))

# 1. In ra môn hình các phần tử là bội số của cả 3 và 9
list_3_9 = []
for number in numbers:
    if number % 3 == 0 and number % 9 == 0:
        list_3_9.append(number)
print("Các phần tử là bội số của cả 3 và 9:", list_3_9)

# 2. Sắp xếp mảng theo thứ tự tăng dần và in ra màn hình
numbers.sort()
print("Mảng sắp xếp giảm dần:", numbers)

# 3. Tính trung bình cộng của các phần tử lớn hơn 50 và nhỏ hơn 80
sum_greater_than_50 = 0
count_greater_than_50 = 0
sum_greater_than_80 = 0
count_greater_than_80 = 0
for num in numbers:
    if num > 50:
        sum_greater_than_50 += num
        count_greater_than_50 += 1
    if num > 80:
        sum_greater_than_80 += num
        count_greater_than_80 += 1

avg_greater_than_50 = sum_greater_than_50 / count_greater_than_50
avg_greater_than_80 = sum_greater_than_80 / count_greater_than_80
print("Trung bình cộng cấu hình lớn hơn 50:", avg_greater_than_50)
print("Trung bình cộng cấu hình lớn hơn 80:", avg_greater_than_80)

# 4. Tìm phần tử lớn thứ ba và nhỏ thứ ba trong mảng
print("Phần tử lớn thứ ba trong mảng:", numbers[2])
print("Phần tử nhỏ thứ ba trong mảng:", numbers[-2])    