# Viết chương trình Python để tính tổng của tất cả các số lẻ từ 1 đến n (n là một số nguyên dương nhập từ bàn phím).

print('------------------------')
print('Writen by Nguyễn Văn Luân')
print('------------------------')

# Tính tổng các số lẻ từ 1 đến n

S = 0
n = int(input('n = '))
if n < 0:
    print("n là số nguyên dương! Vui lòng nhập lại.")
else:
    for i in range(1, n + 1, 2):
        S += i
    # In kết quả
    print("Tổng các số lẻ là: ", S)