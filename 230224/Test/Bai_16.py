# Viết chương trình Python tìm số phần tử là dương và là số nguyên tố của danh sách và vị trí của nó trong danh sách.

print("*"*35)
lst = [-10, -5, 1, 2, 4, 10, 15, 28, 30, 51, 32, 32, 32, 22, 7, -3, -11, 9, 22, 1000, 88]

# Danh sách để lưu các số nguyên tố
ds_nt = []

# Danh sách để lưu vị trí của các số nguyên tố trong danh sách
ds_VT = []

# Duyệt qua từng phần tử và vị trí của nó trong danh sách
for i, num in enumerate(lst):
    # Kiểm tra xem số có phải là số nguyên tố không
    is_prime = True  # Giả định số là số nguyên tố
    if num > 1:  
        for j in range(2, int(num/2) + 1):  
            if num % j == 0:  
                is_prime = False  
                break  # Dừng kiểm tra
    else:
        is_prime = False  # Số không phải là số nguyên tố nếu nhỏ hơn hoặc bằng 1

    if is_prime:  
        ds_nt.append(num)  
        ds_VT.append(i)  

# In ra các số nguyên tố và vị trí của chúng trong danh sách
print("Các số nguyên tố trong danh sách là:", ds_nt)
print("Vị trí của các số nguyên tố trong danh sách là:", ds_VT)
print("*"*35)