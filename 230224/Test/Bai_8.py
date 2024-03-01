# Viết chương trình Python tính số lượng các số dương liên tiếp nhiều nhất.

print("*"*35)
lst = [-10, -5, 1, 2, 4, 10, 15, 28, 30, 51, 32, 32, 32, 22, 7, -3, -11, 9, 22, 100, 88]

So_duong_Max = 0
Dem = 0

# Danh sách lúc đầu
print("Danh sách lúc đầu là:", lst)

for i in lst:
    if i > 0:
        Dem += 1
        So_duong_Max = max(So_duong_Max, Dem)
    else:
        Dem = 0
        
print("Số lượng các số dương liên tiếp nhiều nhất là:", So_duong_Max)
print("*"*35)