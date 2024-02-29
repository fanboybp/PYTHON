# Viết chương trình Python để tính tổng của tất cả các số chia hết cho 3 hoặc 5 từ 1 đến n (n là một số nguyên dương nhập từ bàn phím).

print('------------------------')
print('Writen by Nguyễn Văn Luân')
print('------------------------')

# Tổng các số chia hết cho 3 hoặc 5 từ 1 đến n

S = 0
n = int(input('n = '))
if n < 0:
    print("n là số nguyên dương! Vui lòng nhập lại.")
else:
    for i in range(1, n + 1):
        if (i % 3 == 0 or i % 5 == 0):
            S += i
    print("Tổng các số chia hết cho 3 hoặc 5 là: ", S)