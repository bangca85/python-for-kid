'''
### Bài tập 2: Phân tích dữ liệu thi đấu thể thao

#### Yêu cầu:

1. Nhập vào danh sách các trận đấu, mỗi trận đấu bao gồm tên hai đội và số bàn thắng của từng đội.
2. Viết chức năng để tính tổng số bàn thắng mà mỗi đội đã ghi được trong tất cả các trận đấu.
3. Viết chức năng để tìm đội có số bàn thắng nhiều nhất.
4. Viết chức năng để sắp xếp và in ra bảng xếp hạng dựa trên số bàn thắng từ cao đến thấp.

#### Ví dụ:

```python
# Input: [("Team A", 2, "Team B", 1), ("Team C", 3, "Team A", 1), ("Team B", 2, "Team C", 2)]
# Output:
# Tổng số bàn thắng của mỗi đội: {"Team A": 3, "Team B": 3, "Team C": 5}
# Đội có số bàn thắng nhiều nhất: Team C
# Bảng xếp hạng: [("Team C", 5), ("Team A", 3), ("Team B", 3)]
```

---

'''

# 1. Sử dụng tuple để lưu trữ thông tin của mỗi trận đấu
matches = [
    ("Team A", 2, "Team B", 1),
    ("Team C", 3, "Team A", 1),
    ("Team B", 2, "Team C", 2)
]


# 2. hàm tính tổng số bàn thắng của một đội
def calculate_total_goals(matches):
    team_goals = {}
    for match in matches:
        team1, goals1, team2, goals2 = match
        
        # Cập nhật số bàn thắng cho đội 1
        if team1 in team_goals:
            team_goals[team1] += goals1
        else:
            team_goals[team1] = goals1
            
        # Cập nhật số bàn thắng cho đội 2
        if team2 in team_goals:
            team_goals[team2] += goals2
        else:
            team_goals[team2] = goals2
            
    return team_goals
# 3. hàm tìm đội có số bàn thắng nhiều nhất
def find_top_scorer(team_goals):
    top_team = None
    max_goals = 0
    for team, goals in team_goals.items():
        if goals > max_goals:
            max_goals = goals
            top_team = team
    return top_team


# 4. hàm sắp xếp và in ra bảng xếp hạng
def rank_teams(team_goals):
    # Chuyển đổi từ điển thành danh sách các tuple (team, goals)
    items = list(team_goals.items())

    # Sắp xếp danh sách dựa trên số bàn thắng (goals) bằng cách sử dụng thuật toán sắp xếp cơ bản (bubble sort)
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j][1] < items[j + 1][1]:
                # Hoán đổi nếu số bàn thắng của team thứ j nhỏ hơn team thứ j+1
                items[j], items[j + 1] = items[j + 1], items[j]

    return items
######## - chạy chương trình chính
# Tính tổng số bàn thắng của mỗi đội
team_goals = calculate_total_goals(matches)
print("Tổng số bàn thắng của mỗi đội:", team_goals)

# Tìm đội có số bàn thắng nhiều nhất
top_scorer = find_top_scorer(team_goals)
print("Đội có số bàn thắng nhiều nhất:", top_scorer)

# Sắp xếp và in ra bảng xếp hạng
ranking = rank_teams(team_goals)
print("Bảng xếp hạng:", ranking)