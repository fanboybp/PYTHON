def luuFile():
    file = open('E:\\Python\\Python\\PYTHON\\Dict\\test1\\csdlsinhvien.txt', 'w', encoding='utf-8')
    file.writelines("sv01: Nguyễn Văn Chúc: 9.5\n")
    file.writelines("sv02: Nguyễn Thị Mừng: 8.5\n")
    file.writelines("sv03: Vũ Thị Năm: 9.0\n")
    file.writelines("sv04: Phan Văn Mới: 7.0")
    file.close()
luuFile()

def docFile():
    file = open('E:\\Python\\Python\\PYTHON\\Dict\\test1\\csdlsinhvien.txt', 'r', encoding='utf-8')
    for line in file:
        print(line.strip())
    file.close()
docFile()