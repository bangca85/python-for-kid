'''
#### Bài tập 1: Tính khoảng cách giữa hai điểm

**Yêu cầu:** Viết chương trình tính khoảng cách giữa hai điểm trong không gian 2D. Các tọa độ điểm được lưu trữ trong tuple.

**Input:**

```python
point1 = (3, 4)
point2 = (7, 1)
```

**Output:**

```python
Khoảng cách giữa (3, 4) và (7, 1) là 5.00
```
'''
import math

def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

point1 = (3, 4)
point2 = (7, 1)

distance = calculate_distance(point1, point2)
print(f"Khoảng cách giữa {point1} và {point2} là {distance:.2f}")
