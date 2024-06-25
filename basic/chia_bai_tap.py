import random

def chia_bai_tap(so_bai_tap, hoc_sinh):
    # Tạo danh sách các bài tập từ 1 đến so_bai_tap
    bai_tap = list(range(1, so_bai_tap + 1))
    
    # Xáo trộn danh sách bài tập
    random.shuffle(bai_tap)
    
    # Tính số bài tập mỗi học sinh sẽ nhận
    so_hoc_sinh = len(hoc_sinh)
    so_bai_tap_moi_hoc_sinh = so_bai_tap // so_hoc_sinh
    so_du_bai_tap = so_bai_tap % so_hoc_sinh
    
    # Chia bài tập cho từng học sinh
    phan_bo_bai_tap = {}
    start = 0
    for i in range(so_hoc_sinh):
        end = start + so_bai_tap_moi_hoc_sinh + (1 if i < so_du_bai_tap else 0)
        phan_bo_bai_tap[hoc_sinh[i]] = bai_tap[start:end]
        start = end
    
    return phan_bo_bai_tap

def main():
    # Nhập thông tin
    so_bai_tap = int(input("Nhập vào số lượng bài tập: "))
    so_hoc_sinh = int(input("Nhập vào số lượng học sinh: "))

    hoc_sinh = []
    for i in range(so_hoc_sinh):
        ten_hoc_sinh = input(f"Nhập vào tên học sinh thứ {i + 1}: ")
        hoc_sinh.append(ten_hoc_sinh)

    # Chia bài tập
    ket_qua_chia = chia_bai_tap(so_bai_tap, hoc_sinh)

    # In kết quả
    for hs, bt in ket_qua_chia.items():
        print(f"Bài tập của {hs} là {len(bt)} bài gồm có: {bt}")

if __name__ == "__main__":
    main()