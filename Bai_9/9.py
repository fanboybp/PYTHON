# Viết chương trình Python để tìm số lớn thứ hai trong một danh sách các số nguyên
print('------------------------')
print('Writen by Nguyễn Văn Luân')
print('------------------------')

def max_2(A):
    # Khởi tạo giá trị ban đầu cho max1 và max2 là -∞
    max1 = float('-inf')
    max2 = float('-inf')

    # Duyệt qua từng phần tử trong danh sách A
    for num in A:
        # Nếu phần tử hiện tại là số nguyên và lớn hơn max1
        if isinstance(num, int) and num > max1:
            max1, max2 = num, max1
        # Nếu phần tử hiện tại là số nguyên và lớn hơn max2 và nhỏ hơn max1
        elif isinstance(num, int) and num > max2 and num < max1:
            max2 = num

    # Nếu max2 vẫn là -∞, tức là danh sách chỉ chứa một số duy nhất
    if max2 == float('-inf'):
        return "Không có số lớn thứ hai vì chỉ có một số duy nhất trong danh sách."
    else:
        return max2
# Danh sách các số nguyên
A = [1, 5, 88, 2, 98, 100, 99.6]
# In kết quả
print("Số lớn thứ 2 trong dãy trên là :", max_2(A)) 