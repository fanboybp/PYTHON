# Viết chương trình Python để kiểm tra xem một chuỗi có phải là chuỗi đối xứng hay không.

print('------------------------')
print('Writen by Nguyễn Văn Luân')
print('------------------------')

def is_palindrome(s):
    return s == s[::-1]

# Đọc chuỗi từ file input.txt
with open('E:/Python/Bai_10/input.txt', 'r') as f:
    s = f.read().strip()

# Kiểm tra xem chuỗi có phải chuỗi đối xứng hay không
if is_palindrome(s):
    print(s, "là chuỗi đối xứng.")
else:
    print(s, "không phải chuỗi đối xứng.")