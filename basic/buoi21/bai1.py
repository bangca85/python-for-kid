'''
### Bài tập 1: Phân tích danh sách điểm số

#### Yêu cầu:

1. Nhập vào danh sách điểm số của học sinh từ bàn phím (mỗi điểm cách nhau bởi dấu phẩy).
2. Tính và in ra điểm số trung bình.
3. Tìm và in ra điểm cao nhất và thấp nhất.
4. In ra danh sách các điểm số đã được sắp xếp theo thứ tự tăng dần.

#### Ví dụ:

# Input: 85, 92, 78, 90, 88
# Output:
# Điểm trung bình: 86.6
# Điểm cao nhất: 92
# Điểm thấp nhất: 78
# Danh sách điểm sắp xếp: [78, 85, 88, 90, 92]

'''

# 1. Nhập danh sách điểm số từ bàn phím
scores_input = input("Nhập danh sách điểm số, cách nhau bởi dấu phẩy:")
# Cắt chuỗi thành mảng
scores_array_string =  scores_input.split(",")
# Chuyển đổi mảng thành mảng số
scores_int = map(int, scores_array_string)
# chuyển mảng thành danh sách
scores = list(scores_int)

# 2. Tính và in ra điểm số trung bình
average_score = sum(scores) / len(scores)
print(f"Điểm trung bình: {average_score:.1f}")

# 3. Tìm và in ra điểm cao nhất và thấp nhất
max_score = max(scores)
min_score = min(scores)
print(f"Điểm cao nhất: {max_score}")
print(f"Điểm thấp nhất: {min_score}")

# 4. In ra danh sách các điểm số đã được sắp xếp theo thứ tự tăng dần
sorted_scores = sorted(scores)
print(f"Danh sách điểm sắp xếp: {sorted_scores}")
