# Viết chương trình Python tìm vị trí của phần tử âm đầu tiên trong danh sách.
print("*"*35)
lst = [0, 1, 2, 4, 10, 15, 3, 8, 11, -28, -5, 30, 51]
# Tìm vị trí của phần tử âm đầu tiên
VT_am = 0
for x in range(len(lst)):
    if lst[x] < 0:
        VT_am = x
        break
print("Vị trí âm đầu tiên của danh sách là:", VT_am)
print("*"*35)