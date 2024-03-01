# Viết chương trình Python tìm phần tử lớn thứ nhì của danh sách và các vị trí của các phần tử đạt giá trị lớn nhì.
print("*"*35)
lst = [-10, -5, 1, 2, 4, 10, 15, 28, 30, 51, 32, 32, 32]
ptu_max = max(lst)
ptu2 = float('-inf')
VT = 0

# Danh sách lúc đầu
print("Danh sách lúc đầu là:", lst)

for i in range(len(lst)):
    if lst[i] < ptu_max and lst[i] > ptu2:
        ptu2 = lst[i]
        VT = [i]
    elif lst[i] == ptu2:
        VT.append(i)
        
print("Phần tử lớn thứ nhì của danh sách là:", ptu2)
print("Các vị trí của phần tử đạt giá trị lớn nhì là:", VT)
print("*"*35)