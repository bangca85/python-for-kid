'''
Bài tập 9: Quản lý hệ thống đặt vé xem phim

#### Yêu cầu:

1. Tạo một từ điển để lưu trữ thông tin về các bộ phim và số lượng vé còn lại.
2. Viết chức năng cho phép người dùng đặt vé cho một bộ phim cụ thể, cập nhật lại số lượng vé còn lại.
3. Viết chức năng để kiểm tra số lượng vé còn lại của một bộ phim bất kỳ.
4. Viết chức năng để hiển thị danh sách tất cả các bộ phim còn vé và sắp xếp theo số lượng vé còn lại từ cao đến thấp.

#### Ví dụ:

```python
# Input: {"Avatar": 50, "Inception": 20, "Titanic": 0}
# Output:
# Đặt vé cho Inception, còn lại 19 vé.
# Số lượng vé còn lại cho Avatar: 50
# Danh sách phim còn vé: {"Avatar": 50, "Inception": 19}
```

---
'''

# Chức năng thêm hoặc cập nhật thông tin bộ phim
def add_or_update_movie(movies, movie_name, tickets):
    movies[movie_name] = tickets

# Chức năng đặt vé cho một bộ phim cụ thể
def book_ticket(movies, movie_name):
    if movies.get(movie_name, 0) > 0:
        movies[movie_name] -= 1
        print(f"Đặt vé cho {movie_name}, còn lại {movies[movie_name]} vé.")
    else:
        print(f"{movie_name} đã hết vé hoặc không tồn tại.")

# Chức năng kiểm tra số lượng vé còn lại của một bộ phim bất kỳ
def check_tickets(movies, movie_name):
    remaining_tickets = movies.get(movie_name, "Phim không tồn tại.")
    print(f"Số lượng vé còn lại cho {movie_name}: {remaining_tickets}")

# Chức năng hiển thị danh sách các bộ phim còn vé và sắp xếp theo số lượng vé còn lại# Chức năng hiển thị danh sách các bộ phim còn vé và sắp xếp theo số lượng vé còn lại
def list_movies_with_tickets(movies):
    available_movies = {}
    
    # Lọc các bộ phim còn vé
    for movie, tickets in movies.items():
        if tickets > 0:
            available_movies[movie] = tickets
    
    # Sắp xếp các bộ phim theo số lượng vé còn lại
    sorted_movies = []
    movie_list = list(available_movies.items())
    
    for i in range(len(movie_list)):
        for j in range(i + 1, len(movie_list)):
            if movie_list[i][1] < movie_list[j][1]:
                movie_list[i], movie_list[j] = movie_list[j], movie_list[i]
    
    # Chuyển danh sách đã sắp xếp thành từ điển
    sorted_movies = {movie: tickets for movie, tickets in movie_list}
    
    print(f"Danh sách phim còn vé: {sorted_movies}")
    return sorted_movies


# Chương trình chính 

# Tạo từ điển chứa thông tin bộ phim và số lượng vé
movies = {"Avatar": 50, "Inception": 20, "Titanic": 0}

# Đặt vé cho Inception
book_ticket(movies, "Inception")

# Kiểm tra số lượng vé còn lại của Avatar
check_tickets(movies, "Avatar")

# Hiển thị danh sách các bộ phim còn vé và sắp xếp theo số lượng vé còn lại
list_movies_with_tickets(movies)
