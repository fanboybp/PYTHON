# Viết chương trình Python xóa phần tử thứ k (k nhập từ bàn phím) trong danh sách.

print("*"*35)
lst = [-10, -5, 1, 2, 4, 10, 15, 28, 30, 51, 32, 32, 32, 22, 7, -3, -11, 9, 22, 1000, 88]

print("Danh sách ban đầu:", lst)
k = int(input('k = '))

if k < 1 or k > len(lst):
    print("Vị trí phần tử cần xóa không hợp lệ!")
else:
    del lst[k] # Xóa phần tử thứ k
    print("Danh sách sau khi xóa phần tử thứ", k,"ds_new =", lst)
print("*"*35)