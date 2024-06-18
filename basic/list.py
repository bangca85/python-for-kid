# Bài 1: Đếm số phần tử trong danh sách [3, 5, 7, 2, 8, 1]
def dem_so_phan_tu():
    print("========================================")
    print("Bài 1: Đếm số phần tử trong danh sách [3, 5, 7, 2, 8, 1]")
    print("========================================")
    list = [3, 5, 7, 2, 8, 1]
    dem = 0
    for i in list:
        dem += 1
    print(f"Co {dem} phần tử trong danh sách {list}")

# Bài 2: Tính trung bình cộng của danh sách [3, 5, 7, 2, 8, 1]
def tinh_trung_binh_cung():
    print("========================================")
    print("Bài 2: Tính trung bình cộng của danh sách [3, 5, 7, 2, 8, 1]")
    print("========================================")
    list = [3, 5, 7, 2, 8, 1]
    tong = 0
    for i in list:
        tong += i
    print(f"Trung bình cộng của danh sách {list}:", tong / len(list))

#Bài 3: Kiểm tra xem một số có trong danh sách không [3, 5, 7, 2, 8, 1]
def kiem_tra_so_trong_danh_sach():
    print("========================================")
    print("Bài 3: Kiểm tra xem một số có trong danh sách không [3, 5, 7, 2, 8, 1]")
    print("========================================")
    list = [3, 5, 7, 2, 8, 1]
    number = int(input("Nhập số cần kiểm tra: "))
    for i in list:
        if i == number:
            print(f"{number} có trong danh sách")
            break
    else:
        print(f"{number} không có trong danh sách")

#Bài 4:  Đếm số lần xuất hiện của một số trong danh sách [3, 5, 7, 2, 8, 1, 7]
def dem_so_lan_xuat_hien():
    print("========================================")
    print("Bài 4:  Đếm số lần xuất hiện của một số trong danh sách [3, 5, 7, 2, 8, 1, 7]")
    print("========================================")
    list = [3, 5, 7, 2, 8, 1, 7]
    number = int(input("Nhập số cần đếm: "))
    dem = 0
    for i in list:
        if i == number:
            dem += 1
    print(f"Số lần xuất hiện {number} trong danh sách {list}:", dem)

#Bài 5: Tính tổng các số chẵn trong danh sách [3, 5, 7, 2, 8, 1]
def tinh_tong_so_chan():
    print("========================================")
    print("Bài 5: Tính tổng các số chẵn trong danh sách [3, 5, 7, 2, 8, 1]")
    print("========================================")
    list = [3, 5, 7, 2, 8, 1]
    tong = 0
    for i in list:
        if i % 2 == 0:
            tong += i
    print(f"Tổng các số chẵn trong danh sách {list}:", tong)   

#Bài 6:Nhân tất cả các phần tử trong danh sách [3, 5, 7, 2, 8, 1]
def nhan_tat_ca_so_phan_tu():
    print("========================================")
    print("Bài 6:Nhân tất cả các phần tử trong danh sách [3, 5, 7, 2, 8, 1]")
    print("========================================")
    list = [3, 5, 7, 2, 8, 1]
    tich = 1
    for i in list:
        tich *= i
    print(f"Tích cả các phần tử trong danh sách {list}:", tich)

#Bài 7:Đảo ngược danh sách [3, 5, 7, 2, 8, 1]
def dao_nguoc_danh_sach():
    print("========================================")
    print("Bài 7:Đảo ngược danh sách [3, 5, 7, 2, 8, 1]")
    print("========================================")
    list = [3, 5, 7, 2, 8, 1]
    list.reverse()
    print(f"Đảo ngược danh sách là {list}")

#Bài 8: Tìm số lẻ lớn nhất trong danh sách [3, 5, 7, 2, 8, 1]
def tim_so_le(number):
    if number % 2 != 0:
        return True
    return False
def tim_so_lon_nhat_trong_danh_sach():
    print("========================================")
    print("Bài 8: Tìm số lẻ lớn nhất trong danh sách [3, 5, 7, 2, 8, 1]")
    print("========================================")
    list = [3, 5, 7, 2, 8, 1]
    so_le_lon_nhat = None
    for i in list:
        if tim_so_le(i):
            if so_le_lon_nhat is None or i > so_le_lon_nhat:
                so_le_lon_nhat = i
    print(f"Số lớn nhất trong danh sách {list}:", so_le_lon_nhat)

#Bài 9: Tìm số chẵn nhỏ nhất trong danh sách [3, 5, 7, 2, 8, 1]
def tim_so_chan_nho_nhat_trong_danh_sach():
    print("========================================")
    print("Bài 9: Tìm số chẵn nhỏ nhất trong danh sách [3, 5, 7, 2, 8, 1]")
    print("========================================")
    list = [3, 5, 7, 2, 8, 1]
    so_chan_nho_nhat = None
    for i in list:
        if not tim_so_le(i):
            if so_chan_nho_nhat is None or i < so_chan_nho_nhat:
                so_chan_nho_nhat = i
    print(f"Số chẵn nhỏ nhất trong danh sách {list}:", so_chan_nho_nhat)

#Bài 10: Đếm số phần tử chẵn trong danh sách [3, 5, 7, 2, 8, 1]
def dem_so_phan_tu_chan():
    print("========================================")
    print("Bài 10: Đếm số phần tử chẵn trong danh sách [3, 5, 7, 2, 8, 1]")
    print("========================================")
    list = [3, 5, 7, 2, 8, 1]
    dem = 0
    for i in list:
        if not tim_so_le(i):
            dem += 1
    print(f"Co {dem} phần tử chẵn trong danh sách {list}")

#Bài 11: Tìm tổng các số lẻ trong danh sách [3, 5, 7, 2, 8, 1]
def tinh_tong_so_le_trong_danh_sach():
    print("========================================")
    print("Bài 11: Tìm tổng các số lẻ trong danh sách [3, 5, 7, 2, 8, 1]")
    print("========================================")
    list = [3, 5, 7, 2, 8, 1]
    tong = 0
    for i in list:
        if  tim_so_le(i):
            tong =+ i
    print(f"Tổng các số lẻ trong list {list} là:", tong)

#Bài 12: Tìm phần tử lớn thứ hai trong danh sách [3, 5, 7, 2, 8, 1]
def tim_phan_tu_lon_thu_hai_trong_danh_sach():
    print("========================================")
    print("Bài 12: Tìm phần tử lớn thứ hai trong danh sách [3, 5, 7, 2, 8, 1]")
    print("========================================")
    list = [3, 5, 7, 2, 8, 1]
    list.sort()
    print(f"Phần tử lớn thứ hai trong danh sách {list}:", list[-2]) 

def tim_phan_tu_lon_thu_hai_trong_danh_sach2():
    print("========================================")
    print("Bài 12: Tìm phần tử lớn thứ hai trong danh sách [3, 5, 7, 2, 8, 1]")
    print("========================================")
    list = [3, 5, 7, 2, 8, 1]
    lon_nhat = float('-inf')
    lon_thu_hai = float('-inf')
    for so in list: 
        if so > lon_nhat:
            lon_thu_hai = lon_nhat
            lon_nhat = so
        elif so > lon_thu_hai and so != lon_nhat:
            lon_thu_hai = so
    if lon_thu_hai == float('-inf'):
        print("Không tìm thấy phần tử lớn thứ hai trong danh sách")
    else:
        print(f"Phần tử lớn thứ hai trong danh sách {list}:", lon_thu_hai)


def menu_chinh():
    print("Chào mừng bạn đến với chương trình về các bài tập danh sách!")
    print("Vui lòng chọn số bài tập bạn muốn chạy thử( thí dụ nhập 1 hoặc 10):")
    print("1 --> Bài 1: Đếm số phần tử trong danh sách [3, 5, 7, 2, 8, 1]")
    print("2 --> Bài 2: Tính trung bình cộng của danh sách [3, 5, 7, 2, 8, 1]")
    print("..........")
    print("11 --> Bài 11: Tìm tổng các số lẻ trong danh sách [3, 5, 7, 2, 8, 1]")
    print("12 --> Bài 12: Tìm phần tử lớn thứ hai trong danh sách [3, 5, 7, 2, 8, 1]")
    print("0 --> Thoát")

def main():
    while True:
        menu_chinh()
        lua_chon = input("Nhập số bài tập bạn muốn chạy thử (1-12): ")

        if lua_chon == '1':
            dem_so_phan_tu()
        elif lua_chon == '2':
            tinh_trung_binh_cung()
        elif lua_chon == '3':
            kiem_tra_so_trong_danh_sach()
        elif lua_chon == '4':
            dem_so_lan_xuat_hien()
        elif lua_chon == '5':
            tinh_tong_so_chan()
        elif lua_chon == '6':
            nhan_tat_ca_so_phan_tu()
        elif lua_chon == '7':
            dao_nguoc_danh_sach()
        elif lua_chon == '8':
            tim_so_le()
        elif lua_chon == '9':
            tim_so_chan_nho_nhat_trong_danh_sach()
        elif lua_chon == '10':
            dem_so_phan_tu_chan()
        elif lua_chon == '11':
            tinh_tong_so_le_trong_danh_sach()
        elif lua_chon == '12':
            tim_phan_tu_lon_thu_hai_trong_danh_sach2()
        elif lua_chon == '0':
            print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

        tiep_tuc = input("Bạn có muốn quay lại màn hình chính không? (c/k): ")
        if tiep_tuc.lower() != 'c':
            print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break

if __name__ == "__main__":
    main()

