'''
### Bài tập 18: Quản lý dữ liệu về nhân khẩu học

#### Yêu cầu:

1. Tạo một từ điển để lưu trữ thông tin về dân số của các khu vực, bao gồm tên khu vực, số dân và diện tích.
2. Viết chức năng để thêm hoặc cập nhật thông tin dân số cho một khu vực.
3. Viết chức năng để tính mật độ dân số (số dân trên mỗi km²) của từng khu vực và thêm vào từ điển.
4. Viết chức năng để sắp xếp và in ra danh sách các khu vực theo mật độ dân số từ cao đến thấp.

#### Ví dụ:

```python
# Input: {"Quận 1": {"số dân": 200000, "diện tích": 20}, "Quận 2": {"số dân": 150000, "diện tích": 30}}
# Output:
# Cập nhật dân số: {"Quận 1": {"số dân": 200000, "diện tích": 20}, "Quận 2": {"số dân": 150000, "diện tích": 30}}
# Mật độ dân số: {"Quận 1": 10000, "Quận 2": 5000}
# Danh sách khu vực theo mật độ dân số: [{"Quận 1": 10000}, {"Quận 2": 5000}]
```

---
'''

# 1. Thêm hoặc cập nhật thông tin dân số cho một khu vực
def update_population(areas, area_name, population, area_size):
    areas[area_name] = {"số dân": population, "diện tích": area_size}
    return areas

# 2. Tính mật độ dân số của từng khu vực và thêm vào từ điển
def calculate_density(areas):
    density_dict = {}
    for area_name, info in areas.items():
        density = info["số dân"] / info["diện tích"]
        density_dict[area_name] = density
    return density_dict

# 3. Sắp xếp và in ra danh sách các khu vực theo mật độ dân số từ cao đến thấp
def sort_areas_by_density(density_dict):
    sorted_areas = list(density_dict.items())  # Chuyển đổi thành danh sách các tuple
    # Sắp xếp theo phương pháp đơn giản (bubble sort)
    for i in range(len(sorted_areas)):
        for j in range(i + 1, len(sorted_areas)):
            if sorted_areas[i][1] < sorted_areas[j][1]:  # So sánh mật độ dân số
                # Hoán đổi vị trí nếu phần tử hiện tại có mật độ nhỏ hơn phần tử sau nó
                sorted_areas[i], sorted_areas[j] = sorted_areas[j], sorted_areas[i]
    return sorted_areas

# Chạy các chức năng và in kết quả
# Danh sách các khu vực với số dân và diện tích
areas = {
    "Quận 1": {"số dân": 200000, "diện tích": 20},
    "Quận 2": {"số dân": 150000, "diện tích": 30}
}

# Cập nhật dân số cho "Quận 2"
areas = update_population(areas, "Quận 2", 150000, 30)
print(f"Cập nhật dân số: {areas}")

# Tính mật độ dân số
density_dict = calculate_density(areas)
print(f"Mật độ dân số: {density_dict}")

# Sắp xếp khu vực theo mật độ dân số
sorted_areas = sort_areas_by_density(density_dict)
print(f"Danh sách khu vực theo mật độ dân số: {sorted_areas}")
