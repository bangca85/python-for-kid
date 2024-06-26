'''
Viết một hàm extract_chars nhận vào một chuỗi và trả về một chuỗi mới bao gồm các ký tự từ vị trí lẻ của chuỗi ban đầu.
- input: PythonProgramming
- output: yhnrgamn
'''
def extract_chars():
    chuoi = input("Nhập chuỗi: ")
    return chuoi[1::2]

'''
Viết một hàm substring nhận vào một chuỗi, vị trí bắt đầu và vị trí kết thúc, trả về chuỗi con từ vị trí bắt đầu đến vị trí kết thúc.
- input: HelloWorld vị trí 2 và 7
- output: lloWo 
'''
def substring():
    chuoi = input("Nhập chuỗi: ")
    start = int(input("Nhập vị trí bắt đầu: "))
    end = int(input("Nhập vị trí kết thúc: "))
    return chuoi[start:end]
'''
 Viết một hàm extract_words nhận vào một chuỗi đại diện cho một câu và trả về một danh sách các từ trong câu, mỗi từ là một phần tử của danh sách.
- input: Python programming is fun
- output: ['Python', 'programming', 'is', 'fun']
'''
def extract_words():
    chuoi = input("Nhập chuỗi: ")
    return chuoi.split()

def main():
    while True:
        lua_chon = input("Nhập số bài tập bạn muốn chạy thử (1-3): ")

        if lua_chon == '1':
            chuoi = extract_chars()
            print(f"Chuỗi ở vị trí lẻ là: {chuoi}")
        elif lua_chon == '2':
            chuoi = substring()
            print(f"Chuỗi sau khi cắt là: {chuoi}")
        elif lua_chon == '3':
            chuoi = extract_words()
            print(f"Danh sách từ là {chuoi}")
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

        tiep_tuc = input("Bạn có muốn quay lại màn hình chính không? (c/k): ")
        if tiep_tuc.lower() != 'c':
            print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break

if __name__ == "__main__":
    main()
