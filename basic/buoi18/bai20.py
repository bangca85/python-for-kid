'''
Bài tập 20: Lưu trữ và hiển thị thông tin sách trong thư viện

**Yêu cầu:** Viết chương trình lưu trữ thông tin sách trong thư viện và hiển thị danh sách các sách cùng với tác giả và năm xuất bản.

**Input:**

```python
library = {
    "Book1": {"Author": "Author1", "Year": 2000},
    "Book2": {"Author": "Author2", "Year": 2010}
}
```

**Output:**

```python
Book1:
  Author: Author1
  Year: 2000
Book2:
  Author: Author2
  Year: 2010
```
'''
def display_library_books(library):
    for book, info in library.items():
        print(f"{book}:")
        for key, value in info.items():
            print(f"  {key}: {value}")

library = {
    "Book1": {"Author": "Author1", "Year": 2000},
    "Book2": {"Author": "Author2", "Year": 2010}
}

display_library_books(library)
