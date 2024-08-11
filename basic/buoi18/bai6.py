'''
Bài tập 6: Đếm số lần xuất hiện của các ký tự trong chuỗi

**Yêu cầu:** Viết chương trình đếm số lần xuất hiện của mỗi ký tự trong một chuỗi.

**Input:**

```python
text = "hello world"
```

**Output:**

```python
Số lần xuất hiện của các ký tự: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```
'''

def count_characters(text):
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

text = "hello world"
char_count = count_characters(text)
print(f"Số lần xuất hiện của các ký tự: {char_count}")
