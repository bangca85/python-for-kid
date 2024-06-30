'''
Bài tập 1: Viết chương trình xóa các phần tử trùng lặp trong danh sách.
• input: original_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10]
• output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
def xoa_phan_tu_trung(original_list):
    new_list = []
    for i in original_list:
        if i not in new_list:
            new_list.append(i)
    return new_list

'''
Bài tập 2: Tìm giá trị lớn thứ hai trong danh sách
• input: numbers = [5, 3, 9, 1, 10, 6, 8, 4, 7, 2]
• output: 9
'''
def tim_phan_tu_lon_thu_hai(numbers):
    numbers.sort()
    return numbers[-2]

def second_largest(numbers):
    first, second = float('-inf'), float('-inf')
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second

'''
Bài tập 3: Đếm số phần tử chẵn và lẻ
• input: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
• output: Even: 5, Odd: 5
'''
def dem_so_phan_tu_chan_va_lon(numbers):
    even = 0
    odd = 0
    for i in numbers:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

'''
Bài tập 4: Đảo ngược từ trong câu
• input: sentence = "Hello world this is Python"
• output: "Python is this world Hello"
'''
def dao_nguoc_cau(sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words)

'''
Bài tập 5: Tính tổng các số trong danh sách con
• input: nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
• output: [6, 15, 24]
'''
def tinh_tong_cac_so_trong_danh_sach_con(nested_list):
    result = []
    for sublist in nested_list:
        result.append(sum(sublist))
    return result

def sum_nested_list(nested_list):
    sums = []
    for sublist in nested_list:
        total = 0
        for num in sublist:
            total += num
        sums.append(total)
    return sums

'''
Bài tập 6: Viết chương trình tìm tất cả các số từ 1 đến 100 chia hết cho cả 3 và 5.
• input:
• output: [15, 30, 45, 60, 75, 90]
'''
def tim_so_chia_het_cho_3_5():
    result = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            result.append(i)
    return result

'''
Bài tập 7: Viết chương trình lọc các chuỗi trong danh sách có độ dài lớn hơn 3.
• input: words = ["Python", "is", "fun", "and", "awesome"]
• output: ['Python', 'awesome']
'''
def tim_chuoi_lon_hon_3(words):
    result = []
    for word in words:
        if len(word) > 3:
            result.append(word)
    return result

'''
Bài tập 8: Viết chương trình tìm các phần tử chung trong hai danh sách.
• input: list1 = [1, 2, 3, 4, 5] và list2 = [4, 5, 6, 7, 8]
• output: [4, 5]
'''
def tim_phan_tu_chung(list1, list2):
    result = []
    for i in list1:
        if i in list2 and i not in result:
            result.append(i)
    return result

'''
Bài tập 9: Viết chương trình nhân đôi các phần tử lẻ trong danh sách.
• input: numbers = [1, 2, 3, 4, 5]
• output: [2, 2, 6, 4, 10]
'''
def nhap_doi_tat_cac_phan_tu(numbers):
    result = []
    for i in numbers:
        result.append(i * 2)
    return result

def double_odd_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 != 0:
            result.append(num * 2)
        else:
            result.append(num)
    return result

'''
Bài tập 10: Viết chương trình tính trung bình các phần tử trong mỗi danh sách con.
• input: nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
• output: [2.0, 5.0, 8.0]
'''
def tinh_trung_binh_cac_phan_tu_trong_danh_sach_con(nested_list):
    result = []
    for sublist in nested_list:
        result.append(sum(sublist) / len(sublist))
    return result

def average_nested_list(nested_list):
    averages = []
    for sublist in nested_list:
        total = 0
        for num in sublist:
            total += num
        averages.append(total / len(sublist))
    return averages

'''
Bài tập 11: Viết chương trình tạo danh sách chứa các số lẻ từ 1 đến 100.
• input:
output: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51,
53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
'''
def tao_danh_sach_so_le():
    result = []
    for i in range(1, 101):
        if i % 2 != 0:
            result.append(i)
    return result

'''
Bài tập 12: Viết chương trình đếm số từ trong một câu.
• input: sentence = "Hello world this is Python"
• output: 5
'''
def dem_so_tu(sentence):
    return len(sentence.split())

def word_count(sentence):
    words = sentence.split(' ')
    return len(words)

'''
Bài tập 13: Viết chương trình tạo danh sách các số từ 1 đến 50 không chia hết cho cả 2 và 3.
• input:
• output: [1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 43, 47, 49]
'''
def tao_danh_sach_so_chia_het_cho_2_3():
    result = []
    for i in range(1, 51):
        if i % 2 == 0 and i % 3 == 0:
            result.append(i)
    return result

'''
Bài tập 14: Viết chương trình tìm số lớn thứ ba trong danh sách.
• input: numbers = [5, 3, 9, 1, 10, 6, 8, 4, 7, 2]
• output: 8
'''
def tim_phan_tu_lon_thu_ba(numbers):
    numbers.sort()
    return numbers[-3]

def third_largest(numbers):
    first, second, third = float('-inf'), float('-inf'), float('-inf')
    for num in numbers:
        if num > first:
            third = second
            second = first
            first = num
        elif num > second and num != first:
            third = second
            second = num
        elif num > third and num != second and num != first:
            third = num
    return third

'''
Bài tập 15: Viết chương trình tạo danh sách các ký tự từ một chuỗi và loại bỏ các ký tự trùng lặp.
• input: string = "programming"
• output: ['p', 'r', 'o', 'g', 'a', 'm', 'i', 'n']
'''
def tao_danh_sach_ky_tu_trong_chuoi(string):
    result = []
    for char in string:
        if char not in result:
            result.append(char)
    return result
