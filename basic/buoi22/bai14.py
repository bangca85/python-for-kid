'''
### Bài tập 14: Quản lý thời khóa biểu của sinh viên

#### Yêu cầu:

1. Nhập vào thời khóa biểu của sinh viên, mỗi ngày bao gồm các môn học và thời gian học.
2. Viết chức năng để thêm hoặc cập nhật thời khóa biểu cho một ngày cụ thể.
3. Viết chức năng để tìm và in ra ngày có số lượng môn học nhiều nhất.
4. Viết chức năng để sắp xếp và in ra thời khóa biểu của các ngày trong tuần theo số lượng môn học từ ít đến nhiều.

#### Ví dụ:

```python
# Input: {"Thứ Hai": {"Toán": "08:00-09:30", "Lý": "09:45-11:15"}, "Thứ Ba": {"Hóa": "08:00-09:30"}}
# Output:
# Cập nhật thời khóa biểu: {"Thứ Hai": {"Toán": "08:00-09:30", "Lý": "09:45-11:15"}, "Thứ Ba": {"Hóa": "08:00-09:30", "Anh Văn": "09:45-11:15"}}
# Ngày có số lượng môn học nhiều nhất: Thứ Hai
# Thời khóa biểu theo số lượng môn học: [{"Thứ Ba": 2 môn}, {"Thứ Hai": 2 môn}]
```

---
'''
# 2. Hàm thêm hoặc cập nhật thời khoá biểu cho 1 ngày cụ thể
def update_schedule(schedule, day, subject, time):
    if day in schedule:
        schedule[day][subject] = time
    else:
        schedule[day] = {subject: time}
    return schedule

# 3. Hàm tìm và in ra ngày có số lượng môn học nhiều nhất.
def find_day_with_most_subjects(schedule):
    max_day = None
    max_subjects = 0
    for day, subjects in schedule.items():
        if len(subjects) > max_subjects:
            max_subjects = len(subjects)
            max_day = day
    return max_day

# 4. Hàm sắp xếp và in ra thời khóa biểu của các ngày trong tuần theo số lượng môn học từ ít đến nhiều.
def sort_schedule_by_subject_count(schedule):
    sorted_schedule = []
    for day in sorted(schedule, key=lambda d: len(schedule[d])):
        sorted_schedule.append((day, len(schedule[day])))
    return sorted_schedule

#### Chương trình chính  ######
schedule = {
    "Thứ Hai": {"Toán": "08:00-09:30", "Lý": "09:45-11:15"},
    "Thứ Ba": {"Hóa": "08:00-09:30"}
}

# Cập nhật thời khóa biểu cho Thứ Ba
schedule = update_schedule(schedule, "Thứ Ba", "Anh Văn", "09:45-11:15")
print("Cập nhật thời khóa biểu:", schedule)
# Tìm ngày có số lượng môn học nhiều nhất
max_day = find_day_with_most_subjects(schedule)
print(f"Ngày có số lượng môn học nhiều nhất: {max_day}")
# Sắp xếp và in ra thời khóa biểu
sorted_schedule = sort_schedule_by_subject_count(schedule)
print("Thời khóa biểu theo số lượng môn học:", sorted_schedule)