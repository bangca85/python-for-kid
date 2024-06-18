import random


def menu_chinh():
    print("Chào mừng bạn đến với chương trình!")
    print("Vui lòng chọn số bài tập bạn muốn chạy thử( thí dụ nhập 1 hoặc 10):")
    print("1 --> Bài 1. Viết chương trình yêu cầu người dùng nhập tên của họ và in ra câu chào hỏi kèm theo tên đó.")
    print("2 --> Bài 2.Viết chương trình yêu cầu người dùng nhập vào hai số  và in ra tổng của chúng.")
    print("..........")
    print("23 --> Bài 23. Viết chương trình Tính tổng các số lẻ từ 1 đến N, với N do người dùng nhập vào.")
    print("24 --> Bài 24 Viết chương trình Yêu cầu người dùng nhập một số và kiểm tra xem số đó có phải là số nguyên tố hay không.")
    print("0 --> Thoát")

#Bài 1. Viết chương trình yêu cầu người dùng nhập tên của họ và in ra câu chào hỏi kèm theo tên đó.
def xin_chao():
    print("========================================")
    print("Bài 1. Viết chương trình yêu cầu người dùng nhập tên của họ và in ra câu chào hỏi kèm theo tên đó.")
    print("========================================")
    ten = input("Nhập tên của bạn: ")
    print("Chào " + ten + "!")

#Bài 2.Viết chương trình yêu cầu người dùng nhập vào hai số  và in ra tổng của chúng.
def tinh_tong():
    print("========================================")
    print("Bài 2.Viết chương trình yêu cầu người dùng nhập vào hai số  và in ra tổng của chúng.")
    print("========================================")
    so1 = float(input("Nhập số thứ nhất: "))
    so2 = float(input("Nhập số thứ hai: "))
    tong = so1 + so2
    print(f"Tổng của hai số là: {tong}")

# Bài 3: Viết chương trình tính diện tích và chu vi của hình chữ nhật với chiều dài và chiều rộng do người dùng nhập vào. 
def hinh_chu_nhat():
    print("========================================")
    print("Bài 3: Viết chương trình tính diện tích và chu vi của hình chữ nhật với chiều dài và chiều rộng do người dùng nhập vào. ")
    print("========================================")
    chieu_dai = float(input("Nhập chiều dài: "))
    chieu_rong = float(input("Nhập chiều rộng: "))
    dien_tich = chieu_dai * chieu_rong
    chu_vi = 2 * (chieu_dai + chieu_rong)
    print(f"Diện tích: {dien_tich}")
    print(f"Chu vi: {chu_vi}")

# Bài 4: Viết chương trình chuyển đổi độ C sang độ F
def doi_do_c_sang_f():
    print("========================================")
    print("Bài 4: Viết chương trình chuyển đổi độ C sang độ F")
    print("========================================")
    do_c = float(input("Nhập nhiệt độ (°C): "))
    do_f = (do_c * 9/5) + 32
    print(f"Nhiệt độ (°F): {do_f}")

# Bài 5: Viết chương trình Yêu cầu người dùng nhập chiều cao và cân nặng, sau đó tính chỉ số BMI và cho biết người đó thuộc loại hình thể nào.
def tinh_bmi():
    print("========================================")
    print("Bài 5: Viết chương trình Yêu cầu người dùng nhập chiều cao và cân nặng, sau đó tính chỉ số BMI và cho biết người đó thuộc loại hình thể nào.")
    print("========================================")
    can_nang = float(input("Nhập cân nặng (kg): "))
    chieu_cao = float(input("Nhập chiều cao (m): "))
    bmi = can_nang / (chieu_cao ** 2)
    print(f"BMI: {bmi}")
    if bmi < 18.5:
        print("Thiếu cân")
    elif 18.5 <= bmi < 24.9:
        print("Bình thường")
    elif 25 <= bmi < 29.9:
        print("Thừa cân")
    else:
        print("Béo phì")

#Bài 6:Viết chương trình Yêu cầu người dùng nhập một số và kiểm tra xem số đó là số chẵn hay số lẻ.
def kiem_tra_so_chan():
    print("========================================")
    print("Bài 6:Viết chương trình Yêu cầu người dùng nhập một số và kiểm tra xem số đó là số chẵn hay số lẻ.")
    print("========================================")
    so = int(input("Nhập một số: "))
    if so % 2 == 0:
        print(f"{so} là số chẵn")
    else:
        print(f"{so} là số lẻ")

#Bài 7: Viết chương trình Yêu cầu người dùng nhập một chuỗi và in ra chuỗi đó theo thứ tự ngược lại. 
def dao_chuoi():
    print("========================================")
    print("Bài 7: Viết chương trình Yêu cầu người dùng nhập một chuỗi và in ra chuỗi đó theo thứ tự ngược lại. ")
    print("========================================")
    chuoi = input("Nhập chuỗi: ")
    chuoi_dao_nguoc = chuoi[::-1]
    print("Chuỗi đảo ngược là:", chuoi_dao_nguoc)

#Bài 8: Viết chương trình Yêu cầu người dùng nhap một năm, sau đó kiểm tra xem năm đó phải là năm nhuận hay không.
def kiem_tra_nam_nhuan():
    print("========================================")
    print("Bài 8: Viết chương trình Yêu cầu người dùng nhap một năm, sau đó kiểm tra xem năm đó phải là năm nhuận hay không.")
    print("========================================")
    nam = int(input("Nhập một năm: "))
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        print(f"{nam} là năm nhuận")
    else:
        print(f"{nam} không phải là năm nhuận")

#Bài 9: Viết chương trình Yêu cầu người dùng nhập một số tiền bằng VND và chuyển đổi sang USD theo tỷ giá hối đoái hiện tại.
def doi_tien_vnd_usd():
    print("========================================")
    print("Bài 9: Viết chương trình Yêu cầu người dùng nhập một số tiền bằng VND và chuyển đổi sang USD theo tỷ giá hối đoái hiện tại.")
    print("========================================")
    tien_vnd = int(input("Nhập một tiền VND: "))
    tien_usd = tien_vnd / 23000
    print(f"Số tiền (USD): {tien_usd}")


#Bài 10: Viết chương trình Yêu cầu người dùng nhập một ký tự và kiểm tra xem đó có phải là nguyên âm hay không.
def kiem_tra_nguyen_am():
    print("========================================")
    print("Bài 10: Viết chương trình Yêu cầu người dùng nhập một ký tự và kiểm tra xem đó có phải là nguyên âm hay không.")
    print("========================================")
    ky_tu = input("Nhập một ký tự: ")
    nguyen_am = 'aeiouAEIOU'
    if ky_tu in nguyen_am:
        print(ky_tu, "là nguyên âm")
    else:
        print(ky_tu, "không phải là nguyên âm")

#Bài 11: Viết chương trình Yêu cầu người dùng nhập bán kính và tính chu vi, diện tích của hình tròn
def tinh_dien_tich_chu_vi_hinh_tron():
    print("========================================")
    print("Bài 11: Viết chương trình Yêu cầu người dùng nhập bán kính và tính chu vi, diện tích của hình tròn")
    print("========================================")
    ban_kinh = float(input("Nhập bán kính: "))
    dien_tich = ban_kinh * ban_kinh * 3.14
    chu_vi = 2 * ban_kinh * 3.14
    print(f"Diện tích: {dien_tich}")
    print(f"Chu vi: {chu_vi}")

#Bài 12: Viết chươn trình Yêu cầu người dùng nhập vào số giây và chuyển đổi thành giờ, phút, giây.
def doi_giay_phut_giay():
    print("========================================")
    print("Bài 12: Viết chươn trình Yêu cầu người dùng nhập vào số giây và chuyển đổi thành giờ, phút, giây.")
    print("========================================")
    so_giay = int(input("Nhập số giây: "))
    gio = so_giay // 3600
    phut = (so_giay % 3600) // 60
    giay = so_giay % 60
    print(f"Từ {so_giay} đổi thành: {gio} giờ {phut} phút {giay} giây")

#Bài 13:  Viết chương trình Tính tổng các số chẵn từ 1 đến N, với N do người dùng nhập vào.
def tinh_tong_so_chan():
    print("========================================")
    print("Bài 13:  Viết chương trình Tính tổng các số chẵn từ 1 đến N, với N do người dùng nhập vào.")
    print("========================================")
    n = int(input("Nhập số n: "))
    tong = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            tong += i
    print(f"Tong cac so chan tu 1 den {n} = {tong}")

#Bài 14: Viết chương trình Tạo một danh sách gồm 10 số nguyên ngẫu nhiên và in ra danh sách đó.
def tao_danh_sach_so_nguyen():
    print("========================================")
    print("Bài 14: Viết chương trình Tạo một danh sách gồm 10 số nguyên ngẫu nhiên và in ra danh sách đó.")
    print("========================================")
    danh_sach = []
    for i in range(10):
        so_nguyen = random.randint(1, 100)
        danh_sach.append(so_nguyen)
    print(f"Danh sách số nguyên ngẫu nhiên: {danh_sach}") 

#Bài 15: Viết chương trình Yêu cầu người dùng nhập vào một danh sách các số và tìm số lớn nhất, nhỏ nhất trong danh sách đó.
def tim_so_lon_nhat_trong_danh_sach():
    print("========================================")
    print("Bài 15: Viết chương trình Yêu cầu người dùng nhập vào một danh sách các số và tìm số lớn nhất, nhỏ nhất trong danh sách đó.")
    print("========================================")
    danh_sach = []
    for i in range(10):
        so_nguyen = int(input(f"Nhập số nguyên thu {i+1}: "))
        danh_sach.append(so_nguyen)
    so_lon_nhat = max(danh_sach)
    so_nho_nhat = min(danh_sach)
    print(f"Số lớn nhất trong danh sách: {so_lon_nhat}")
    print(f"Số nhỏ nhất trong danh sách: {so_nho_nhat}")

def tim_so_nho_nhat_trong_danh_sach2():
    print("========================================")
    print("Bài 15: Viết chương trình Yêu cầu người dùng nhập vào một danh sách các số và tìm số lớn nhất, nhỏ nhất trong danh sách đó.")
    print("========================================")
    danh_sach = list(map(int, input("Nhập các số, cách nhau bởi dấu cách: ").split()))
    lon_nhat = max(danh_sach)
    nho_nhat = min(danh_sach)
    print("Số lớn nhất trong danh sách:", lon_nhat)
    print("Số nhỏ nhất trong danh sách:", nho_nhat)

#Bài 16: Viết chương trình Yêu cầu người dùng nhập vào một chuỗi và một ký tự, đếm số lần xuất hiện của ký tự đó trong chuỗi.
def dem_so_lan_xuat_hien_ky_tu():
    print("========================================")
    print("Bài 16: Viết chương trình Yêu cầu người dùng nhập vào một chuỗi và một ký tự, đếm số lần xuất hiện của ký tự đó trong chuỗi.")
    print("========================================")
    chuoi = input("Nhập chuỗi: ")
    ky_tu = input("Nhập ký tự: ")
    dem = 0
    for i in range(len(chuoi)):
        if chuoi[i] == ky_tu:
            dem += 1
    print(f"Số lần xuất hiện {ky_tu} trong chuỗi: {dem}")

def dem_so_lan_xuat_hien_ky_tu2():
    print("========================================")
    print("Bài 16: Viết chương trình Yêu cầu người dùng nhập vào một chuỗi và một ký tự, đếm số lần xuất hiện của ký tự đó trong chuỗi.")
    print("========================================")
    chuoi = input("Nhập chuỗi: ")
    ky_tu = input("Nhập ký tự: ")
    dem = chuoi.count(ky_tu)
    print(f"Số lần xuất hiện {ky_tu} trong chuỗi: {dem}")

#Bài 17: Yêu cầu người dùng nhập một chuỗi và kiểm tra xem chuỗi đó có phải là palindrome (chuỗi đối xứng) hay không? 
def kiem_tra_chuoi_palindrome():
    print("========================================")
    print("Bài 17: Yêu cầu người dùng nhập một chuỗi và kiểm tra xem chuỗi đó có phải là palindrome (chuỗi đối xứng) hay không? ")
    print("========================================")
    chuoi = input("Nhập chuỗi: ")
    if chuoi == chuoi[::-1]:
        print(chuoi, "là chuỗi palindrome")
    else:
        print(chuoi, "không phải là chuỗi palindrome")

#Bài 18:  Viết chương trình in bảng cửu chương từ 1 đến 10.
def bang_cuu_chuong():
    print("========================================")
    print("Bài 18:  Viết chương trình in bảng cửu chương từ 1 đến 10.")
    print("========================================")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")
        print("-" * 20)

#Bài 19: Viết chương trình tính tổng các số nguyên từ 1 đến N, với N do người dùng nhập vào.
def tinh_tong_so_nguyen():
    print("========================================")
    print("Bài 19: Viết chương trình tính tổng các số nguyên từ 1 đến N, với N do người dùng nhập vào.")
    print("========================================")
    n = int(input("Nhập số nguyên n: "))
    tong = 0
    for i in range(1, n+1):
        tong += i
    print(f"Tổng các số nguyên từ 1 đến {n} là: {tong}")

def tinh_tong_so_nguyen2():
    print("========================================")
    print("Bài 19: Viết chương trình tính tổng các số nguyên từ 1 đến N, với N do người dùng nhập vào.")
    print("========================================")
    n = int(input("Nhập số nguyên n: "))
    tong = sum(range(1, n+1))
    print(f"Tổng các số nguyên từ 1 đến {n} là: {tong}")

#Bài 20. Viết chương trình Yêu cầu người dùng nhập N và in các số nguyên từ 1 đến N.
def in_so_nguyen():
    print("========================================")
    print("Bài 20. Viết chương trình Yêu cầu người dùng nhập N và in các số nguyên từ 1 đến N.")
    print("========================================")
    n = int(input("Nhập số nguyên n: "))
    for i in range(1, n+1):
        print(i)

#Bài 21. Viết chương trình Yêu cầu người dùng nhập N và in các số chẵn từ 1 đến N.
def in_so_chan():
    print("========================================")
    print("Bài 21. Viết chương trình Yêu cầu người dùng nhập N và in các số chẵn từ 1 đến N.")
    print("========================================")
    n = int(input("Nhập số nguyên n: "))
    for i in range(2, n+1, 2):
        print(i)

#Bài 22. Viết chương trình Yêu cầu người dùng nhập N và in các số lẻ từ 1 đến N.
def in_so_le():
    print("========================================")
    print("Bài 22. Viết chương trình Yêu cầu người dùng nhập N và in các số lẻ từ 1 đến N.")
    print("========================================")
    n = int(input("Nhập số nguyên n: "))
    for i in range(1, n+1, 2):
        print(i)

#Bài 23. Viết chương trình Tính tổng các số lẻ từ 1 đến N, với N do người dùng nhập vào.
def tinh_tong_so_le():
    print("========================================")
    print("Bài 23. Viết chương trình Tính tổng các số lẻ từ 1 đến N, với N do người dùng nhập vào.")
    print("========================================")
    n = int(input("Nhập số nguyên n: "))
    tong = 0
    for i in range(1, n+1, 2):
        tong += i
    print(f"Tổng các số lẻ từ 1 đến {n} là: {tong}")
def tinh_tong_so_le2():
    print("========================================")
    print("Bài 23. Viết chương trình Tính tổng các số lẻ từ 1 đến N, với N do người dùng nhập vào.")
    print("========================================")
    n = int(input("Nhập số nguyên n: "))
    tong = sum(range(1, n+1, 2))
    print(f"Tổng các số lẻ từ 1 đến {n} là: {tong}")

#Bài 24 Viết chương trình Yêu cầu người dùng nhập một số và kiểm tra xem số đó có phải là số nguyên tố hay không.
def kiem_tra_so_nguyen_to():
    print("========================================")
    print("Bài 24 Viết chương trình Yêu cầu người dùng nhập một số và kiểm tra xem số đó có phải là số nguyên tố hay không.")
    print("========================================")
    n = int(input("Nhập số nguyên n: "))
    if n > 1:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                print(n, "không phải là số nguyên tố")
                break
        else:
            print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")

def kiem_tra_so_nguyen_to2():
    n = int(input("Nhập số nguyên n: "))
    if n > 1 and all(n%i!=0 for i in range(2, int(n**0.5)+1)):
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")


def main():
    while True:
        menu_chinh()
        lua_chon = input("Nhập số bài tập bạn muốn chạy thử (1-24): ")

        if lua_chon == '1':
            xin_chao()
        elif lua_chon == '2':
            tinh_tong()
        elif lua_chon == '3':
            hinh_chu_nhat()
        elif lua_chon == '4':
            doi_do_c_sang_f()
        elif lua_chon == '5':
            tinh_bmi()
        elif lua_chon == '6':
            kiem_tra_so_chan()
        elif lua_chon == '7':
            dao_chuoi()
        elif lua_chon == '8':
            kiem_tra_nam_nhuan()
        elif lua_chon == '9':
            doi_tien_vnd_usd()
        elif lua_chon == '10':
            kiem_tra_nguyen_am()
        elif lua_chon == '11':
            tinh_dien_tich_chu_vi_hinh_tron()
        elif lua_chon == '12':
            doi_giay_phut_giay()
        elif lua_chon == '13':
            tinh_tong_so_chan()
        elif lua_chon == '14':
            tao_danh_sach_so_nguyen()
        elif lua_chon == '15':
            tim_so_lon_nhat_trong_danh_sach()
        elif lua_chon == '16':
            dem_so_lan_xuat_hien_ky_tu()
        elif lua_chon == '17':
            kiem_tra_chuoi_palindrome()
        elif lua_chon == '18':
            bang_cuu_chuong()
        elif lua_chon == '19':
            tinh_tong_so_nguyen()
        elif lua_chon == '20':
            in_so_nguyen()
        elif lua_chon == '21':
            in_so_chan()
        elif lua_chon == '22':
            in_so_le()
        elif lua_chon == '23':
            tinh_tong_so_le()
        elif lua_chon == '24':
            kiem_tra_so_nguyen_to()
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

