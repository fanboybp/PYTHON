# Viết chương trình Python để tìm số lớn nhất trong ba số.
print('------------------------')
print('Writen by Nguyễn Văn Luân')
print('------------------------')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
max = a
if b > max:
    max = b
if c > max:
    max = c
print("Số lớn nhất trong 3 số là: ", max)