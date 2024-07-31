'''
Bài 9:
str = "10,20,30,40,50,60,70,80,90,100"
1. In ra màn hình các phần tử lớn hơn 50.
2. Sắp xếp mảng theo thứ tự tăng dần và in ra màn hình.
3. Tìm phần tử xuất hiện nhiều nhất và in ra giá trị đó.
4. Kiểm tra xem phần tử 25 có xuất hiện trong mảng hay không.

'''
# Chuỗi đầu vào
str_data = "10,20,30,40,50,60,70,80,90,100"

# Tách chuỗi thành danh sách các số
numbers = list(map(int, str_data.split(',')))

# 1. In ra màn hình các phần tử lớn hơn 50
greater_than_50 = []
for num in numbers:
    if num > 50:
        greater_than_50.append(num)
print("Các phần tử lớn hơn 50:", greater_than_50)

# 2. Sắp xếp mảng theo thứ tự tăng dần và in ra màn hình
sorted_numbers = sorted(numbers)
print("Mảng sau khi sắp xếp tăng dần:", sorted_numbers)

# 3. Tìm phần tử xuất hiện nhiều nhất và in ra giá trị đó
max_count = 0
most_common = None
for num in numbers:
    count = 0
    for other_num in numbers:
        if num == other_num:
            count += 1
    if count > max_count:
        max_count = count
        most_common = num
print("Phần tử xuất hiện nhiều nhất:", most_common)

# 4. Kiểm tra xem phần tử 25 có xuất hiện trong mảng hay không
found = False
for num in numbers:
    if num == 25:
        found = True
        break
if found:
    print("Phần tử 25 có xuất hiện trong mảng.")
else:
    print("Phần tử 25 không xuất hiện trong mảng.")
