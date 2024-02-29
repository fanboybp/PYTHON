# Viết chương trình Python để tính tổng các số chẵn trong một danh sách các số nguyên.

print('------------------------')
print('Writen by Nguyễn Văn Luân')
print('------------------------')

# Đọc chuỗi từ file input.txt
with open('E:/Python/Bai_16/input.txt', 'r') as f:
    numbers = [int(num) for line in f for num in line.split()]

# Tính tổng các số chẵn
even_sum = sum(num for num in numbers if num % 2 == 0)

# In kết quả
print(f'Tổng số chẵn là: {even_sum}')