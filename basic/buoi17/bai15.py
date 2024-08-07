'''
Bài 15
str = "23,45,12,67,34,89,56,78,91,104"
1. In ra màn hình các phần tử là số nguyên tố và có hai chữ số.
2. Sắp xếp mảng theo thứ tự giảm dần và in ra màn hình.
3. Tính tổng các phần tử là số chẵn và lớn hơn 50.
4. Tìm phần tử nhỏ thứ ba trong mảng.
'''
list_str = "23,45,12,67,34,89,56,78,91,104"
# Chuyển chuỗi này mảng các số nguyên
numbers = list(map(int, list_str.split(',')))

# 1. In ra môn hình các phần tử là số nguyên tố và có hai chữ số
# viết hàm tìm số nguyên tố
def find_prime_number(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

list_prime = []
for number in numbers:
    if find_prime_number(number) and 9 < number < 100:
        list_prime.append(number)
print("Các phần tử là số nguyên tố và có hai chữ số:", list_prime)

#2. Sắp xếp mảng theo thứ tự giảm dần và in ra màn hình.
numbers.sort(reverse=True)
print("Mảng sắp xếp giảm dần:", numbers)

# 3. Tính tổng các phần tử là số chẵn và lớn hơn 50
sum_odd = 0
sum_greater_than_50 = 0
for num in numbers:
    if num % 2 == 1:
        sum_odd += num
    if num > 50:
        sum_greater_than_50 += num
print("Tích số chẵn:", sum_odd)
print("Tích số lớn hơn 50:", sum_greater_than_50)

# 4. Tìm phần tử nhỏ thứ ba trong mảng
print("Phần tử nhỏ thứ ba trong mảng:", numbers[-3])