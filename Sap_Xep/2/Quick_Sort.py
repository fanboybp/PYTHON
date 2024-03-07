# Bài tập về nhà: Viết lại các thuật toán  sắp xếp Quick Sort bằng python. 
# Xử lý với file dữ liệu 1000 số
def partition(arr, low, high):
    ptu_cuoi = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= ptu_cuoi:
            # Nếu phần tử hiện tại nhỏ hơn hoặc bằng phần tử cuối cùng
            # Tăng chỉ số của phần tử nhỏ hơn lên 1
            i += 1
            # Đổi chỗ phần tử arr[i] và arr[j]
            arr[i], arr[j] = arr[j], arr[i]
    # Đổi chỗ phần tử cuối cùng và phàn tử arr[i + 1]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        # Tìm phần tử cuối cùng
        pi = partition(arr, low, high)
        # Sắp xếp phần tửu nhỏ hơn phần tử cuối cùng
        quick_sort(arr, low, pi - 1)
        # Sắp xếp các phần tử lớn hơn phần tử cuối cùng
        quick_sort(arr, pi + 1, high)

def read_file(file):
    numbers = []
    with open(file, 'r') as f:
        for line in f:
            for num in line.split():
                numbers.append(int(num.strip()))
    return numbers

# def remove(numbers):
#     unique_numbers = list(set(numbers))
#     return unique_numbers

file = 'E:\\Python\\Python\\PYTHON\\Sap_Xep\\2\\1000.txt'
numbers = read_file(file)
# numbers = remove(numbers)
quick_sort(numbers, 0, len(numbers) - 1)

with open('E:\\Python\\Python\\PYTHON\\Sap_Xep\\2\\output.txt', 'w') as f:
    for i, numbers in enumerate(numbers):
        f.write(str(numbers))
        if (i + 1) % 100 == 0:
            f.write('\n')
        else:
            f.write('\t\t')
    print('Xong!')