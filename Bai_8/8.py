# Viết chương trình Python để tìm số Fibonacci.
print('------------------------')
print('Writen by Nguyễn Văn Luân')
print('------------------------')

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Nhập số lượng số Fibonacci cần tính: "))
fib = [fibonacci(i) for i in range(n)]
print(f"Các số Fibonacci đầu tiên là: {fib}")