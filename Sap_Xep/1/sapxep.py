# Viết lại các thuật toán  sắp xếp (1) Heap Sort bằng python. Xử lý với file dữ liệu 1000 số
# Sắp xếp

# -*- coding: utf-8 -*-
from collections import Counter
import codecs

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Xây dựng max heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract từng phần tử từ heap đã xây dựng.
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Hoán đổi
        heapify(arr, i, 0)

def read_file(file):
    numbers = []
    with open(file, 'r') as f:
        for line in f:
            for num in line.split():
                numbers.append(int(num.strip()))
    return numbers

file = 'E:\\Python\\Python\\PYTHON\\Sap_Xep\\1\\1000.txt'
numbers = read_file(file)
heap_sort(numbers)

# Xóa số trùng nhau
# unique_numbers = list(set(numbers))
# unique_numbers.sort()

with open('E:\\Python\\Python\\PYTHON\\Sap_Xep\\1\\output.txt', 'w') as f:
    for i, number in enumerate(numbers):
        f.write(str(number))
        if (i + 1) % 100 == 0:  # Ghi 100 số trên mỗi dòng
            f.write('\n')
        else:
            f.write('\t\t')
    print('Xong!')