# Viết chương trình Python tìm đoạn con có các số hạng dương liên tiếp có tổng lớn nhất. 
# (Nếu có nhiều đoạn con thoả mãn thì đưa ra màn hình: Số đoạn con thoả mãn và các đoạn con đó).
print("*"*35)
lst = [-10, -5, 1, 2, 4, 10, 15, 28, 30, 51, 32, 32, 32, 22, 7, -3, -11, 9, 22, 1000, 88]

max_sum = 0 # Tổng max
max_ds_con = [] # ds lưu đoạn con có sum max
current_sum = 0 # Lưu tổng đoạn con dương hiện tại
current_ds_con = [] # ds lưu đoạn con dương hiện tại

for i in lst:
    if i > 0:
        current_sum += i
        current_ds_con.append(i) # Thêm số hiện tại vào đoạn con dương hiện tại
    else:
        if current_sum > max_sum:
            max_sum = current_sum # Cập nhật tổng lớn
            max_ds_con = [current_ds_con] # Cập nhật ds đoạn con
        elif current_sum == max_sum:
            max_ds_con.append(current_ds_con) # Thêm đoạn con dương hiện tại vào ds
        current_sum = 0 # Reset tổng đoạn con dương HT
        current_ds_con = [] # Reset đoạn con dương HT
        
# Xử lý TH khi đoạn con dương kết thúc ở cuối ds
if current_sum > max_sum:
    max_sum = current_sum
    max_ds_con = [current_ds_con]
elif current_sum == max_sum:
    max_ds_con.append(current_ds_con)

# In kết quả
print("Tổng lớn nhất của các số hạng dương liên tiếp là:", max_sum)
print("Số lượng đoạn con thoả mãn:", len(max_ds_con))
print("Các đoạn con có tổng bằng", max_sum, "là:")

for ds_con in max_ds_con:
    print(ds_con)
print("*"*35)