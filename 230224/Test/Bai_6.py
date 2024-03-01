# Viết chương trình Python tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.
print("*"*35)
lst = [-10, -5, 1, 2, 4, 10, 15, 28, 30, 51, 61, 99, 8]
VT = max(lst)
max = 0
# Danh sách lúc đầu
print("Danh sách lúc đầu là:", lst)
for i in range(len(lst) -1, -1, -1):
   if lst[i] == VT:
       VTC = i      
   x = lst[i]
   if max < x:
       max = x
print("Phần tử lớn nhất là :", max)
print("Vị trí của phần tử lớn nhất cuối cùng là:", VTC)
print("*"*35)