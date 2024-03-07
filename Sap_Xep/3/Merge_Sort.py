# Bài tập về nhà: Viết lại các thuật toán  sắp xếp Merge Sort bằng python. 
# Xử lý với file dữ liệu 1000 số

def  merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Tìm chỉ số giữa 2 mảng
        left = arr[:mid]    # Chia thành 2 phần
        right = arr[mid:]
        
        merge_sort(left)    # Gọi đệ quy để sắp xếp nửa trái
        merge_sort(right)
        
        # Merge 2 nửa đã sắp xếp
        i =  j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        # Sao chép nếu còn
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        # Sao chép nếu còn
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

def read(file):
    numbers = []
    with open(file, 'r') as f:
        for line in f:
            for num in line.split():
                numbers.append(int(num.strip()))
    return numbers

# def remove(numbers):
#      unique_numbers = list(set(numbers))
#      return unique_numbers

file = 'E:\\Python\\Python\\PYTHON\\Sap_Xep\\3\\1000.txt'
numbers = read(file)
# numbers = remove(numbers)
sorted_numbers = merge_sort(numbers)

if sorted_numbers == sorted(numbers):
    print("Thuật toán Merge Sort đã đúng.")
else:
    print("Thuật toán Merge Sort chưa đúng.")

with open('E:\\Python\\Python\\PYTHON\\Sap_Xep\\3\\output.txt', 'w') as f:
    for i, numbers in enumerate(sorted_numbers):
        f.write(str(numbers))
        if (i + 1) % 100 == 0:
            f.write('\n')
        else:
            f.write('\t\t')
    print('Xong!')
