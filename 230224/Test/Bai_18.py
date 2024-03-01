# Viết chương trình Python chèn danh sách [1,2,3] vào vị trí đầu, cuối và thứ 5 của danh sách

print("*"*35)
lst = [-10, -5, 4, 10, 15, 28, 30, 51, 32, 32, 32, 22, 7, -3, -11, 9, 22, 1000, 88]
# Danh sách lúc đầu
print("Danh sách lúc đầu là:")
print(lst)

ds = [1, 2, 3]
lst = ds + lst # Chèn đầu
lst += ds # Chèn cuối
lst = lst[:4] + ds + lst[4:] # Chèn Vị trí thứ 5

# In
print("Danh sách sau khi chèn là:")
print(lst)
print("*"*35)
