# Viết chương trình Python để tìm số nguyên tố.
print('------------------------')
print('Writen by Nguyễn Văn Luân')
print('------------------------')

def so_nt(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Nhập số nguyên tố
n = int(input('n = '))

if so_nt(n):
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không là số nguyên tố")