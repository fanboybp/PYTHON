# Viết chương trình Python để in ra tất cả các số nguyên tố từ 2 đến n (n là một số nguyên dương nhập từ bàn phím).

print('------------------------')
print('Writen by Nguyễn Văn Luân')
print('------------------------')

# Hàm kiểm tra một số có phải là số nguyên tố không
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

import math

# Nhập số nguyên dương n
n = int(input('n = '))

# In các số nguyên tố từ 2 đến n
print("Các số từ 2 đến", n, "là:")
for num in range(2, n + 1):
    if is_prime(num):
        print(num, end = '\t')
