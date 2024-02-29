# Viết chương trình Python để in ra tất cả các số Armstrong từ 1 đến n (n là một số nguyên dương nhập từ bàn phím). 
# Một số Armstrong là một số mà tổng lũy thừa của các chữ số của nó bằng chính nó.

print('------------------------')
print('Writen by Nguyễn Văn Luân')
print('------------------------')

def armstrong(num):
    # Chuyển số thành chuỗi để dễ xử lý từng chữ số
    num_str = str(num)
    # Số chữ số trong num
    num_digits = len(num_str)
    # Tính tổng lũy thừa các chữ số
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    # Trả về True nếu tổng lũy thừa bằng chính số đó (num)
    return armstrong_sum == num

def armstrong_to_n(n):
    armstrong_n = []
    for i in range (1, n + 1):
        if armstrong(i):
            armstrong_n.append(i)
    return armstrong_n

# Nhập n từ bán phím
n = int(input('n = '))
armstrong_n_list = armstrong_to_n(n)
print("Các số Armstrong từ 1 đến", n, "là:", armstrong_n_list)