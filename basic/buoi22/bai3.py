'''
### Bài tập 3: Xử lý chuỗi và phân tích văn bản

#### Yêu cầu:

1. Nhập vào một đoạn văn bản từ bàn phím.
2. Viết chức năng để đếm số lần xuất hiện của mỗi ký tự trong văn bản (bao gồm cả khoảng trắng và dấu câu).
3. Viết chức năng để xác định và in ra ký tự xuất hiện nhiều nhất.
4. Viết chức năng để mã hóa văn bản bằng cách thay thế mỗi ký tự bằng ký tự tiếp theo trong bảng chữ cái (ví dụ: 'a' -> 'b', 'b' -> 'c', ...).

#### Ví dụ:

```python
# Input: "Hello World!"
# Output:
# Tần suất xuất hiện của mỗi ký tự: {"H": 1, "e": 1, "l": 3, "o": 2, " ": 1, "W": 1, "r": 1, "d": 1, "!": 1}
# Ký tự xuất hiện nhiều nhất: l
# Văn bản mã hóa: "Ifmmp Xpsme!"
```

---
'''


# 2. Viết hàm đếm so lần xuất hiện một ký tự
def count_characters(text):
    character_count = {}
    for char in text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

# 3. Viết hàm xác định và in ra ký tự xuất hiện nhiều nhất
def find_most_frequent_character(character_count):
    max_char = None
    max_count = 0
    for char, count in character_count.items():
        if count > max_count:
            max_count = count
            max_char = char
    return max_char
# 4. Viết hàm mã hoá và thay thế một ký tự bằng ký tự tiếp theo
# 
'''
Hàm chr() nhận vào một giá trị ASCII và trả về ký tự tương ứng.
Hàm ord() nhận vào một ký tự và trả về giá trị ASCII tương ứng của ký tự đó.
Giả sử char = 'a':

ord('a') trả về 97.
ord('a') + 1 là 98.
chr(98) trả về 'b'.
'''
def encrypt_text(text):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Chỉ mã hóa ký tự chữ cái
            if char == 'z':
                encrypted_text += 'a'
            elif char == 'Z':
                encrypted_text += 'A'
            else:
                encrypted_text += chr(ord(char) + 1)
        else:
            encrypted_text += char
    return encrypted_text

######### -- chạy chương trình chính ##########
# 1. Nhap vao van ban
text = input("Nhập đoạn văn bản: ")

# Đếm số lần xuất hiện của mỗi ký tự
character_count = count_characters(text)
print("Tần suất xuất hiện của mỗi ký tự:", character_count)

# Xác định ký tự xuất hiện nhiều nhất
most_frequent_char = find_most_frequent_character(character_count)
print("Ký tự xuất hiện nhiều nhất:", most_frequent_char)

# Mã hóa văn bản
encrypted_text = encrypt_text(text)
print("Văn bản mã hóa:", encrypted_text)