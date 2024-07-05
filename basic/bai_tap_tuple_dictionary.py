### Bài Tập Về Tuple
'''
Bài tập 1: Tính khoảng cách giữa hai điểm
**Yêu cầu:** Viết chương trình tính khoảng cách giữa hai điểm trong không gian 2D. Các tọa độ điểm được lưu trữ trong tuple.

**Hướng dẫn cách tiếp cận và giải bài:**
1. Sử dụng công thức khoảng cách Euclid giữa hai điểm `(x1, y1)` và `(x2, y2)`:
   \[
   \text{distance} = \sqrt{(x2 - x1)^2 + (y2 - y1)^2}
   \]
2. Lấy tọa độ từ các tuple.
3. Tính toán khoảng cách và định dạng kết quả để hiển thị.
''' 
import math

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

point1 = (3, 4)
point2 = (7, 1)
distance = calculate_distance(point1, point2)
print(f"Khoảng cách giữa {point1} và {point2} là {distance:.2f}")
 
'''
#### Bài tập 2: Tìm phần tử lớn thứ hai trong tuple
**Yêu cầu:** Viết chương trình tìm phần tử lớn thứ hai trong một tuple các số nguyên.

**Hướng dẫn cách tiếp cận và giải bài:**
1. Chuyển đổi tuple thành danh sách để dễ dàng thao tác.
2. Loại bỏ các phần tử trùng lặp bằng cách chuyển đổi danh sách thành tập hợp.
3. Sắp xếp tập hợp theo thứ tự giảm dần.
4. Lấy phần tử thứ hai trong danh sách đã sắp xếp.
'''
def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    return unique_numbers[-2]

numbers = (5, 3, 9, 1, 10, 6, 8, 4, 7, 2)
second_largest_num = second_largest(numbers)
print(f"Phần tử lớn thứ hai là: {second_largest_num}")

'''
#### Bài tập 3: Tìm các phần tử chung của hai tuple
**Yêu cầu:** Viết chương trình tìm các phần tử chung của hai tuple.

**Hướng dẫn cách tiếp cận và giải bài:**
1. Chuyển đổi hai tuple thành tập hợp.
2. Sử dụng phép toán giao của hai tập hợp để tìm các phần tử chung.
3. Chuyển kết quả trở lại dạng tuple.

'''
def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
common = common_elements(tuple1, tuple2)
print(f"Các phần tử chung là: {common}")

'''
#### Bài tập 4: Đảo ngược tuple
**Yêu cầu:** Viết chương trình đảo ngược thứ tự các phần tử trong một tuple.

**Hướng dẫn cách tiếp cận và giải bài:**
1. Sử dụng slicing để đảo ngược thứ tự các phần tử trong tuple.
'''

def reverse_tuple(tup):
    return tup[::-1]

numbers = (1, 2, 3, 4, 5)
reversed_numbers = reverse_tuple(numbers)
print(f"Tuple sau khi đảo ngược: {reversed_numbers}")

'''
#### Bài tập 5: Ghép các phần tử của hai tuple thành các cặp
**Yêu cầu:** Viết chương trình ghép các phần tử của hai tuple thành các cặp.

**Hướng dẫn cách tiếp cận và giải bài:**
1. Sử dụng hàm `zip` để ghép các phần tử từ hai tuple thành các cặp.
2. Chuyển đổi kết quả từ `zip` thành tuple.
'''
def pair_elements(tuple1, tuple2):
    return tuple(zip(tuple1, tuple2))

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
paired = pair_elements(tuple1, tuple2)
print(f"Các cặp phần tử: {paired}")
'''
### Bài Tập Về Dictionary

#### Bài tập 6: Đếm số lần xuất hiện của các ký tự trong chuỗi
**Yêu cầu:** Viết chương trình đếm số lần xuất hiện của mỗi ký tự trong một chuỗi.

**Hướng dẫn cách tiếp cận và giải bài:**
1. Khởi tạo một dictionary rỗng để lưu trữ số lần xuất hiện của mỗi ký tự.
2. Duyệt qua từng ký tự trong chuỗi và cập nhật số lần xuất hiện của nó trong dictionary.
3. Trả về dictionary chứa số lần xuất hiện của mỗi ký tự.

'''
def count_characters(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

text = "hello world"
char_count = count_characters(text)
print(f"Số lần xuất hiện của các ký tự: {char_count}")

'''#### Bài tập 7: Tạo danh bạ điện thoại
**Yêu cầu:** Viết chương trình tạo một danh bạ điện thoại và cho phép người dùng tra cứu số điện thoại.

**Hướng dẫn cách tiếp cận và giải bài:**
1. Tạo một dictionary chứa tên và số điện thoại.
2. Viết hàm tra cứu số điện thoại dựa trên tên.
3. Sử dụng hàm `get` để tra cứu và trả về số điện thoại hoặc thông báo nếu không tìm thấy.'''

def create_phonebook():
    phonebook = {
        "Alice": "123-456-7890",
        "Bob": "987-654-3210",
        "Charlie": "555-555-5555"
    }
    return phonebook

def lookup_phone(phonebook, name):
    return phonebook.get(name, "Không tìm thấy số điện thoại")

phonebook = create_phonebook()
name = "Alice"
print(f"Số điện thoại của {name}: {lookup_phone(phonebook, name)}")

'''#### Bài tập 8: Tính điểm trung bình của học sinh
**Yêu cầu:** Viết chương trình tính điểm trung bình của một học sinh với điểm của các môn học được lưu trữ trong dictionary.

**Hướng dẫn cách tiếp cận và giải bài:**
1. Duyệt qua các giá trị trong dictionary để tính tổng điểm.
2. Chia tổng điểm cho số lượng môn học để tính điểm trung bình.
'''

def calculate_average(grades):
    total = sum(grades.values())
    count = len(grades)
    return total / count

grades = {"Math": 85, "Science": 90, "English": 78}
average = calculate_average(grades)
print(f"Điểm trung bình: {average:.2f}")


'''#### Bài tập 9: Thêm và xóa khóa trong dictionary
**Yêu cầu:** Viết chương trình cho phép thêm và xóa khóa trong dictionary.

**Hướng dẫn cách tiếp cận và giải bài:**
1. Viết hàm để thêm cặp khóa-giá trị vào dictionary.
2. Viết hàm để xóa cặp khóa-giá trị khỏi dictionary.
'''
def add_subject(grades, subject, score):
    grades[subject] = score

def remove_subject(grades, subject):
    if subject in grades:
        del grades[subject]

grades = {"Math": 85, "Science": 90}
add_subject(grades, "English", 78)
print(f"Sau khi thêm môn English: {grades}")
remove_subject(grades, "Math")
print(f"Sau khi xóa môn Math: {grades}")

'''
#### Bài tập 10: Chuyển đổi danh sách các tuple thành dictionary
**Yêu cầu:** Viết chương trình chuyển đổi danh sách các tuple thành một dictionary.

**Hướng dẫn cách tiếp cận và giải bài:**
1. Sử dụng hàm `dict` để chuyển đổi danh sách các tuple thành dictionary.
'''

def list_to_dict(tuples):
    return dict(tuples)

list_of_tuples = [("name", "John"), ("age", 20), ("major", "Computer Science")]
student_dict = list_to_dict(list_of_tuples)
print(f"Dictionary: {student_dict}")

'''
### Bài Tập Kết Hợp Tuple và Dictionary

#### Bài tập 11: Tìm các phần tử không xuất hiện trong cả hai tuple
**Yêu cầu:** Viết chương trình tìm các phần tử không xuất hiện trong cả hai tuple.

**Hướng dẫn cách tiếp cận và giải bài:**
1. Chuyển đổi hai tuple thành tập hợp.
2. Sử dụng phép toán XOR của hai tập hợp để tìm các phần tử không chung.
3. Chuyển kết quả trở lại dạng tuple.
'''

def unique_elements(tuple1, tuple2):
    return tuple(set(tuple1) ^

 set(tuple2))

tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)
unique = unique_elements(tuple1, tuple2)
print(f"Các phần tử duy nhất: {unique}")

'''
#### Bài tập 12: Lưu trữ và tra cứu thông tin học sinh
**Yêu cầu:** Viết chương trình lưu trữ thông tin học sinh và cho phép tra cứu thông tin theo tên.

**Hướng dẫn cách tiếp cận và giải bài:**
1. Tạo một dictionary chứa thông tin học sinh.
2. Viết hàm tra cứu thông tin học sinh dựa trên tên.
'''

def create_student_records():
    students = {
        "John": {"age": 20, "major": "Computer Science"},
        "Jane": {"age": 22, "major": "Mathematics"}
    }
    return students

def lookup_student(students, name):
    return students.get(name, "Không tìm thấy học sinh")

students = create_student_records()
name = "John"
print(f"Thông tin của {name}: {lookup_student(students, name)}")

'''
#### Bài tập 13: Tính tổng các giá trị trong dictionary
**Yêu cầu:** Viết chương trình tính tổng các giá trị trong một dictionary.

**Hướng dẫn cách tiếp cận và giải bài:**
1. Sử dụng hàm `sum` để tính tổng các giá trị trong dictionary.
'''

def sum_values(d):
    return sum(d.values())

data = {"a": 10, "b": 20, "c": 30}
total = sum_values(data)
print(f"Tổng các giá trị: {total}")

'''
#### Bài tập 14: Tìm phần tử xuất hiện nhiều nhất trong tuple
**Yêu cầu:** Viết chương trình tìm phần tử xuất hiện nhiều nhất trong một tuple.

**Hướng dẫn cách tiếp cận và giải bài:**
1. Khởi tạo một dictionary để lưu trữ số lần xuất hiện của từng phần tử.
2. Duyệt qua các phần tử trong tuple và cập nhật số lần xuất hiện của chúng trong dictionary.
3. Tìm phần tử có số lần xuất hiện lớn nhất.
'''

def most_frequent_element(tup):
    frequency = {}
    for item in tup:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    most_frequent = max(frequency, key=frequency.get)
    return most_frequent

numbers = (1, 2, 3, 2, 4, 2, 5, 3)
most_frequent = most_frequent_element(numbers)
print(f"Phần tử xuất hiện nhiều nhất: {most_frequent}")

'''
#### Bài tập 15: Lưu trữ và hiển thị điểm số của học sinh theo môn học
**Yêu cầu:** Viết chương trình lưu trữ điểm số của học sinh theo môn học và hiển thị thông tin này.

**Hướng dẫn cách tiếp cận và giải bài:**
1. Tạo một dictionary chứa tên học sinh và dictionary điểm số của các môn học.
2. Viết hàm để hiển thị thông tin điểm số của từng học sinh.
'''

def display_grades(students):
    for student, grades in students.items():
        print(f"Điểm của {student}:")
        for subject, grade in grades.items():
            print(f"  {subject}: {grade}")

students = {
    "John": {"Math": 85, "Science": 90},
    "Jane": {"Math": 92, "Science": 88}
}
display_grades(students)

'''
#### Bài tập 16: Gộp các dictionary
**Yêu cầu:** Viết chương trình gộp hai dictionary lại với nhau.

**Hướng dẫn cách tiếp cận và giải bài:**
1. Sử dụng phương thức `update` để gộp hai dictionary.
'''

def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = merge_dicts(dict1, dict2)
print(f"Dictionary sau khi gộp: {merged_dict}")

'''
#### Bài tập 17: Sắp xếp dictionary theo giá trị
**Yêu cầu:** Viết chương trình sắp xếp dictionary theo giá trị.

**Hướng dẫn cách tiếp cận và giải bài:**
1. Sử dụng hàm `sorted` với tham số `key` để sắp xếp dictionary theo giá trị.
'''

def sort_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

data = {"a": 3, "b": 1, "c": 2}
sorted_data = sort_by_value(data)
print(f"Dictionary sau khi sắp xếp: {sorted_data}")

'''
#### Bài tập 18: Tạo danh sách các tuple từ dictionary
**Yêu cầu:** Viết chương trình tạo danh sách các tuple từ một dictionary.

**Hướng dẫn cách tiếp cận và giải bài:**
1. Sử dụng phương thức `items` của dictionary để lấy danh sách các cặp khóa-giá trị và chuyển đổi thành danh sách các tuple.
'''

def dict_to_list_of_tuples(d):
    return list(d.items())

data = {"name": "John", "age": 20, "major": "Computer Science"}
list_of_tuples = dict_to_list_of_tuples(data)
print(f"Danh sách các tuple: {list_of_tuples}")

'''
#### Bài tập 19: Tính tổng giá trị của các phần tử trong danh sách tuple
**Yêu cầu:** Viết chương trình tính tổng giá trị của các phần tử trong danh sách các tuple chứa số nguyên.

**Hướng dẫn cách tiếp cận và giải bài:**
1. Sử dụng vòng lặp để duyệt qua từng tuple trong danh sách và tính tổng các giá trị của các phần tử.
'''

def sum_of_tuples(tuples):
    total = 0
    for tup in tuples:
        total += sum(tup)
    return total

tuples = [(1, 2), (3, 4), (5, 6)]
total = sum_of_tuples(tuples)
print(f"Tổng giá trị: {total}")

'''
#### Bài tập 20: Lưu trữ và hiển thị thông tin sách trong thư viện
**Yêu cầu:** Viết chương trình lưu trữ thông tin sách trong thư viện và hiển thị danh sách các sách cùng với tác giả và năm xuất bản.

**Hướng dẫn cách tiếp cận và giải bài:**
1. Tạo một dictionary chứa thông tin sách với các chi tiết như tác giả và năm xuất bản.
2. Viết hàm để hiển thị thông tin sách trong thư viện.
'''

def display_books(library):
    for title, details in library.items():
        print(f"{title}:")
        for key, value in details.items():
            print(f"  {key}: {value}")

library = {
    "Book1": {"Author": "Author1", "Year": 2000},
    "Book2": {"Author": "Author2", "Year": 2010}
}
display_books(library)
