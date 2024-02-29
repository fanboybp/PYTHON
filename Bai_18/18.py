# Viết chương trình Python để in ra tất cả các số hoàn hảo từ 1 đến n (n là một số nguyên dương nhập từ bàn phím). 
# Một số hoàn hảo là một số mà tổng các ước của nó (không kể chính nó) bằng chính nó.

print('------------------------')
print('Writen by Nguyễn Văn Luân')
print('------------------------')

# Hàm kiểm tra xem một số có phải là số hoàn hảo hay không
def so_hoan_hao(num):
    sum = 0
    # Duyệt qua tất cả các số từ 1 đến num - 1
    for i in range(1, num):
        # Kiểm tra nếu i là ước số của num
        if num % i == 0:
            sum += i
    # Trả về True nếu tổng các ước số bằng chính số đó (num)
    return sum == num

# Hàm tạo danh sách các số hoàn hảo từ 1 đến n
def so_hh_den_n(n):
    nso_hh = []
     # Duyệt qua tất cả các số từ 1 đến n
    for i in range(1, n + 1):
        # Kiểm tra xem số i có phải là số hoàn hảo không
        if so_hoan_hao(i):
            # Nếu là số hoàn hảo, thêm vào danh sách
            nso_hh.append(i)
    # Trả về danh sách các số hoàn hảo từ 1 đến n
    return nso_hh
# Nhập n từ bàn phím
n = int(input('n = '))
# Gọi hàm để tạo danh sách các số hoàn hảo từ 1 đến n
ds_so_hh = so_hh_den_n(n)
# In kết quả
print("Các số hoàn hảo từ 1 đến", n, "là:", ds_so_hh)
