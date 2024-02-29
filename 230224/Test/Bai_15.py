#  Viết chương trình Python chuyển các phần tử dương của danh sách lên đầu danh sách và in danh sách ra màn hình.

print("*"*35)
lst = [-10, -5, 1, 2, 4, 10, 15, 28, 30, 51, 32, 32, 32, 22, 7, -3, -11, 9, 22, 1000, 88]

ds_ptu_duong = []
ds_new = []

for i in lst:
    if i > 0:
        ds_ptu_duong.append(i)
    else:
        ds_new.append(i)

new_ds = ds_ptu_duong + ds_new

# In
print("Danh sách sau khi các phần tử dương được chuyển lên đầu là:")
print(new_ds)
print("*"*35)