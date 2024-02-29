# Viết chương trình Python để in ra bảng cửu chương từ 1 đến 10
print('------------------------')
print('Writen by Nguyễn Văn Luân')
print('------------------------')

# In ra bảng cửu chương từ số 1 đến số 10
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}", end="\n---------------\n")
print("Chương trình đã kết thúc.")