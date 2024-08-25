'''
### Bài tập 17: Quản lý và phân tích ngân sách dự án

#### Yêu cầu:

1. Tạo một từ điển để lưu trữ thông tin ngân sách của các dự án, bao gồm tên dự án, ngân sách dự kiến, và chi phí thực tế.
2. Viết chức năng để thêm hoặc cập nhật thông tin ngân sách cho một dự án.
3. Viết chức năng để tính tổng ngân sách dự kiến và tổng chi phí thực tế của tất cả các dự án.
4. Viết chức năng để tìm và in ra các dự án vượt quá ngân sách dự kiến.

#### Ví dụ:

```python
# Input: {"Dự án A": {"ngân sách dự kiến": 5000, "chi phí thực tế": 6000}, "Dự án B": {"ngân sách dự kiến": 3000, "chi phí thực tế": 2500}}
# Output:
# Cập nhật ngân sách: {"Dự án A": {"ngân sách dự kiến": 5000, "chi phí thực tế": 6000}, "Dự án B": {"ngân sách dự kiến": 3000, "chi phí thực tế": 3000}}
# Tổng ngân sách dự kiến: 8000
# Tổng chi phí thực tế: 9000
# Dự án vượt ngân sách: Dự án A
```

'''

# 2. Thêm hoặc cập nhật thông tin ngân sách cho một dự án
def update_project_budget(projects, project_name, estimated_budget, actual_cost):
    projects[project_name] = {"ngân sách dự kiến": estimated_budget, "chi phí thực tế": actual_cost}
    return projects

# 3. Tính tổng ngân sách dự kiến và tổng chi phí thực tế của tất cả các dự án
def calculate_totals(projects):
    total_estimated_budget = 0
    total_actual_cost = 0
    for project in projects.values():
        total_estimated_budget += project["ngân sách dự kiến"]
        total_actual_cost += project["chi phí thực tế"]
    return total_estimated_budget, total_actual_cost

# 4. Tìm và in ra các dự án vượt quá ngân sách dự kiến
def find_over_budget_projects(projects):
    over_budget_projects = []
    for project_name, budget in projects.items():
        if budget["chi phí thực tế"] > budget["ngân sách dự kiến"]:
            over_budget_projects.append(project_name)
    return over_budget_projects

### Chạy chương trình chính ###
# Danh sách các dự án với ngân sách dự kiến và chi phí thực tế
projects = {
    "Dự án A": {"ngân sách dự kiến": 5000, "chi phí thực tế": 6000},
    "Dự án B": {"ngân sách dự kiến": 3000, "chi phí thực tế": 2500}
}

# Cập nhật ngân sách cho "Dự án B"
projects = update_project_budget(projects, "Dự án B", 3000, 3000)
print(f"Cập nhật ngân sách: {projects}")

# Tính tổng ngân sách dự kiến và chi phí thực tế
total_estimated_budget, total_actual_cost = calculate_totals(projects)
print(f"Tổng ngân sách dự kiến: {total_estimated_budget}")
print(f"Tổng chi phí thực tế: {total_actual_cost}")

# Tìm các dự án vượt ngân sách
over_budget_projects = find_over_budget_projects(projects)
print(f"Dự án vượt ngân sách: {', '.join(over_budget_projects)}")
