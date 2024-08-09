'''
Bài 17 
str = "4,8,15,16,23,42,50,54,60,72" 
1. In ra màn hình các phần tử là số chẵn và là bội số của 4. 
2. Sắp xếp mảng theo thứ tự giảm dần và in ra màn hình. 
3. Tính tích của 4 số lớn nhất trong mảng. 
4. Tìm phần tử có giá trị lớn nhất và phần tử nhỏ nhất trong mảng.
'''

# Chuỗi đầu vào
str_in = "4,8,15,16,23,42,50,54,60,72"
# Tách chuỗi sang danh sách các số
numbers = list(map(int, str_in.split(',')))

# 1. In ra môn hình các phần tử là số chẵn và là bội số của 4
list_4 = []
for number in numbers:
    if number % 2 == 0 and number % 4 == 0:
        list_4.append(number)
print("Các phần tử là số chẵn và là bội số của 4:", list_4)

# 2. Sắp xếp mảng theo thứ tự giảm dần và in ra môn hình
numbers.sort(reverse=True)
print("Mảng sắp xếp giảm dần:", numbers)

# 3. Tính tích của 4 số lớn nhất trong mảng
add_4 = 1
for num in numbers[:4]:
    add_4 *= num
print("Tích 4 số lớn nhất trong mảng:", add_4)

# 4. Tìm phần tử có giá trị lớn nhất và phần tử nhỏ nhất trong mảng
print("Phần tử có giá trị lớn nhất trong mảng:", max(numbers))
print("Phần tử nhỏ nhất trong mảng:", min(numbers))
