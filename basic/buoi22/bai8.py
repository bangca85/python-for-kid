'''
### Bài tập 8: Phân tích kết quả khảo sát

#### Yêu cầu:

1. Nhập vào kết quả khảo sát của một nhóm người, mỗi kết quả bao gồm tên người trả lời và lựa chọn của họ (ví dụ: "Đồng ý", "Không đồng ý", "Không ý kiến").
2. Viết chức năng để đếm số lượng mỗi lựa chọn.
3. Viết chức năng để tìm và in ra lựa chọn phổ biến nhất.
4. Viết chức năng để hiển thị tỷ lệ phần trăm của mỗi lựa chọn trong tổng số lượt khảo sát.
5. Viết chức năng để lọc ra những người có lựa chọn là "Đồng ý" và in ra danh sách tên của họ.

#### Ví dụ:

```python
# Input: [("John", "Đồng ý"), ("Alice", "Không đồng ý"), ("Bob", "Đồng ý"), ("Eve", "Không ý kiến"), ("Charlie", "Đồng ý")]
# Output:
# Số lượng mỗi lựa chọn: {"Đồng ý": 3, "Không đồng ý": 1, "Không ý kiến": 1}
# Lựa chọn phổ biến nhất: Đồng ý
# Tỷ lệ phần trăm của mỗi lựa chọn: {"Đồng ý": 60.0%, "Không đồng ý": 20.0%, "Không ý kiến": 20.0%}
# Danh sách người chọn "Đồng ý": ["John", "Bob", "Charlie"]
```

---

'''
# Chức năng để đếm số lượng mỗi lựa chọn
def count_choices(survey_results):
    choice_counts = {}
    for name, choice in survey_results:
        if choice in choice_counts:
            choice_counts[choice] += 1
        else:
            choice_counts[choice] = 1
    return choice_counts

# Chức năng để tìm và in ra lựa chọn phổ biến nhất
# def find_most_popular_choice(choice_counts):
#     most_popular = max(choice_counts, key=choice_counts.get)
#     return most_popular
# Chức năng để tìm và in ra lựa chọn phổ biến nhất sử dụng vòng lặp for
def find_most_popular_choice(choice_counts):
    most_popular = None
    max_count = 0
    
    for choice, count in choice_counts.items():
        if count > max_count:
            most_popular = choice
            max_count = count
            
    return most_popular



# Chức năng để hiển thị tỷ lệ phần trăm của mỗi lựa chọn trong tổng số lượt khảo sát
def calculate_percentage(choice_counts, total_responses):
    percentages = {}
    for choice, count in choice_counts.items():
        percentages[choice] = (count / total_responses) * 100
    return percentages

# Chức năng để lọc ra những người có lựa chọn là "Đồng ý" và in ra danh sách tên của họ
def filter_agree(survey_results):
    agree_list = []
    for name, choice in survey_results:
        if choice == "Đồng ý":
            agree_list.append(name)
    return agree_list

# Chạy chương trình với dữ liệu mẫu
survey_results = [
    ("John", "Đồng ý"),
    ("Alice", "Không đồng ý"),
    ("Bob", "Đồng ý"),
    ("Eve", "Không ý kiến"),
    ("Charlie", "Đồng ý")
]

# Đếm số lượng mỗi lựa chọn
choice_counts = count_choices(survey_results)
print(f"Số lượng mỗi lựa chọn: {choice_counts}")

# Tìm lựa chọn phổ biến nhất
most_popular_choice = find_most_popular_choice(choice_counts)
print(f"Lựa chọn phổ biến nhất: {most_popular_choice}")

# Tính tỷ lệ phần trăm của mỗi lựa chọn
total_responses = len(survey_results)
percentages = calculate_percentage(choice_counts, total_responses)
percentages_formatted = {k: f"{v:.1f}%" for k, v in percentages.items()}
print(f"Tỷ lệ phần trăm của mỗi lựa chọn: {percentages_formatted}")

# Lọc và in ra danh sách người chọn "Đồng ý"
agree_list = filter_agree(survey_results)
print(f"Danh sách người chọn 'Đồng ý': {agree_list}")
