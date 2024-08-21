
### Bài tập 1: Quản lý kho hàng

#### Yêu cầu:

1. Tạo một từ điển để lưu trữ thông tin sản phẩm trong kho, bao gồm tên sản phẩm, số lượng và giá mỗi đơn vị.
2. Viết chức năng cho phép thêm mới hoặc cập nhật sản phẩm trong kho (nếu sản phẩm đã tồn tại, chỉ cập nhật số lượng và giá).
3. Viết chức năng để tính tổng giá trị của kho hàng.
4. Viết chức năng để tìm và in ra sản phẩm có giá trị cao nhất trong kho (tính bằng giá mỗi đơn vị * số lượng).

#### Ví dụ:

```python
# Input: {"Sản phẩm A": {"số lượng": 10, "giá": 50}, "Sản phẩm B": {"số lượng": 5, "giá": 100}}
# Output:
# Cập nhật kho hàng: {"Sản phẩm A": {"số lượng": 10, "giá": 50}, "Sản phẩm B": {"số lượng": 8, "giá": 100}}
# Tổng giá trị kho hàng: 1600
# Sản phẩm có giá trị cao nhất: Sản phẩm B với giá trị 800
```

---

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

### Bài tập 3: Xử lý chuỗi và phân tích văn bản

#### Yêu cầu:

1. Nhập vào một đoạn văn bản từ bàn phím.
2. Viết chức năng để đếm số lần xuất hiện của mỗi ký tự trong văn bản (bao gồm cả khoảng trắng và dấu câu).
3. Viết chức năng để xác định và in ra ký tự xuất hiện nhiều nhất.
4. Viết chức năng để mã hóa văn bản bằng cách thay thế mỗi ký tự bằng ký tự tiếp theo trong bảng chữ cái (ví dụ: 'a' -> 'b', 'b' -> 'c', ...).

#### Ví dụ:

```python
# Input: "Hello World!"
# Output:
# Tần suất xuất hiện của mỗi ký tự: {"H": 1, "e": 1, "l": 3, "o": 2, " ": 1, "W": 1, "r": 1, "d": 1, "!": 1}
# Ký tự xuất hiện nhiều nhất: l
# Văn bản mã hóa: "Ifmmp Xpsme!"
```

---

### Bài tập 4: Quản lý danh sách học sinh và điểm số nâng cao

#### Yêu cầu:

1. Tạo một từ điển lưu trữ danh sách học sinh và danh sách điểm số của họ cho từng môn học.
2. Viết chức năng để tính điểm trung bình của mỗi học sinh.
3. Viết chức năng để xếp hạng các học sinh dựa trên điểm trung bình từ cao đến thấp.
4. Viết chức năng để tìm học sinh có điểm trung bình cao nhất và thấp nhất.

#### Ví dụ:

```python
# Input: {"John": {"Toán": 85, "Lý": 78, "Hóa": 92}, "Alice": {"Toán": 88, "Lý": 95, "Hóa": 80}}
# Output:
# Điểm trung bình của mỗi học sinh: {"John": 85.0, "Alice": 87.67}
# Xếp hạng học sinh: [("Alice", 87.67), ("John", 85.0)]
# Học sinh có điểm trung bình cao nhất: Alice
# Học sinh có điểm trung bình thấp nhất: John
```

---

### Bài tập 5: Quản lý thông tin nhân viên

#### Yêu cầu:

1. Tạo một từ điển lưu trữ thông tin nhân viên, bao gồm tên, tuổi, phòng ban, và mức lương.
2. Viết chức năng để thêm mới hoặc cập nhật thông tin nhân viên.
3. Viết chức năng để tìm và in ra nhân viên có mức lương cao nhất và thấp nhất.
4. Viết chức năng để tính tổng lương mà công ty phải chi trả cho tất cả nhân viên.

#### Ví dụ:

```python
# Input: {"John": {"Tuổi": 30, "Phòng ban": "IT", "Lương": 1500}, "Alice": {"Tuổi": 28, "Phòng ban": "HR", "Lương": 1300}}
# Output:
# Thêm hoặc cập nhật thông tin nhân viên: {"John": {"Tuổi": 30, "Phòng ban": "IT", "Lương": 1500}, "Alice": {"Tuổi": 28, "Phòng ban": "HR", "Lương": 1400}}
# Nhân viên có mức lương cao nhất: John - 1500
# Nhân viên có mức lương thấp nhất: Alice - 1400
# Tổng lương của công ty: 2900
```

---

### Bài tập 6: Phân tích dữ liệu tiêu dùng của khách hàng

#### Yêu cầu:

1. Nhập vào một danh sách các giao dịch của khách hàng, mỗi giao dịch bao gồm tên khách hàng, số lượng hàng hóa và giá trị giao dịch.
2. Viết chức năng để tính tổng số tiền mà mỗi khách hàng đã chi tiêu.
3. Viết chức năng để tìm và in ra khách hàng chi tiêu nhiều nhất.
4. Viết chức năng để tìm tất cả các khách hàng có tổng chi tiêu trên mức trung bình.

#### Ví dụ:

```python
# Input: [("John", 2, 100), ("Alice", 3, 150), ("John", 1, 50), ("Bob", 5, 200)]
# Output:
# Tổng chi tiêu của mỗi khách hàng: {"John": 250, "Alice": 150, "Bob": 200}
# Khách hàng chi tiêu nhiều nhất: John
# Khách hàng có chi tiêu trên mức trung bình: {"John": 250, "Bob": 200}
```

---

### Bài tập 7: Quản lý và phân tích đơn hàng

#### Yêu cầu:

1. Nhập vào danh sách các đơn hàng, mỗi đơn hàng bao gồm mã đơn hàng, tên khách hàng, sản phẩm, số lượng và giá.
2. Viết chức năng để tính tổng doanh thu từ tất cả các đơn hàng.
3. Viết chức năng để tìm đơn hàng có giá trị cao nhất.
4. Viết chức năng để sắp xếp và in ra danh sách đơn hàng theo giá trị từ cao đến thấp.

#### Ví dụ:

```python
# Input: [{"mã": "A1", "khách hàng": "John", "sản phẩm": "Laptop", "số lượng": 1, "giá": 1000}, {"mã": "A2", "khách hàng": "Alice", "sản phẩm": "Phone", "số lượng": 2, "giá": 600}]
# Output:
# Tổng doanh thu: 2200
# Đơn hàng có giá trị cao nhất: A1 - 1000
# Danh sách đơn hàng sắp xếp: [{"mã": "A1", "khách hàng": "John", "sản phẩm": "Laptop", "số lượng": 1, "giá": 1000}, {"mã": "A2", "khách hàng": "Alice", "sản phẩm": "Phone", "số lượng": 2, "giá": 600}]
```

---

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

### Bài tập 9: Quản lý hệ thống đặt vé xem phim

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

### Bài tập 10: Quản lý đơn đặt hàng của khách hàng

#### Yêu cầu:

1. Tạo một danh sách chứa các đơn đặt hàng, mỗi đơn đặt hàng bao gồm tên khách hàng, sản phẩm, số lượng, và giá.
2. Viết chức năng để tính tổng số tiền mà mỗi khách hàng phải trả.
3. Viết chức năng để tìm và in ra khách hàng có tổng số tiền phải trả cao nhất.
4. Viết chức năng để tìm tất cả các khách hàng có tổng số tiền phải trả trên mức trung bình.

#### Ví dụ:

```python
# Input: [("John", "Laptop", 1, 1000), ("Alice", "Phone", 2, 600), ("Bob", "Tablet", 1, 300)]
# Output:
# Tổng số tiền của mỗi khách hàng: {"John": 1000, "Alice": 1200, "Bob": 300}
# Khách hàng có tổng số tiền cao nhất: Alice
# Khách hàng có tổng số tiền trên mức trung bình: {"Alice": 1200}
```

---

### Bài tập 11: Phân tích và xử lý dữ liệu bán hàng

#### Yêu cầu:

1. Nhập vào danh sách các giao dịch bán hàng, mỗi giao dịch bao gồm mã sản phẩm, số lượng bán, và giá bán.
2. Viết chức năng để tính tổng doanh thu từ tất cả các giao dịch.
3. Viết chức năng để tìm và in ra sản phẩm bán chạy nhất (sản phẩm có số lượng bán nhiều nhất).
4. Viết chức năng để sắp xếp và in ra danh sách sản phẩm theo tổng doanh thu từ cao đến thấp.

#### Ví dụ:

```python
# Input: [("SP01", 10, 100), ("SP02", 5, 200), ("SP01", 2, 100)]
# Output:
# Tổng doanh thu: 2400
# Sản phẩm bán chạy nhất: SP01
# Danh sách sản phẩm theo doanh thu: [("SP01", 1200), ("SP02", 1000)]
```

---

### Bài tập 12: Quản lý dữ liệu học sinh

#### Yêu cầu:

1. Nhập vào danh sách các học sinh, mỗi học sinh bao gồm tên, lớp, và điểm số của từng môn học.
2. Viết chức năng để tính điểm trung bình của mỗi học sinh.
3. Viết chức năng để xếp hạng các học sinh dựa trên điểm trung bình từ cao đến thấp.
4. Viết chức năng để tìm và in ra học sinh có điểm trung bình cao nhất và thấp nhất trong mỗi lớp.

#### Ví dụ:

```python
# Input: [{"tên": "John", "lớp": "10A", "Toán": 85, "Lý": 78, "Hóa": 92}, {"tên": "Alice", "lớp": "10A", "Toán": 88, "Lý": 95, "Hóa": 80}]
# Output:
# Điểm trung bình của mỗi học sinh: {"John": 85.0, "Alice": 87.67}
# Xếp hạng học sinh: [{"tên": "Alice", "điểm trung bình": 87.67}, {"tên": "John", "điểm trung bình": 85.0}]
# Học sinh có điểm trung bình cao nhất lớp 10A: Alice
# Học sinh có điểm trung bình thấp nhất lớp 10A: John
```

---

### Bài tập 13: Quản lý ngân sách chi tiêu cá nhân

#### Yêu cầu:

1. Tạo một từ điển để lưu trữ các hạng mục chi tiêu hàng tháng và số tiền đã chi tiêu cho mỗi hạng mục.
2. Viết chức năng để thêm hoặc cập nhật chi tiêu cho một hạng mục.
3. Viết chức năng để tính tổng số tiền đã chi tiêu trong tháng.
4. Viết chức năng để tìm và in ra hạng mục chi tiêu nhiều nhất và ít nhất.

#### Ví dụ:

```python
# Input: {"Ăn uống": 300, "Giải trí": 150, "Mua sắm": 200}
# Output:
# Cập nhật chi tiêu: {"Ăn uống": 300, "Giải trí": 150, "Mua sắm": 250}
# Tổng chi tiêu trong tháng: 700
# Hạng mục chi tiêu nhiều nhất: Ăn uống
# Hạng mục chi tiêu ít nhất: Giải trí
```

---

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

### Bài tập 15: Phân tích dữ liệu điểm thi đại học

#### Yêu cầu:

1. Nhập vào danh sách các thí sinh, mỗi thí sinh bao gồm tên, điểm của các môn thi.
2. Viết chức năng để tính điểm trung bình của mỗi thí sinh.
3. Viết chức năng để xếp hạng các thí sinh dựa trên điểm trung bình từ cao đến thấp.
4. Viết chức năng để tìm và in ra danh sách các thí sinh đủ điều kiện đỗ đại học (điểm trung bình >= 5.0).

#### Ví dụ:

```python
# Input: [{"tên": "John", "Toán": 7.0, "Lý": 8.0, "Hóa": 6.5}, {"tên": "Alice", "Toán": 4.5, "Lý": 5.5, "Hóa": 4.0}]
# Output:
# Điểm trung bình của mỗi thí sinh: {"John": 7.17, "Alice": 4.67}
# Xếp hạng thí sinh: [{"tên": "John", "điểm trung bình": 7.17}, {"tên": "Alice", "điểm trung bình": 4.67}]
# Thí sinh đủ điều kiện đỗ đại học: ["John"]
```

---

### Bài tập 16: Phân tích và xử lý dữ liệu bán lẻ

#### Yêu cầu:

1. Nhập vào danh sách các giao dịch bán lẻ, mỗi giao dịch bao gồm mã sản phẩm, số lượng bán và giá bán.
2. Viết chức năng để tính tổng doanh thu từ tất cả các giao dịch.
3. Viết chức năng để tìm sản phẩm có doanh thu cao nhất.
4. Viết chức năng để tạo và in ra báo cáo doanh thu chi tiết cho từng sản phẩm.

#### Ví dụ:

```python
# Input: [("SP01", 10, 100), ("SP02", 5, 200), ("SP01", 2, 100)]
# Output:
# Tổng doanh thu: 2400
# Sản phẩm có doanh thu cao nhất: SP01
# Báo cáo doanh thu: {"SP01": {"số lượng": 12, "doanh thu": 1200}, {"SP02": {"số lượng": 5, "doanh thu": 1000}}
```

---

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

### Bài tập 19: Phân tích kết quả học tập của sinh viên

#### Yêu cầu:

1. Tạo một từ điển lưu trữ kết quả học tập của sinh viên, mỗi sinh viên bao gồm các môn học và điểm số tương ứng.
2. Viết chức năng để tính điểm trung bình của mỗi sinh viên.
3. Viết chức năng để tìm và in ra sinh viên có điểm trung bình cao nhất và thấp nhất.
4. Viết chức năng để xác định và in ra những sinh viên có điểm trung bình dưới 5 (yếu).

#### Ví dụ:

```python
# Input: {"John": {"Toán": 4, "Lý": 6, "Hóa": 5}, "Alice": {"Toán": 8, "Lý": 7, "Hóa": 9}}
# Output:
# Điểm trung bình của mỗi sinh viên: {"John": 5.0, "Alice": 8.0}
# Sinh viên có điểm trung bình cao nhất: Alice
# Sinh viên có điểm trung bình thấp nhất: John
# Sinh viên có điểm trung bình dưới 5: ["John"]
```

---

### Bài tập 20: Quản lý và phân tích danh sách đơn hàng

#### Yêu cầu:

1. Nhập vào danh sách các đơn hàng, mỗi đơn hàng bao gồm mã đơn hàng, tên sản phẩm, số lượng, giá tiền, và trạng thái đơn hàng (đã giao hoặc chưa giao).
2. Viết chức năng để tính tổng số lượng đơn hàng đã giao và chưa giao.
3. Viết chức năng để tính tổng doanh thu từ các đơn hàng đã giao.
4. Viết chức năng để tìm và in ra danh sách các đơn hàng chưa giao.

#### Ví dụ:

```python
# Input: [{"mã": "DH01", "sản phẩm": "Laptop", "số lượng": 1, "giá": 1000, "trạng thái": "Đã giao"}, {"mã": "DH02", "sản phẩm": "Phone", "số lượng": 2, "giá": 600, "trạng thái": "Chưa giao"}]
# Output:
# Tổng số đơn hàng đã giao: 1
# Tổng số đơn hàng chưa giao: 1
# Tổng doanh thu từ các đơn hàng đã giao: 1000
# Danh sách đơn hàng chưa giao: [{"mã": "DH02", "sản phẩm": "Phone", "số lượng": 2, "giá": 600, "trạng thái": "Chưa giao"}]
```
