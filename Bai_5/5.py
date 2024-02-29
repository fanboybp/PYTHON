# Viết chương trình Python để đổi chỗ giá trị của hai biến
print('------------------------')
print('Writen by Nguyễn Văn Luân')
print('------------------------')
# Nhập 2 biến a và b
a = float(input('a = '))
b = float(input('b = '))
# Đổi chỗ giá trị của 2 biến
a, b = b, a
# Hiển thị kết quả
print('------------------------')
print("Giá trị mới của a là:", a, "\nGiá trị mới của b là:", b)