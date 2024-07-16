'''
Bài toán: Sắp xếp các chữ cái trong từ có khoảng cách tối thiểu (Rearrange Characters with Minimum Distance)
Vấn đề:
Cho một chuỗi s và một số nguyên k, hãy viết một hàm để sắp xếp lại các chữ cái trong chuỗi sao cho không có hai chữ cái giống nhau nào cách nhau ít hơn k vị trí. Nếu không thể sắp xếp được, trả về một chuỗi rỗng.

Ví dụ:
Input: s = "aabbcc", k = 3

Output: "abcabc"

Giải thích: Các chữ cái a, b, và c được sắp xếp sao cho không có chữ cái nào cách nhau ít hơn 3 vị trí.

Input: s = "aaabc", k = 3

Output: ""

Giải thích: Không thể sắp xếp lại chuỗi để các chữ cái giống nhau cách nhau ít nhất 3 vị trí.


'''

'''
Cách giải: Sử dụng Đếm Tần Số và Xây Dựng Kết Quả Trực Tiếp
Ý tưởng chính:
Đếm số lần xuất hiện của từng ký tự.
Sử dụng một danh sách để theo dõi các vị trí mà mỗi ký tự có thể được chèn vào, đảm bảo khoảng cách k giữa các ký tự giống nhau.
Tạo kết quả bằng cách chèn các ký tự vào các vị trí hợp lệ.
Cách tiếp cận chi tiết:
Đếm số lần xuất hiện của từng ký tự.
Sắp xếp các ký tự theo số lần xuất hiện giảm dần.
Sử dụng một danh sách để theo dõi các vị trí hợp lệ cho mỗi ký tự.
Chèn các ký tự vào vị trí hợp lệ, đảm bảo khoảng cách k giữa các ký tự giống nhau.
function rearrangeString(s, k):
    if k == 0:
        return s
    
    # Đếm số lần xuất hiện của từng ký tự
    char_count = Counter(s)
    
    # Sắp xếp các ký tự theo số lần xuất hiện giảm dần
    sorted_chars = sorted(char_count, key=lambda x: -char_count[x])
    
    # Tạo kết quả với các vị trí trống
    result = [''] * len(s)
    
    # Chỉ số hiện tại để chèn ký tự
    current_index = 0
    
    for char in sorted_chars:
        count = char_count[char]
        while count > 0:
            # Nếu vượt quá độ dài chuỗi, bắt đầu lại từ vị trí tiếp theo trong khoảng cách k
            if current_index >= len(s):
                current_index = (current_index % k) + 1
                if result[current_index] != '':
                    return ""
            
            # Chèn ký tự vào vị trí hiện tại và di chuyển đến vị trí hợp lệ tiếp theo
            if result[current_index] == '':
                result[current_index] = char
                current_index += k
                count -= 1
            else:
                current_index += 1
        
    return ''.join(result)

'''
from collections import Counter

def rearrangeString(s, k):
    if k == 0:
        return s

    # Đếm số lần xuất hiện của từng ký tự
    char_count = Counter(s)
    
    # Sắp xếp các ký tự theo số lần xuất hiện giảm dần
    sorted_chars = sorted(char_count, key=lambda x: -char_count[x])
    
    # Tạo kết quả với các vị trí trống
    result = [''] * len(s)
    
    # Chỉ số hiện tại để chèn ký tự
    current_index = 0
    
    for char in sorted_chars:
        count = char_count[char]
        while count > 0:
            # Nếu vượt quá độ dài chuỗi, bắt đầu lại từ vị trí tiếp theo trong khoảng cách k
            if current_index >= len(s):
                current_index = (current_index % k) + 1
                if result[current_index] != '':
                    return ""
            
            # Chèn ký tự vào vị trí hiện tại và di chuyển đến vị trí hợp lệ tiếp theo
            if result[current_index] == '':
                result[current_index] = char
                current_index += k
                count -= 1
            else:
                current_index += 1
    
    return ''.join(result)

# Ví dụ sử dụng
s = "aabbcc"
k = 3
result = rearrangeString(s, k)
print("Rearranged string:", result)
