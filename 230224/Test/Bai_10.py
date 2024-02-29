# Viết chương trình Python tính số lượng các phần tử liên tiếp đan dấu nhiều nhất 
# (dãy phần tử liên tiếp được gọi là đan dấu nếu tích hai phần tử liên tiếp âm).

print("*"*35)
lst = [1, -10, 5, -9, 8, -22, 10, -2, 99, 88, 77, 6, 9]

Dem_max = 0
Dem_HT = 0

for i in range(len(lst) - 1):
    if lst[i] * lst[i + 1] < 0:
        Dem_HT += 1
        Dem_max = max(Dem_max, Dem_HT)
    else:
        Dem_HT = 0
print("Số lượng các phần tử liên tiếp đan dấu nhiều nhất là:", Dem_max)
print("*"*35)