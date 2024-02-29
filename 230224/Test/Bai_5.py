# Viết chương trình Python tìm vị trí của phần tử dương cuối cùng trong danh sách.
print("*"*35)
lst = [-10, -5, 1, 2, 4, 10, 15, 28, 30, 51, 61, 3, 11]
max1 = max(lst)
for i in range(len(lst) -1, -1, -1):
   if lst[i] > 0:
       max2 = i
       break
print("Vị trí của phần tử dương cuối cùng là:", max2)
print("*"*35)