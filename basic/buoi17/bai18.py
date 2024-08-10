'''
Bài 18 
str = "3,7,11,15,19,23,27,31,35,39" 
1. In ra màn hình các phần tử là số lẻ và chia hết cho 5. 
2. Sắp xếp mảng theo thứ tự tăng dần và in ra màn hình. 
3. Tính tổng các phần tử là số nguyên tố. 
4. Tìm phần tử có giá trị trung bình trong mảng.
'''

# Chuỗi đầu vào
str_in = "3,7,11,15,19,23,27,31,35,39"
# Tách chuỗi sang danh sách các số
numbers = list(map(int, str_in.split(',')))

# 1. In ra môn hình các phần tử là số lẻ và chia hết cho 5
list_5 = []
for number in numbers:
    if number % 2 != 0 and number % 5 == 0:
        list_5.append(number)
print("Các phần tử là số lẻ và chia hết cho 5:", list_5)

# 2. Sắp xếp mảng theo thứ tự tăng dần và in ra môn hình
numbers.sort()
print("Mảng sắp xếp giảm dần:", numbers)

# 3. Tính tổng các phần tử là số nguyên tố
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

sum_prime = 0
for num in numbers:
    if is_prime(num):
        sum_prime += num
print("Tích số nguyên tố:", sum_prime)

# 4. Tìm phần tử có giá trị trung bình trong mảng
print("Phần tử có giá trị trung bình trong mảng:", sum(numbers) / len(numbers))