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
Ý tưởng chính:
Đếm số lần xuất hiện của mỗi ký tự.
Sử dụng một danh sách để theo dõi vị trí tiếp theo mà mỗi ký tự có thể xuất hiện hợp lệ.
Lặp qua mỗi vị trí trong kết quả, tại mỗi bước, chọn ký tự có số lần xuất hiện lớn nhất và có thể đặt tại vị trí hiện tại.
Cập nhật số lần xuất hiện và vị trí tiếp theo của ký tự đó.

function rearrangeString(s, k):
    if k == 0:
        return s
    
    # Đếm số lần xuất hiện của từng ký tự
    char_count = Counter(s)
    
    # Sử dụng max_heap để lưu trữ các ký tự theo số lần xuất hiện
    max_heap = PriorityQueue()
    for char, count in char_count.items():
        max_heap.put((-count, char))
    
    # Kết quả cuối cùng
    result = [''] * len(s)
    # Danh sách để theo dõi vị trí tiếp theo mà mỗi ký tự có thể xuất hiện hợp lệ
    next_valid_position = {}
    
    for i in range(len(s)):
        if max_heap.empty():
            return ""
        
        count, char = max_heap.get()
        while char in next_valid_position and next_valid_position[char] > i:
            if max_heap.empty():
                return ""
            count, char = max_heap.get()
        
        result[i] = char
        next_valid_position[char] = i + k
        
        if -count > 1:
            max_heap.put((count + 1, char))
    
    return ''.join(result)


'''
from collections import Counter
from queue import PriorityQueue

def rearrangeString(s, k):
    if k == 0:
        return s

    # Đếm số lần xuất hiện của từng ký tự
    char_count = Counter(s)
    
    # Sử dụng max_heap để lưu trữ các ký tự theo số lần xuất hiện
    max_heap = PriorityQueue()
    for char, count in char_count.items():
        max_heap.put((-count, char))
    
    # Kết quả cuối cùng
    result = [''] * len(s)
    # Danh sách để theo dõi vị trí tiếp theo mà mỗi ký tự có thể xuất hiện hợp lệ
    next_valid_position = {}
    
    for i in range(len(s)):
        if max_heap.empty():
            return ""
        
        count, char = max_heap.get()
        while char in next_valid_position and next_valid_position[char] > i:
            if max_heap.empty():
                return ""
            count, char = max_heap.get()
        
        result[i] = char
        next_valid_position[char] = i + k
        
        if -count > 1:
            max_heap.put((count + 1, char))
    
    return ''.join(result)

# Ví dụ sử dụng
s = "aabbcc"
k = 3
result = rearrangeString(s, k)
print("Rearranged string:", result)
