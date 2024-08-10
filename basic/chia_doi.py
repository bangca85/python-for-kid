import random
print("start")
team_members = ["Bằng", "Bảo", "Phúc", "Quyền", "Thịnh", "Thuật", "Trung", "Tú", "Văn", "Thương"]

# Thành viên đã chọn đội
team_red = ["Bảo", "Quyền", "Thịnh"]
team_blue = ["Trung", "Thương", "Phúc"]
 
remaining_members = [member for member in team_members if member not in team_red + team_blue]
 
random.shuffle(remaining_members)
 
for i, member in enumerate(remaining_members):
    if i % 2 == 0:
        team_red.append(member)
    else:
        team_blue.append(member)

print("Đội Đỏ:", team_red)
print("Đội Xanh:", team_blue)