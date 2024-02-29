# Viết chương trình Python tính số lượng các số dương liên tiếp có tổng lớn nhất.

print("*"*35)
lst = [-10, -5, 1, 2, 4, 10, 15, 28, 30, 51, 32, 32, 32, 22, 7, -3, -11, 9, 22, 1000, 88]

max_sum = 0
sum_HT = 0
max_dem = 0
Dem_HT = 0

for i in lst:
    if i > 0:
        sum_HT += i
        Dem_HT += 1
        if  max_sum < sum_HT:
            max_sum = sum_HT
            max_dem = Dem_HT
    else:
        sum_HT = 0
        Dem_HT = 0
print("Số lượng các số dương liên tiếp có tổng lớn nhất là:", max_dem)
print("*"*35)