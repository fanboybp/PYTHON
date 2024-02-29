# Viết chương trình Python để tìm số nguyên tố lớn nhất nhỏ hơn hoặc bằng n (n là một số nguyên dương nhập từ bàn phím).

print('------------------------')
print('Writen by Nguyễn Văn Luân')
print('------------------------')

# Hàm kiểm tra xem một số có phải số nguyên tố hay không
def so_nt(s):
    # Số nhỏ hơn 2 không phải số nguyên tố
    if s < 2:
        return False
    # Duyệt qua các số từ 2 đến căn bậc 2 của s
    for i in range(2, int(s ** 0.5) + 1):
        # Nếu số chia hết cho một số trong khoảng này, không phải số nguyên tố
        if s % i == 0:
            return False
    # Nếu không chia hết cho bất kỳ số nào trong khoảng trên, là số nguyên tố
    return True

# Hàm tìm số nguyên tố lớn nhất nhỏ hơn hoặc bằng n
def so_nt_max1(n):
    so_ngto = None
    # Duyệt từ n về 2 (lớn dần)
    for i in range (n, 1, -1):
        # Nếu i là số nguyên tố, gán cho so_ngto và kết thúc vòng lặp
        if  so_nt(i):
            so_ngto = i
            break
    return so_ngto

# Nhập số n
n = int(input('n = '))
# Gọi hàm để tìm số nguyên tố lớn nhất nhỏ hơn hoặc bằng n
so_ngto = so_nt_max1(n)
# Kiểm tra nếu có số nguyên tố lớn nhất nhỏ hơn hoặc bằng n
if so_ngto is not None:
    print("Số nguyên tó lớn nhất nhỏ hơn hoặc bằng", n, "là:", so_ngto)
else:
    print("Không có số nguyên tố nào nhỏ hơn hoặc bằng", n)