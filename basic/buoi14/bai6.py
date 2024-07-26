'''
Bài 6: 
str = "102,56,87,34,21,78,100,99,34,56,78"
1. In ra màn hình các phần tử có chữ số đầu tiên là 1.
2. Sắp xếp mảng theo thứ tự giảm dần và in ra màn hình.
3. Tìm phần tử có tần suất xuất hiện nhiều nhất và in ra giá trị đó.
'''

str_in = "102,56,87,34,21,78,100,99,34,56,78"

# Chuyển chuỗi thành mảng các số nguyên
numbers = list(map(int, str_in.split(',')))

# 1. In ra màn hình các phần tử có chữ số đầu tiên là 1
first_digit_1 = []
for num in numbers:
    if str(num)[0] == '1':
        first_digit_1.append(num)
print("Các phần tử có chữ số đầu tiên là 1:", first_digit_1)

# 2. Sắp xếp mảng theo thứ tự giảm dần và in ra màn hình
numbers.sort(reverse=True)
print("Mảng sắp xếp giảm dần:", numbers)

# 3. Tìm phần tử có tần suất xuất hiện nhiều nhất và in ra giá trị đó
max_count = 0
most_frequent = None
for num in numbers:
    count = numbers.count(num)
    if count > max_count:
        max_count = count
        most_frequent = num

print("Phần tử có tần suất xuất hiện nhiều nhất:", most_frequent)
