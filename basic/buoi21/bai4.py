'''
Bài tập 4: Phân tích văn bản

#### Yêu cầu:

1. Nhập vào một đoạn văn bản từ bàn phím.
2. Đếm và in ra số lượng từ trong văn bản.
3. Tìm và in ra từ dài nhất trong đoạn văn bản.
4. Tạo và in ra một từ điển lưu trữ số lần xuất hiện của mỗi từ trong đoạn văn bản.

#### Ví dụ:

# Input: "Học Python rất thú vị và bổ ích. Python là ngôn ngữ lập trình mạnh mẽ."
# Output:
# Số lượng từ: 12
# Từ dài nhất: "lập trình"
# Từ điển tần suất: {"Học": 1, "Python": 2, "rất": 1, "thú": 1, "vị": 1, "và": 1, "bổ ích": 1, "là": 1, "ngôn ngữ": 1, "lập trình": 1, "mạnh mẽ": 1}

'''
# 1. Nhập vào một đoạn văn bản từ bàn phím
text = input("Nhập đoạn văn bản: ")

# 2. Đếm và in ra số lượng từ trong văn bản
words = text.split()
word_count = len(words)
print(f"Số lượng từ: {word_count}")

# 3. Tìm và in ra từ dài nhất trong đoạn văn bản
# dùng lệnh max để xác định
#longest_word = max(words, key=len)
# hoặc dùng các lệnh cơ bản như bên dưới
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(f"Từ dài nhất: {longest_word}")

# 4. Tạo và in ra một từ điển lưu trữ số lần xuất hiện của mỗi từ trong đoạn văn bản
word_frequency = {}
for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1
print(f"Từ điển tần suất: {word_frequency}")
