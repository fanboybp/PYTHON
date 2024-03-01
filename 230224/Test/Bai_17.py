# Viết chương trình Python chèn một số m (m nhập vào từ bàn phím ) vào đầu danh sách, cuối danh sách và vị trí thứ 5 của danh sách.
print("*"*35)
lst = [-10, -5, 1, 2, 4, 10, 15, 28, 30, 51, 32, 32, 32, 22, 7, -3, -11, 9, 22, 1000, 88]

# Danh sách lúc đầu
print("Danh sách lúc đầu là:")
print(lst)

m = int(input('m = '))
lst.insert(0, m) # Chèn đầu
lst.append(m) # chèn cuối
lst.insert(4, m) # Chèn vt thứ 5

# In
print("Danh sách sau khi chèn số m là:")
print(lst)
print("*"*35)