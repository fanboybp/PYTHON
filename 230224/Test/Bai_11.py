# Viết chương trình Python tính số lượng các phần tử không tăng nhiều nhất.

print("*"*35)
lst = [-10, -5, 1, 2, 4, 10, 15, 28, 30, 51, 32, 22, 7, -3, -11, 9, 22, 1000, 88]

Dem = 0
MaxDem = 0

# Danh sách lúc đầu
print("Danh sách lúc đầu là:", lst)

for i in range(1 , len(lst)):
    if lst[i] >= lst[i-1]:
        Dem += 1
    else:
        MaxDem = max(MaxDem, Dem)
        Dem = 0
print("Số lượng các phần tử không tăng nhiều nhất là:", MaxDem)
print("*"*35)