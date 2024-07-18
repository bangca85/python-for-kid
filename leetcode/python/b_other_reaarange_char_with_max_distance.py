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

Testcase 3:
s = "aaadbbcc"
k = 2
output:
"abacabcd"

Testcase 4:
s = "aaaa"
k = 2
Output:
"aaaa"
=> chỉ 1 ký tự a không cần giữ khoảng cách

Testcase 5:
s = "aaabbb"
k = 2

Output:
"ababab"
Các ký tự 'a' và 'b' đều xuất hiện với khoảng cách ít nhất là 2 vị trí.

Testcase 6:
s = "aaabbbccc"
k = 3

"abcabcabc"
Các ký tự 'a', 'b', và 'c' đều xuất hiện với khoảng cách ít nhất là 3 vị trí.

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
from collections import Counter, deque
import heapq

def rearrangeString(s, k):
    if k == 0:
        return s

    # Đếm số lần xuất hiện của từng ký tự
    char_count = Counter(s)
    
    # Nếu chỉ có một loại ký tự duy nhất, trả về chuỗi đó
    if len(char_count) == 1:
        return s
    
    # Sử dụng max_heap để lưu trữ các ký tự theo số lần xuất hiện giảm dần
    max_heap = [(-count, char) for char, count in char_count.items()]
    # print(max_heap)
    heapq.heapify(max_heap)
    
    # Hàng đợi để theo dõi các ký tự đã sử dụng
    wait_queue = deque()
    result = []

    while max_heap:
        count, char = heapq.heappop(max_heap)
        result.append(char)
        wait_queue.append((char, count + 1))
        
        # Nếu hàng đợi chờ có đủ k phần tử, đưa phần tử trở lại hàng đợi ưu tiên nếu còn xuất hiện
        if len(wait_queue) >= k:
            ready_char, ready_count = wait_queue.popleft()
            if ready_count < 0:
                heapq.heappush(max_heap, (ready_count, ready_char))

    # Nếu kết quả có độ dài bằng chuỗi ban đầu, trả về kết quả
    if len(result) == len(s):
        return ''.join(result)
    
    return ""

# Testcase mới
def run_tests():
    test_cases = [
        ("aabbcc", 3, "abcabc"),
        ("aaabc", 3, ""),
        ("aaadbbcc", 2, "abacabcd"),
        ("aaaa", 2, "aaaa"),
        ("aaabbb", 2, "ababab"),
        ("aaabbbccc", 3, "abcabcabc"),
        # ("aaabbbbcc", 2, "ababcbabc"),
        ("a", 2, "a"),
        ("aabbccddeeff", 4, "abcdefabcdef"),
        ("aabbccdd", 1, "aabbccdd"),
    ]

    for s, k, expected in test_cases:
        result = rearrangeString(s, k)
        assert result == expected, f"Test failed for input {s}, {k}. Expected {expected}, but got {result}"
        print(f"Test passed for input {s}, {k}. Got {result}")

# Chạy các testcase
run_tests()
