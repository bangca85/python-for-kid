
'''
Bài tập 14: Tìm phần tử xuất hiện nhiều nhất trong tuple

**Yêu cầu:** Viết chương trình tìm phần tử xuất hiện nhiều nhất trong một tuple.

**Input:**

```python
numbers = (1, 2, 3, 2, 4, 2, 5, 3)
```

**Output:**

```python
Phần tử xuất hiện nhiều nhất: 2
```
'''
def find_most_frequent(numbers):
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    # sử dụng hàm max với giá trị key là frequency.get
    most_frequent = max(frequency, key=frequency.get)
    return most_frequent

def find_most_frequent2(numbers):
    frequency = {}
    
    # Tạo từ điển lưu trữ tần suất xuất hiện của các số
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    
    # Tìm phần tử có tần suất xuất hiện nhiều nhất
    most_frequent = None
    max_count = 0
    
    for num, count in frequency.items():
        if count > max_count:
            max_count = count
            most_frequent = num
    
    return most_frequent


numbers = (1, 2, 3, 2, 4, 2, 5, 3)
most_frequent = find_most_frequent(numbers)
print(f"Phần tử xuất hiện nhiều nhất: {most_frequent}")
