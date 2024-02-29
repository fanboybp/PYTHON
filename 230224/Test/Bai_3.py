# Viết chương trình Python tính trung bình cộng của cả danh sách, trung bình cộng các phần tử dương trong danh sách.

print("*"*35)
lst = [-10, -5, 1, 2, 4, 10, 15, 28, 30, 51]
S = 0
for x in lst:
    S += x
long = len(lst)
tbc = S / long
print("Trung bình cộng của phần tử là:", tbc)

tong_so_duong = 0
so_duong = 0
for x in lst:
    if x > 0:
        so_duong += 1
        tong_so_duong += x
tbcd = tong_so_duong / so_duong
print("*"*35)
print("Trung bình cộng của số dương là:", tbcd)
print("*"*35)