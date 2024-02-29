# Viết chương trình Python sắp xếp danh sách theo thứ tự tăng dần, giảm dần.
print("*"*35)
lst = [-10, -5, 1, 2, 4, 10, 15, 28, 30, 51, 32, 32, 32, 22, 7, -3, -11, 9, 22, 1000, 88]
print("Danh sách lúc đầu là:", lst)
lst.sort()
print("Danh sách theo thứ tự tăng dần là:", lst)
lst.reverse()
print("Danh sách theo thứ tự giảm dần là:", lst)
print("*"*35)