# Viết chương trình Python tìm vị trí bắt đầu đoạn con dương liên tiếp có nhiều phần tử nhất
print("*"*35)
lst = [-10, -5, 1, 2, 4, 10, 15, 28, 30, 51, 32, 32, 32, 22, 7, -3, -11, 9, 22, 1000, 88]

VT_max_start = -1 # VT bắt đầu đoạn con dương liên tiếp có nhiều phần tử nhất
max_length = 0 # Độ dài đoạn con dương liên tiếp dài nhất
current_VT_start = -1 # Vị trí bắt đầu của đoạn con dương liên tiếp HT
current_length = 0 # Độ dài đoạn con dương liên tiếp Hiên tại

# Danh sách lúc đầu
print("Danh sách lúc đầu là:", lst)

for i, num in enumerate(lst):
    if num > 0:
        if  current_VT_start == -1: # Nếu chưa có đoạn con nào
            current_VT_start = i
            current_length = 1
        else:
            current_length += 1
    else:
        if current_length > max_length:
            max_length = current_length
            VT_max_start = current_VT_start
        # Reset
        current_VT_start = -1
        current_length = 0
# Xủ lý
if current_length > max_length:
    max_length = current_length
    VT_max_start = current_VT_start
    
print("Vị trí bắt đầu của đoạn con dương liên tiếp có nhiều phần tử nhất là:", VT_max_start)
print("*"*35)