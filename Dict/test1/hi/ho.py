# -*- coding: utf-8 -*-
from collections import Counter
import codecs
#-----------------------------------------
# Chương trình chính
print("--------------------------------------\n")
print("     CHƯƠNG TRÌNH THỐNG KÊ TỪ        \n")
print("---------------------------------------\n")
# Mở file nguồn chỉ đọc read
fsource = codecs.open("E:\\Python\\Python\\PYTHON\\Dict\\test1\\hi\\roses.txt", 'r', "utf-8")
dict_Word = {}      # Biến lưu trữ từ điển các từ và số lần sử dụng nó
for line in fsource:    # Đọc toàn bộ file, mỗi lần đọc 1 dòng
    maxline = len(line)
    i = 0
    while i < maxline:
        # Loại bỏ các dấu chấm câu
        if line[i] == "." or line[i] == "," or line[i] == ";":
            line = line[:i] + line[i + 1:]
            maxline = maxline - 1
        i = i + 1
    list = line.split()     # Biến đổi dòng vừa đọc thành dạng list
    print(line)
    
    count_Word = Counter(list)    # Thống kê từng từ trong dòng list vừa rồi lưu trữ vào từ điển count_Word
    print(count_Word)
    for word in count_Word:     # Cập nhật nó vào trong từ điển dict
        if word in dict_Word: # Nếu đã có rồi thì cập nhật thêm số thống kê
            dict_Word[word] = dict_Word[word] + count_Word[word]    # Cập nhật
        else:
            dict_Word.setdefault(word, count_Word[word])    # Nếu chưa có thì thêm mới phần tử này
        #print(word, " ", count[word])
fsource.close() # Đọc xong rồi thì đóng file lại
# Mở file đích để ghi write
ftarget = codecs.open("E:\\Python\\Python\\PYTHON\\Dict\\test1\\hi\\roses1.txt", 'w', "utf-8")
# Ghi vào file
for word in dict_Word:
    ftarget.write(word + " : " + str(dict_Word[word]) + '\n')
print("*"*100)
ftarget.close()