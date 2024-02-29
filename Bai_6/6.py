# Viết chương trình Python để tìm giai thừa của một số nguyên dương.
print('------------------------')
print('Writen by Nguyễn Văn Luân')
print('------------------------')

def GT(a):
    if a == 0:
        return 1
    if a < 0:
        print("Hãy kiểm tra lại a!")
    else:
        return a * GT(a - 1)
# Nhập một số a
a = int(input('a = '))
# Tính giai thừa
result = GT(a)
# In kết quả
print('------------------------')
print(f"Giai thừa của {a} là: {result}")